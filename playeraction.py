import tkinter as tk
from tkinter import messagebox, font as tkFont
from tkinter import ttk
from PIL import Image, ImageTk
import os
import time

#This class contains all the code for the player action screen
class PlayerActionScreen:

    #default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList):

        #Get root, ID, and Name lists from display.py
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList

    #Countdown timer
    def update_timer(self):
        if self.seconds_left >= 0:
            #formatting into minutes/seconds
            minutes, seconds = divmod(self.seconds_left, 60)

            #Update the label with current time
            self.time_label.config(text=f"Time Remaining: {minutes}:{seconds:02d}")
            self.seconds_left -= 1
            #schedule update_timer to run again after 1 second
            self.root.after(1000, self.update_timer)
        else:
            self.player_entry_screen()


    #This may be broken now, I'm not sure...
    # countdown timer function
    # def timer(self, seconds=30):
    #     if seconds >= 0:
    #         print(f"{seconds}\n")
    #         img_path = os.path.expanduser(f"images/{seconds}.tif")
    #         self.img = Image.open(img_path)
    #         self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
    #         self.img = ImageTk.PhotoImage(self.img)
    #         label = tk.Label(self.root, image=self.img, bg="black")
    #         label.pack()
    #         self.root.after(1000, self.timer, seconds - 1)
    #     else:
    #         self.player_entry_screen()
    
    
    #CODE FOR PLAYERACTION SCREEN GOES HERE!!!
    def run(self):

        #change this value to change gameplay time
        self.seconds_left = 360
        
        # setting name of window
        self.root.title("Photon")
        self.root.minsize(800, 600)
        self.root.configure(bg="black")

        #set title font
        title_font = tkFont.Font(family='Calibri', size=24, weight='bold')
        title = tk.Label(self.root, text="Player Action Screen", font=title_font, bg="black", fg="white")
        title.place(relx=0.5, rely=0.05, anchor="center")
        
        #--------------------------------------------------Frames-------------------------------------------------------------------------------
        #black background for score keeping (referenced from his github)
        back_frame= tk.Frame(self.root, bd=1, highlightthickness=5, highlightbackground="grey", background="black")
        back_frame.place(relx=0.15, rely=.15, relwidth=0.7, relheight=0.75)

        #blue frame where gameplay is tracked
        game_frame= tk.Frame(self.root, bd=1, highlightthickness=5, highlightbackground="grey", background="blue")
        game_frame.place(relx=0.15, rely=.4, relwidth=0.7, relheight=0.42)


        #-------------------------------------------------Labels--------------------------------------------------------------------------------
        #Team labels
        #red team
        red_team_label = tk.Label(back_frame, text='RED TEAM', font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="red", padx=-1, pady=-1)
        red_team_label.place(relx=.35, rely=.02, anchor="n")

        #green team
        green_team_label = tk.Label(back_frame, text='GREEN TEAM', font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="green", padx=-1, pady=-1)
        green_team_label.place(relx=.625, rely=.02, anchor="n")

        #Current score label
        current_score_label = tk.Label(back_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="black", foreground="cyan", padx=-1, pady=-1)
        current_score_label.place(relx=1, rely=0, anchor="ne")

        #Current action label
        current_action_label = tk.Label(game_frame, text='Current Game Action', font=('Bell Gothic Std Black', 12, 'bold italic'), background="blue", foreground="cyan", padx=-1, pady=-1)
        current_action_label.place(relx=1, rely=0, anchor="ne")

        #Time remaining (replace placehold with incremental time value)
        self.time_label = tk.Label(back_frame, text=f"Time Remaining: {self.seconds_left}", font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="white", padx=-1, pady=-1)
        self.time_label.place(relx=0.99, rely=.98, anchor="se")

        #starting the countdown
        self.update_timer()