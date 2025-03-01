import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont

from udpbutton import UDPButton
from addplayerbutton import AddPlayerButton

class Display:

    #default constructor
    def __init__(self):

        #setup default values for name and ID list for red and green team
        self.redNameList = ["None"] * 15
        self.redIDList = ["None"] * 15
        self.greenNameList = ["None"] * 15
        self.greenIDList = ["None"] * 15

        #setup tkinter GUI elements
        self.root = tk.Tk()
        self.root.title("Loading...")
        self.root.configure(bg="black")

        #create objects for the three buttons
        #THESE CLASSES DO NOT HANDLE DISPLAYING THE BUTTONS, they handle the code that is run when the button is pressed
        self.UDPButton = UDPButton(self.root)
        self.AddPlayerButton = AddPlayerButton(self.root, self.redIDList, self.greenIDList, self.redNameList, self.greenNameList)

        #get screen self.width and self.height
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        #initalize self.image and open the splash screen
        self.img = Image.open("images/logo.jpg")
        self.splash_screen()

        #switch to player entry screen after 3000 milliseconds
        self.root.after(3000, self.switchToPlayerEntry)
        

    #code for the splash screen
    def splash_screen(self):
        self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.root, image=self.img, bg="black")    
        label.pack()
        self.root.geometry(f"{self.width}x{self.height}")
    
    #switch to playerEntryScreen
    def switchToPlayerEntry(self):
        self.player_entry_screen()

    #code for the player entry screen
    def player_entry_screen(self):
        #setting name of window
        self.root.title("Photon")
        self.root.minsize(800,600)

        #setting the sizes
        title_relheight = 0.1  # 10% of the window is for title
        button_relheight = 0.1  # 10% for the buttons at the bottom
        row_count = 15
        row_relheight = (1 - title_relheight - button_relheight) / row_count

        #Set background colors
        red_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="red")
        green_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="green")

        #Title Placement
        titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
        title = tk.Label(self.root, font=titlefont, text="Edit Current Game", background="black", fg="white")
        title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")

        #Place background frames
        red_frame.place(relx=0, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)
        green_frame.place(relx=0.5, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)

        # Create StringVars for dynamic updates
        self.id_vars = [tk.StringVar(value=self.redIDList[i]) for i in range(15)]
        self.name_vars = [tk.StringVar(value=self.redNameList[i]) for i in range(15)]
        self.id_vars2 = [tk.StringVar(value=self.greenIDList[i]) for i in range(15)]
        self.name_vars2 = [tk.StringVar(value=self.greenNameList[i]) for i in range(15)]

        # Create labels for red team
        id_label = tk.Label(self.root, text='ID', font=('calibre', 12, 'bold'), background="red")
        id_label.place(relx=0.151, rely=0.12, anchor="center")

        name_label = tk.Label(self.root, text='Name', font=('calibre', 12, 'bold'), background="red")
        name_label.place(relx=0.348, rely=0.12, anchor="e")
        for i in range(row_count):
            row_rel_y = title_relheight + (i + 1.0) * row_relheight  

            num_label = tk.Label(self.root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="red")
            num_label.place(relx=0.075, rely=row_rel_y, anchor="center")

            id_entry = tk.Label(self.root, textvariable=self.id_vars[i], font=('calibre', 10, 'normal'), background="white")
            id_entry.place(relx=0.15, rely=row_rel_y, relwidth=0.1, anchor="center")

            name_entry = tk.Label(self.root, textvariable=self.name_vars[i], font=('calibre', 10, 'normal'), background="white")
            name_entry.place(relx=0.33, rely=row_rel_y, relwidth=0.15, anchor="center")

        # Create labels for green team
        id_label2 = tk.Label(self.root, text='ID', font=('calibre', 12, 'bold'), background="green")
        id_label2.place(relx=0.658, rely=0.12, anchor="e")

        name_label2 = tk.Label(self.root, text='Name', font=('calibre', 12, 'bold'), background="green")
        name_label2.place(relx=0.848, rely=0.12, anchor="e")
        for i in range(row_count):
            row_rel_y = title_relheight + (i + 1.0) * row_relheight  

            num_label2 = tk.Label(self.root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="green")
            num_label2.place(relx=0.575, rely=row_rel_y, anchor="center")

            id_entry2 = tk.Label(self.root, textvariable=self.id_vars2[i], font=('calibre', 10, 'normal'), background="white")
            id_entry2.place(relx=0.65, rely=row_rel_y, relwidth=0.1, anchor="center")

            name_entry2 = tk.Label(self.root, textvariable=self.name_vars2[i], font=('calibre', 10, 'normal'), background="white")
            name_entry2.place(relx=0.83, rely=row_rel_y, relwidth=0.15, anchor="center")
        
        self.player_entry_buttons()

    # Handles all the code for displaying buttons and calling the appropriate method
    def player_entry_buttons(self):
        # button to activate the start game function
        # lambda prevents the startGame function from being called as soon as the program starts up
        sub_btn = tk.Button(self.root, text='Start Game', command=lambda: self.startGame(), width=15, height=3)

        # button to activate the change address function
        address_btn = tk.Button(self.root, text="Change Address", command=self.UDPButton.change_udp_client_inter, width=15, height=3)

        # button for adding a player to the game
        add_btn = tk.Button(self.root, text='Add Player',
                            command=lambda: self.AddPlayerButton.addPlayer(self.id_vars, self.name_vars, self.id_vars2, self.name_vars2),
                            width=15, height=3)

        # Button placement
        sub_btn.place(relx=0.5, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        address_btn.place(relx=0.2, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        add_btn.place(relx=0.8, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)

    #function for starting the game, to be fully implemented later
    def startGame(self):
        numRedPlayers = 0
        numGreenPlayers = 0

        #check to make sure that a player is on each team
        for i in range(15):
            if self.redIDList[i] != "None":
                numRedPlayers += 1
            
            if self.greenIDList[i] != "None":
                numGreenPlayers += 1

        #if both teams dont have at least one player, throw an error
        if numRedPlayers == 0 or numGreenPlayers == 0:
            messagebox.showerror(title="Error", message="You must have at least one player on each team to start a game!")
            return
        #otherwise, start the game
        else:
            messagebox.showinfo(title="Notification", message="Start will be implemented in a future sprint!")

    # countdown timer function
    def timer(self, seconds=30):
        if seconds >= 0:
            print(f"{seconds}\n")
            img_path = os.path.expanduser(f"images/{seconds}.tif")
            self.img = Image.open(img_path)
            self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(self.img)
            label = tk.Label(self.root, image=self.img, bg="black")
            label.pack()
            self.root.after(1000, self.timer, seconds - 1)
        else:
            self.player_entry_screen()
