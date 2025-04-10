import tkinter as tk
from tkinter import messagebox, font as tkFont
from PIL import Image, ImageTk
import os

from playerentry import PlayerEntryScreen
from playeraction import PlayerActionScreen

class Display:

    #default constructor
    def __init__(self, server):

        #setup default values for name and ID list for red and green team
        self.redNameList = [" "] * 15
        self.redIDList = [" "] * 15
        self.greenNameList = [" "] * 15
        self.greenIDList = [" "] * 15

        #setup tkinter GUI elements
        self.root = tk.Tk()
        self.root.title("Loading...")
        self.root.configure(bg="black")

        #initilizing server
        self.server = server

        #get screen self.width and self.height
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        #Initialize the playerentryscreen
        #All code for PlayerEntryScreen can be found in playerentry.py
        self.PlayerEntryScreen = PlayerEntryScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList, self) 

        #Initialize the playeractionscreen
        #All code for PlayerActionScreen can be found in playeraction.py
        self.PlayerActionScreen = PlayerActionScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList, self, self.server)
        
        #binding F10 key to call clear button
        self.root.bind("<F12>", self.clear_entry)

        #binding F5 key to call startgame under PlayerEntryScreen
        self.root.bind("<F5>", self.PlayerEntryScreen.startGame)

        #display the splash screen
        self.splash_screen()

        #switch to player entry screen after 3000 milliseconds (Unless Testing)
        if self.PlayerActionScreen.Test == True:
            self.switchToPlayerEntry()
        else:
            self.root.after(3000, self.switchToPlayerEntry)

    #code for clear button
    def clear_entry(self, event=None):
        print("Entries Cleared")
        for i in range(15):
            #invidually clearing the lists values.
            self.redIDList[i] = " "
            self.redNameList[i] = " "
            self.greenIDList[i] = " "
            self.greenNameList[i] = " "

            #clearing the list graphically from the GUI
            self.PlayerEntryScreen.id_vars[i].set("")
            self.PlayerEntryScreen.name_vars[i].set("")
            self.PlayerEntryScreen.id_vars2[i].set("")
            self.PlayerEntryScreen.name_vars2[i].set("")

    #code for the splash screen
    def splash_screen(self):
        #initalize self.image and open the splash screen
        self.img = Image.open("images/logo.jpg")
        self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.root, image=self.img, bg="black")    
        label.pack()
        self.root.geometry(f"{self.width}x{self.height}")
        
    #code for the countdown timer screen
    def countdown_timer_screen(self, seconds):
        if seconds >= 0:
            #print(f"{seconds}\n")
            img_path = os.path.expanduser(f"images/{seconds}.jpg")
            self.img = Image.open(img_path)
            self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
            self.img = ImageTk.PhotoImage(self.img)
            if hasattr(self, "label") and self.label.winfo_exists():
                self.label.config(image=self.img)
            else:
                self.label = tk.Label(self.root, image=self.img, bg="black")
                self.label.pack()
            self.root.after(1000, self.countdown_timer_screen, seconds - 1)
        else:
            self.PlayerActionScreen.run() # Show the player action screen
    
    #switch to playerEntryScreen
    def switchToPlayerEntry(self):
        self.PlayerEntryScreen.run() #show the playerentry screen

    #switch to playerActionScreen (Ed: Possible name change due to how its modified now?)
    def switchToPlayerAction(self):
        # Reinitialize the display when switching back
        if self.PlayerActionScreen.Test == True:
            self.PlayerActionScreen.run()
        else:
            for widget in self.root.winfo_children():
                widget.destroy()  # Clear current widgets
            self.countdown_timer_screen(30) # Show the playeraction screen
        