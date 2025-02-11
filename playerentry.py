import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import font as tkFont

root = tk.Tk()
root.title("Image Display")
root.configure(bg="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

codename_table_red = []
codename_table_green = []
id_table_red = []
id_table_green = []


def get_id_texts():
    red_ids = [id_field.cget("text") for id_field in id_table_red]
    green_ids = [id_field.cget("text") for id_field in id_table_green]
    red_names = [id_field.cget("text") for id_field in codename_table_red]
    green_names = [id_field.cget("text") for id_field in codename_table_green]

    print("Red IDs:", red_ids)
    print("Green IDs:", green_ids)
    print("Red Names:", red_names)
    print("Green Names:", green_names)
    return red_ids, green_ids, red_names, green_names

def change_button():
    box_font = tkFont.Font(family="Calibri", size=16, weight="bold")
    box = tk.Label(root, font=box_font, width=20, height=20, text="Please Select Slot to Change")
    #boxwidth = box.winfo_reqwidth()
    #boxheight = box.winfo_reqheight()
    #box.place(x=int(width/2 - boxwidth/2), y=int(height/2 - boxheight/2))
    
    # Fetch and print ID texts
    red_ids, green_ids, red_names, green_names = get_id_texts()
    print("Red IDs:", red_ids)
    print("Green IDs:", green_ids)
    print("Red Names:", red_names)
    print("Green Names:", green_names)

#Set background colors
red_frame = tk.Frame(bd=0, highlightthickness=0, background="red")
green_frame = tk.Frame(bd=0, highlightthickness=0, background="green")
#green_frame = tk.Frame(bd=0, highlightthickness=0, background="blue")
red_frame.place(x=0, y=0, relwidth=.5, relheight=1.0, anchor="nw")
green_frame.place(relx=.5, y=0, relwidth=.5, relheight=1.0, anchor="nw")

#Set Edit Current Game
titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
title_left = tk.Label(root, font=titlefont, text="Edit Curr", background="red")
title_right = tk.Label(root, font=titlefont, text="ent Game", background="green")
#title_right = tk.Label(root, font=titlefont, text="ent Game", background="blue")
title_left_width = title_left.winfo_reqwidth()
title_height = title_left.winfo_reqheight()
placetitle = int(int(width/2) - int(title_left_width))
half_width = int(width/2)
title_right.place(x = half_width, anchor="nw")
title_left.place(x = placetitle, anchor="nw")



#Make num_text
num_font = tkFont.Font(family="Calibri", size=16, weight="bold")
number = tk.Label(root, font=num_font, text="")
num_height = number.winfo_reqheight()
num_width = number.winfo_reqwidth()
#make id field
id_font = num_font
char_width = id_font.measure("0")
id_width = char_width * 15
#id_table_red = []
#id_table_green = []
#make codename field
codename_font = id_font
codename_width = int(id_width * 2)
#codename_table_red = []
#codename_table_green = []


#Red side numbers, id field, and codename field
for i in range(15):
    number = tk.Label(root, font=num_font, text=i + 1, background="red")
    if(i < 9):
        #Can't tell which looks better
        number.place(x = num_width/3, y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        #number.place(x = num_width/4, y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Label(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(num_width * 12), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Label(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int((id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        codename_table_red.append(codename)
    else:
        number.place(y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Label(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(num_width * 12), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id_table_red.append(id)
        codename = tk.Label(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int((id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        codename_table_red.append(codename)

#Green side numbers, id field, and codename field
for j in range(15):
    number = tk.Label(root, font=num_font, text=j + 1, background="green")
    #number = tk.Label(root, font=num_font, text=j + 1, background="blue")
    if(j < 9):
        #Can't tell which looks better
        number.place(x = int(half_width + num_width/3), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        #number.place(x = int(half_width +num_width/4), y = int(int(title_height) + int((num_height + 10) * (i + 1))), anchor="nw")
        id = tk.Label(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(half_width + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id_table_green.append(id)
        codename = tk.Label(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int(half_width + (id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        codename_table_green.append(codename)
    else:
        number.place(x = half_width, y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id = tk.Label(root, font=id_font, borderwidth=1, width=15, height = 1)
        id.place(x = int(half_width + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        id_table_green.append(id)
        codename = tk.Label(root, font=codename_font, borderwidth=1, width = 40, height=1)
        codename.place(x = int(half_width + (id_width + 15) + num_width * 6), y = int(int(title_height) + int((num_height + 10) * (j + 1))), anchor="nw")
        codename_table_green.append(codename)

for i2 in range(15):
    id_table_red[i2].config(text= "123")
    codename_table_red[i2].config(text= "win")
for j2 in range(15):
    id_table_green[j2].config(text="123")
    codename_table_green[j2].config(text= "win")
#print button
button = tk.Button(root, text="Change", command=change_button)
button.place(x = 20, y = int(int(title_height) + int((num_height + 10) * (i + 2))), anchor="nw")
#Go
root.geometry(f"{width}x{height}")

root.mainloop()