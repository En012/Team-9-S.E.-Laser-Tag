import tkinter as tk
import os
import tkinter.font as tkFont
from PIL import Image, ImageTk
import time
import __main__

class Display:
    # def __init__(self, root):
    #     # Initialize something?

    def player_entry_screen(root):
        #setting name of window
        root.title("Photon")
        root.minsize(800,600)

        #setting the sizes
        title_relheight = 0.1  # 10% of the window is for title
        button_relheight = 0.1  # 10% for the buttons at the bottom
        row_count = 15
        row_relheight = (1 - title_relheight - button_relheight) / row_count

        #Set background colors
        red_frame = tk.Frame(root, bd=0, highlightthickness=0, background="red")
        green_frame = tk.Frame(root, bd=0, highlightthickness=0, background="green")

        #Title Placement
        titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
        title = tk.Label(root, font=titlefont, text="Edit Current Game", background="black", fg="white")
        title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")

        #Place background frames
        red_frame.place(relx=0, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)
        green_frame.place(relx=0.5, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)

        # Red & Green Team User Lists
        name_List = ["None"] * 15
        id_List = ["None"] * 15
        name_List2 = ["None"] * 15
        id_List2 = ["None"] * 15

        # Create StringVars for dynamic updates
        id_vars = [tk.StringVar(value=id_List[i]) for i in range(15)]
        name_vars = [tk.StringVar(value=name_List[i]) for i in range(15)]
        id_vars2 = [tk.StringVar(value=id_List2[i]) for i in range(15)]
        name_vars2 = [tk.StringVar(value=name_List2[i]) for i in range(15)]

        # Create labels for red team
        id_label = tk.Label(root, text='ID', font=('calibre', 12, 'bold'), background="red")
        id_label.place(relx=0.151, rely=0.12, anchor="center")

        name_label = tk.Label(root, text='Name', font=('calibre', 12, 'bold'), background="red")
        name_label.place(relx=0.348, rely=0.12, anchor="e")
        for i in range(row_count):
            row_rel_y = title_relheight + (i + 1.0) * row_relheight  

            num_label = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="red")
            num_label.place(relx=0.075, rely=row_rel_y, anchor="center")

            id_entry = tk.Label(root, textvariable=id_vars[i], font=('calibre', 10, 'normal'), background="white")
            id_entry.place(relx=0.15, rely=row_rel_y, relwidth=0.1, anchor="center")

            name_entry = tk.Label(root, textvariable=name_vars[i], font=('calibre', 10, 'normal'), background="white")
            name_entry.place(relx=0.33, rely=row_rel_y, relwidth=0.15, anchor="center")

        # Create labels for green team
        id_label2 = tk.Label(root, text='ID', font=('calibre', 12, 'bold'), background="green")
        id_label2.place(relx=0.658, rely=0.12, anchor="e")

        name_label2 = tk.Label(root, text='Name', font=('calibre', 12, 'bold'), background="green")
        name_label2.place(relx=0.848, rely=0.12, anchor="e")
        for i in range(row_count):
            row_rel_y = title_relheight + (i + 1.0) * row_relheight  

            num_label2 = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="green")
            num_label2.place(relx=0.575, rely=row_rel_y, anchor="center")

            id_entry2 = tk.Label(root, textvariable=id_vars2[i], font=('calibre', 10, 'normal'), background="white")
            id_entry2.place(relx=0.65, rely=row_rel_y, relwidth=0.1, anchor="center")

            name_entry2 = tk.Label(root, textvariable=name_vars2[i], font=('calibre', 10, 'normal'), background="white")
            name_entry2.place(relx=0.83, rely=row_rel_y, relwidth=0.15, anchor="center")

        #Buttons

        #button to activate the start game function
        #lambda prevents the startGame function from being called as soon as the program starts up
        sub_btn=tk.Button(root,text = 'Start Game', command = lambda: __main__.startGame(id_List, id_List2), width = 15, height = 3)

        #button to activate the change address function
        address_btn= tk.Button(root, text="Change Address", command=__main__.change_udp_client_inter, width = 15, height = 3)

        #button for adding a player to the game
        add_btn = tk.Button(root, text='Add Player', 
                            command=lambda: __main__.addPlayer(root, id_List, name_List, id_List2, name_List2, id_vars, name_vars, id_vars2, name_vars2), 
                            width=15, height=3)

        # Button placement
        sub_btn.place(relx=0.5, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        address_btn.place(relx=0.2, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        add_btn.place(relx=0.8, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)

    #switch to playerEntryScreen
    def switch(root):
        Display.player_entry_screen(root)

    #countdown timer test function
    seconds = 30
    def timer(root):
        global seconds, img, label, width, height
        if(seconds >= 0):
            print(f"{seconds}\n")
            img_path = os.path.expanduser(f"images/{seconds}.tif")
            seconds = seconds - 1
            root.after(1000, Display.timer)
        else:
            Display.player_entry_screen(root)
        img = Image.open(img_path)
        img = img.resize((width, height), Image.LANCZOS)
        img = ImageTk.PhotoImage(img)
        label.configure(image=img)