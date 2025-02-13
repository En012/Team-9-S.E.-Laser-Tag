import tkinter as tk
import tkinter.font as tkFont
import os
import playerentryscreentest2 as pe
from PIL import Image, ImageTk

class Screen:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Display")
        self.root.configure(bg="black")

        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        img_path = os.path.expanduser("images/logo.jpg")
        self.img = Image.open(img_path)
        self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        self.label = tk.Label(self.root, image=self.img, bg="black")
        self.label.pack()
        self.root.after(3000, self.switch)

    def switch(self):
        pe.player_entry_screen(self.root)