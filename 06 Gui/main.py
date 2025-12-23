import tkinter as tk
from tkinter import messagebox

class ButtonCalling:
    def __init__(self, root):
        self.root = root
        self.root.title("Button Calling")

        self.button = tk.Button(
            root,
            text="Click Me",
            command=self.show_message
        )
        self.button.pack(pady=20)

    def show_message(self):
        messagebox.showinfo("Message", "Button clicked!")


root = tk.Tk()
app = ButtonCalling(root)
root.mainloop()
