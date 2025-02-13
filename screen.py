import tkinter as tk
import tkinter.font as tkFont
import os
import playerentryscreentest2 as pe
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Display")
root.configure(bg="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

img_path = os.path.expanduser("images/logo.jpg")
def switch():
    pe.player_entry_screen(root)


img = Image.open(img_path)
img = img.resize((width, height), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=img, bg="black")    
label.pack()
root.after(3000, switch)
root.mainloop()