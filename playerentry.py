import tkinter as tk
from tkinter import messagebox, font as tkFont

from udpbutton import UDPButton
from addplayerbutton import AddPlayerButton

#This class contains all code for the PlayerEntryScreen
class PlayerEntryScreen:
    #Default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList, switch_to_player_action):

        #Get root, ID, and Name lists from display.py
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList

        #-------------------------------------------------------------------------------------------------------------
        #self.switch_to_player_action is used to switch back to display.py when the "start game" button is pressed
        #In display.py, the switchToPlayerAction function will be called, which will start up the player action screen

        #so when you press the start game button the program counter will go as follows: 
        #startGame in playerentry.py ---> switchToPlayerAction in display.py ---> run in playeraction.py

        self.switch_to_player_action = switch_to_player_action

        #-------------------------------------------------------------------------------------------------------------

        #create objects for the UDP and AddPlayer button
        #THESE OBJECTS DO NOT HANDLE DISPLAYING THE BUTTONS, they handle the code that is run when the buttons are pressed
        self.UDPButton = UDPButton(self.root)
        self.AddPlayerButton = AddPlayerButton(self.root, self.redIDList, self.greenIDList, self.redNameList, self.greenNameList)

    # code for the player entry screen
    def run(self):
        # setting name of window
        self.root.title("Photon")
        self.root.minsize(800, 600)
        self.root.configure(bg="white")

        # setting the sizes
        title_relheight = 0.1  # 10% of the window is for title
        button_relheight = 0.1  # 10% for the buttons at the bottom
        row_count = 15
        row_relheight = (1 - title_relheight - button_relheight) / row_count

        # Set background colors
        red_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="red")
        green_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="green")

        # Title Placement
        titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
        title = tk.Label(self.root, font=titlefont, text="Edit Current Game", background="black", fg="white")
        title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")

        # Place background frames
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
        id_label2.place(relx=0.65, rely=0.12, anchor="center")

        name_label2 = tk.Label(self.root, text='Name', font=('calibre', 12, 'bold'), background="green")
        name_label2.place(relx=0.83, rely=0.12, anchor="center")
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
        sub_btn = tk.Button(self.root, text='Start Game [F5]', command=lambda: self.startGame(), width=15, height=3)

        # button to activate the change address function. Calls method from the UDPButton object
        address_btn = tk.Button(self.root, text="Change Address", command=self.UDPButton.change_udp_client_inter, width=15, height=3)

        # button for adding a player to the game. Calls method from the AddPlayerButton object
        add_btn = tk.Button(self.root, text='Add Player',
                            command=lambda: self.AddPlayerButton.addPlayer(self.id_vars, self.name_vars, self.id_vars2, self.name_vars2),
                            width=15, height=3)

        # Button placement
        sub_btn.place(relx=0.5, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        address_btn.place(relx=0.2, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        add_btn.place(relx=0.8, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)

    # function for starting the game, event=None is for the F5 keybind
    def startGame(self, event=None):
        numRedPlayers = 0
        numGreenPlayers = 0

        # check to make sure that a player is on each team
        for i in range(15):
            if self.redIDList[i] != " ":
                numRedPlayers += 1

            if self.greenIDList[i] != " ":
                numGreenPlayers += 1

        # if both teams don't have at least one player, throw an error
        if numRedPlayers == 0 or numGreenPlayers == 0:
            messagebox.showerror(title="Error", message="You must have at least one player on each team to start a game!")
            return
        # otherwise, start the game
        else:
            self.switch_to_player_action() #go back to display.py and switch to the player action screen