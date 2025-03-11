import tkinter as tk
from tkinter import messagebox, font as tkFont
from tkinter import ttk
#from PIL import Image, ImageTk
import os

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
        self.redScoreList = []
        self.greenScoreList = []

    #Countdown timer
    def update_timer(self):
        if self.seconds_left >= 0:
            #formatting into minutes/seconds
            minutes, seconds = divmod(self.seconds_left, 60)

            #Update the label with current time
            self.time_remaining_label.config(text=f"{minutes}:{seconds:02d}")
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
    def display_players(self, red_frame, green_frame):
            initial_score = 0
            # Red team players
            red_length = len(self.redIDList)
            for i in range(red_length):
                player = self.redNameList[i]
                red_player_name_label = tk.Label(red_frame, text=player, font=('Arial', 12), bg="red", fg="black")
                red_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                self.redScoreList.append(initial_score)
                score = self.redScoreList[i]
                red_player_score_label = tk.Label(red_frame, text=score, font=('Arial', 12), bg="red", fg="black")
                red_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
            #green team players
            green_length = len(self.greenIDList)
            for i in range(green_length):
                player = self.greenNameList[i]
                green_player_name_label = tk.Label(green_frame, text=player, font=('Arial', 12), bg="green", fg="black")
                green_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                self.greenScoreList.append(initial_score)
                score = self.greenScoreList[i]
                green_player_score_label = tk.Label(green_frame, text=score, font=('Arial', 12), bg="green", fg="black")
                green_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
    
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
        #Keeping old in case we need to go back
        """
        #black background for score keeping (referenced from his github)
        #back_frame= tk.Frame(self.root, bd=1, highlightthickness=5, highlightbackground="grey", background="black")
        #back_frame.place(relx=0.15, rely=.15, relwidth=0.7, relheight=0.75)

        #blue frame where gameplay is tracked
        #game_frame= tk.Frame(self.root, bd=1, highlightthickness=5, highlightbackground="grey", background="blue")
        #game_frame.place(relx=0.15, rely=.4, relwidth=0.7, relheight=0.42)
        """
        red_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="red")
        green_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="green")
        black_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="black")

        red_frame.place(relx=0, rely=0, relwidth=.33333333333, relheight=1)
        black_frame.place(relx=.33333333333, rely=0, relwidth=.333333333334, relheight=1)
        green_frame.place(relx=.666666667, rely=0, relwidth=.33333333333, relheight=1)
        #-------------------------------------------------Labels--------------------------------------------------------------------------------
        ##Team labels##
        #red team
        red_team_label = tk.Label(red_frame, text='RED TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="red", foreground="black", padx=-1, pady=-1)
        red_team_label.place(relx=.5, rely=.02, anchor="n")

        #green team
        green_team_label = tk.Label(green_frame, text='GREEN TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="green", foreground="black", padx=-1, pady=-1)
        green_team_label.place(relx=.5, rely=.02, anchor="n")
        """
        #Current score label
        current_score_label = tk.Label(main_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="black", foreground="cyan", padx=-1, pady=-1)
        current_score_label.place(relx=1, rely=0, anchor="ne")

        #Current action label
        current_action_label = tk.Label(main_frame, text='Current Game Action', font=('Bell Gothic Std Black', 12, 'bold italic'), background="blue", foreground="cyan", padx=-1, pady=-1)
        current_action_label.place(relx=1, rely=0, anchor="ne")"
        """
        #Time remaining
        self.time_label = tk.Label(black_frame, text=f"Time Remaining:", font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="white", padx=-1, pady=-1)
        self.time_label.place(relx=0.5, rely=.8, anchor="n")
        self.time_remaining_label = tk.Label(black_frame, text=f"{self.seconds_left}", font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="white", padx=-1, pady=-1)
        self.time_remaining_label.place(relx=0.5, rely=.85, anchor="n")
        self.display_players(red_frame, green_frame)
        #starting the countdown
        self.update_timer()
#test
if __name__ == "__main__":
    root = tk.Tk()
    # Example data, this would be passed from the display.py
    redIDList = ["1", "2"]
    greenIDList = ["3", "4"]
    redNameList = ["Red1", "Red2"]
    greenNameList = ["Green1", "Green2"]

    screen = PlayerActionScreen(root, redIDList, greenIDList, redNameList, greenNameList)
    screen.run()
    root.mainloop()