import tkinter as tk
from tkinter import messagebox, font as tkFont
from PIL import Image, ImageTk
import os

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
        #All code for PlayerEntryScreen can be found in playerentry.py
        self.PlayerEntryScreen = PlayerEntryScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList, self.switchToPlayerAction) 

        #Initialize the playeractionscreen
        #All code for PlayerActionScreen can be found in playeraction.py
        self.PlayerActionScreen = PlayerActionScreen(self.root, self.redIDList, self.redNameList, self.greenIDList, self.greenNameList)
        
        #display the splash screen
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
        #adfa