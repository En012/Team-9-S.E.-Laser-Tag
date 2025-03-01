import tkinter as tk
from tkinter import messagebox, font as tkFont

class PlayerActionScreen:

    #default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList):
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList
    
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
        
        