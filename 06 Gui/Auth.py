import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


class AuthApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Login System")
        self.root.geometry("300x300")

        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.current_user = None

        self.create_table()
        self.login_screen()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        """)
        self.conn.commit()

    def hash_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    # ---------- Screens ----------
    def login_screen(self):
        self.clear()

        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.login_username = tk.Entry(self.root)
        self.login_username.pack()

        tk.Label(self.root, text="Password").pack()
        self.login_password = tk.Entry(self.root, show="*")
        self.login_password.pack()

        tk.Button(self.root, text="Login", command=self.login).pack(pady=5)
        tk.Button(self.root, text="Register", command=self.register_screen).pack()

    def register_screen(self):
        self.clear()

        tk.Label(self.root, text="Register", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Username").pack()
        self.reg_username = tk.Entry(self.root)
        self.reg_username.pack()

        tk.Label(self.root, text="Password").pack()
        self.reg_password = tk.Entry(self.root, show="*")
        self.reg_password.pack()

        tk.Button(self.root, text="Register Account", command=self.register).pack(pady=5)
        tk.Button(self.root, text="Back to Login", command=self.login_screen).pack()

    def dashboard_screen(self):
        self.clear()

        tk.Label(self.root, text="Dashboard", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text=f"Welcome {self.current_user}").pack(pady=10)

        tk.Button(self.root, text="Logout", command=self.logout).pack()

    # ---------- Logic ----------
    def register(self):
        username = self.reg_username.get()
        password = self.reg_password.get()

        if not username or not password:
            messagebox.showerror("Error", "All fields required")
            return

        hashed = self.hash_password(password)

        try:
            self.cursor.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, hashed)
            )
            self.conn.commit()
            messagebox.showinfo("Success", "Registration successful")
            self.login_screen()
        except sqlite3.IntegrityError:
            messagebox.showerror("Error", "Username already exists")

    def login(self):
        username = self.login_username.get()
        password = self.login_password.get()

        hashed = self.hash_password(password)

        self.cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (username, hashed)
        )

        user = self.cursor.fetchone()

        if user:
            self.current_user = username
            self.dashboard_screen()
        else:
            messagebox.showerror("Error", "Invalid credentials")

    def logout(self):
        self.current_user = None
        self.login_screen()


# ---------- Run App ----------
root = tk.Tk()
app = AuthApp(root)
root.mainloop()
