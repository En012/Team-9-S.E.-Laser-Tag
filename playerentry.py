import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import font as tkFont

#Set Title of window
root = tk.Tk()
root.title("Player Entry")

#Get information about Screen in use
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

#Set background colors
red_frame = tk.Frame(bd=0, highlightthickness=0, background="red")
green_frame = tk.Frame(bd=0, highlightthickness=0, background="green")
red_frame.place(x=0, y=0, relwidth=.5, relheight=1.0, anchor="nw")
green_frame.place(relx=.5, y=0, relwidth=.5, relheight=1.0, anchor="nw")

#Set Edit Current Game
titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
title_left = tk.Label(root, font=titlefont, text="Edit Curr", background="red")
title_right = tk.Label(root, font=titlefont, text="ent Game", background="green")
title_left_width = title_left.winfo_reqwidth()
title_height = title_left.winfo_reqheight()
placetitle = int(int(width/2) - int(title_left_width))
half_width = int(width/2)
title_left.place(x = placetitle, anchor="nw")
title_right.place(x = half_width , anchor="nw")


#Make num_text
num_font = tkFont.Font(family="Calibri", size=16, weight="bold")
number = tk.Label(root, font=num_font, text="")
num_height = number.winfo_reqheight()
num_width = number.winfo_reqwidth()
#make id field
id_font = num_font
char_width = id_font.measure("0")
id_width = char_width * 15
id_table_red = []
id_table_green = []
#make codename field
codename_font = id_font
codename_width = int(id_width * 2)
codename_table_red = []
codename_table_green = []

#Red side numbers, id field, and codename field
for i in range(15):
    number = tk.Label(root, font=num_font, text=i + 1, background="red")
    if(i < 9):
        #Can't tell which looks better
        number.place(x = num_width/3, y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        #number.place(x = num_width/4, y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Text(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Text(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int((id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        codename_table_red.append(codename)
    else:
        number.place(y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Text(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Text(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int((id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        codename_table_red.append(codename)
    i = i + 1

#Green side numbers, id field, and codename field
for j in range(15):
    number = tk.Label(root, font=num_font, text=j + 1, background="green")
    if(j < 9):
        #Can't tell which looks better
        number.place(x = int(half_width + num_width/3), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        #number.place(x = int(half_width +num_width/4), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Text(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(half_width + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Text(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int(half_width + (id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        codename_table_green.append(codename)
    else:
        number.place(x = half_width, y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id = tk.Text(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(half_width + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Text(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int(half_width + (id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        codename_table_green.append(codename)
    j = j + 1

#Go
root.geometry(f"{width}x{height}")
root.mainloop()