import tkinter as tk
from tkinter import messagebox, font as tkFont
from PIL import Image, ImageTk
import os

#This class contains all the code for the player action screen
class PlayerActionScreen:

    #default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList):
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList


    #This may be broken now, I'm not sure...
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
    
    
    #CODE FOR PLAYERACTION SCREEN GOES HERE!!!
    def run(self):

        #PLACEHOLDER CODE, CHANGE IT!
        
        # setting name of window
        self.root.title("Photon")
        self.root.minsize(800, 600)

        # Set title font
        title_font = tkFont.Font(family='Calibri', size=24, weight='bold')
        title = tk.Label(self.root, text="Player Action Screen", font=title_font, bg="white", fg="black")
        title.place(relx=0.5, rely=0.1, anchor="center")

        #whatever goes here, idk, thats for Trevor and Eduardo to decide
        #but whatever it is... it better be cool
        