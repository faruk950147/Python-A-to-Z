import tkinter as tk
from tkinter import messagebox

class Canvas:
    def __init__(self, root):
        # It's receive the root canvas from the main.py
        self.root = root
        # Set the title of the canvas
        self.root.title("Canvas")
        # Set the size of the canvas
        self.root.geometry("300x300")
        # Set the canvas to be non-resizable
        self.root.resizable(False, False)
        # Set the background color of the canvas
        self.root.configure(bg="blue")
        # always keep the canvas on top
        self.root.attributes("-topmost", True)
        # no closed canvas
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    
    def on_closing(self):
         messagebox.showinfo("Message", "Button clicked!")
       


root = tk.Tk()
canvas = Canvas(root)
root.mainloop()