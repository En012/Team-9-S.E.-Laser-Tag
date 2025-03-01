import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont

from playerentry import PlayerEntryScreen
from playeraction import PlayerActionScreen

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

        #get screen self.width and self.height
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()

        #Initialize the playerentryscreen
        self.PlayerEntryScreen = PlayerEntryScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList, self.switchToPlayerAction) 

        #Initialize the playeractionscreen
        self.PlayerActionScreen = PlayerActionScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList)
        
        #run the splash screen
        self.splash_screen()

        #switch to player entry screen after 3000 milliseconds
        self.root.after(3000, self.switchToPlayerEntry)
        

    #code for the splash screen
    def splash_screen(self):
        #initalize self.image and open the splash screen
        self.img = Image.open("images/logo.jpg")
        self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.root, image=self.img, bg="black")    
        label.pack()
        self.root.geometry(f"{self.width}x{self.height}")
    
    #switch to playerEntryScreen
    def switchToPlayerEntry(self):
        self.PlayerEntryScreen.run() #show the playerentry screen

    #switch to playerActionScreen
    def switchToPlayerAction(self):
        # Reinitialize the display when switching back
        for widget in self.root.winfo_children():
            widget.destroy()  # Clear current widgets
        self.PlayerActionScreen.run() # Show the playeraction screen

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