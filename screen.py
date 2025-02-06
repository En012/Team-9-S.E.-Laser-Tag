import tkinter as tk
import os
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Image Display")
root.configure(bg="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

img_path = os.path.expanduser("images/logo.jpg")
def switch():
    global img, label, height, width
    img_path = os.path.expanduser("images/lebron.jpg")
    img = Image.open(img_path)
    img = img.resize((width, height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label.configure(image=img)


img = Image.open(img_path)
img = img.resize((width, height), Image.LANCZOS)
img = ImageTk.PhotoImage(img)
label = tk.Label(root, image=img, bg="black")    
label.pack()
root.after(3000, switch)
root.mainloop()