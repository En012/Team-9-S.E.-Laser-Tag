import tkinter as tk
from tkinter import messagebox, font as tkFont
from tkinter import ttk
#from playerentry import PlayerEntryScreen
#from PIL import Image, ImageTk # Should probably be commented out since it is not used at the moment
import os
#import udp stuff for traffic generatorcl
import udpclient
from udpserver import UDPServer

#This class contains all the code for the player action screen
class PlayerActionScreen:

    #default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList, master):

        #Get root, ID, and Name lists from display.py
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList
        self.redScoreList = []
        self.greenScoreList = []
        self.greenTotalScore = 0
        self.redTotalScore = 0
        self.master = master
        self.timerEnd = False

        self.server = UDPServer(message_callback=self.handle_server_message)

    #Countdown timer
    def update_timer(self):
        if self.seconds_left >= 0:
            self.timerEnd = False
            #formatting into minutes/seconds
            minutes, seconds = divmod(self.seconds_left, 60)

            #Update the label with current time
            self.time_remaining_label.config(text=f"{minutes}:{seconds:02d}")
            self.seconds_left -= 1
            #schedule update_timer to run again after 1 second
            self.root.after(1000, self.update_timer)
        else:
            self.timerEnd = True
            self.back_to_entry_screen(self.timerEnd)

    def update_ui(self):
        self.root.update()
        self.green_width1 = self.root.winfo_width() / 3
        if(self.green_width1 != self.green_width):
            self.green_width = self.green_width1
            check = self.green_label_width/self.green_width
            green_place = 1 - check
            self.current_score_label_green.place(relx=green_place, rely=0, anchor="nw")
        self.root.after(200, self.update_ui)

    def display_players(self, red_frame, green_frame):
            initial_score = 0
            # Red team players
            red_length = len(self.redIDList)
            for i in range(red_length):
                player = self.redNameList[i]
                if(player != " "):
                    red_player_name_label = tk.Label(red_frame, text=player, font=('Arial', 12), bg="red", fg="black")
                    red_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                    self.redScoreList.append(initial_score)
                    score = self.redScoreList[i]
                    red_player_score_label = tk.Label(red_frame, text=score, font=('Arial', 12), bg="red", fg="black")
                    red_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
                    self.redTotalScore = self.redTotalScore + score
            #green team players
            green_length = len(self.greenIDList)
            for i in range(green_length):
                player = self.greenNameList[i]
                if(player != " "):
                    green_player_name_label = tk.Label(green_frame, text=player, font=('Arial', 12), bg="green", fg="black")
                    green_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                    self.greenScoreList.append(initial_score)
                    score = self.greenScoreList[i]
                    green_player_score_label = tk.Label(green_frame, text=score, font=('Arial', 12), bg="green", fg="black")
                    green_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
                    self.greenTotalScore = self.greenTotalScore + score
    def switch_to_entry(self):
            from display import Display
            for widget in self.root.winfo_children():
                widget.destroy()  # Clear current widgets
            self.master.switchToPlayerEntry()  # Restart Player Entry Screen
    
    #gets things set up to interact with servertraffic.py
    def start_server_traffic(self):
        
        #start up the udp server to listen from servertraffic.py
        self.server.start_udp_server()

        #send startgame code (202) to servertraffic.py
        udpclient.send_udp_message(f"{202}")

    #this is where playeraction recieves the message from UDPServer and Traffic Gen
    def handle_server_message(self, message):

        #all messages recieved here should be in the form {integer:integer} 
        #first integer is equipment ID of player transmitting (aka the shooter)
        #the second integer is the equipment ID of the player who got hit
        
        print(f"Recieved in playeractionscreen: {message}")

        #UPDATE UI and stuff here

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
        self.black_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="black")

        red_frame.place(relx=0, rely=0, relwidth=.33333333333, relheight=1)
        self.black_frame.place(relx=.33333333333, rely=0, relwidth=.333333333334, relheight=1)
        green_frame.place(relx=.666666667, rely=0, relwidth=.33333333333, relheight=1)
        #-------------------------------------------------Labels--------------------------------------------------------------------------------
        ##Team labels##
        #red team
        red_team_label = tk.Label(red_frame, text='RED TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="red", foreground="black", padx=-1, pady=-1)
        red_team_label.place(relx=.5, rely=.02, anchor="n")

        red_total_score = tk.Label(red_frame, text=f'RED TEAM SCORE: {self.redTotalScore}', font=('Bell Gothic Std Black', 15, "bold"), background="red", foreground="black", padx=-1, pady=-1)
        red_total_score.place(relx=.49, rely=0.99, anchor="s")

        #green team
        green_team_label = tk.Label(green_frame, text='GREEN TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="green", foreground="black", padx=-1, pady=-1)
        green_team_label.place(relx=.5, rely=.02, anchor="n")

        green_total_score = tk.Label(green_frame, text=f'GREEN TEAM SCORE: {self.greenTotalScore}', font=('Bell Gothic Std Black', 15, "bold"), background="green", foreground="black", padx=-1, pady=-1)
        green_total_score.place(relx=.49, rely=0.99, anchor="s")
       #Current score label
        current_score_label_red = tk.Label(red_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="red", foreground="cyan", padx=-1, pady=-1)
        current_score_label_red.place(relx=0, rely=0, anchor="nw")
        self.current_score_label_green = tk.Label(green_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="green", foreground="cyan", padx=-1, pady=-1)
        self.green_label_width = self.current_score_label_green.winfo_reqwidth()
        self.root.update()
        self.green_width = self.root.winfo_width() / 3
        check = self.green_label_width/self.green_width
        green_place = 1 - check
        self.current_score_label_green.place(relx=green_place, rely=0, anchor="nw")


        #Current action label
        current_action_label = tk.Label(self.black_frame, text='Current Game Action', font=('Bell Gothic Std Black', 12, 'bold italic'), background="black", foreground="cyan", padx=-1, pady=-1)
        current_action_label.place(relx=0.5, rely=0, anchor="n")
        #Time remaining
        self.time_label = tk.Label(self.black_frame, text=f"Time Remaining:", font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="white", padx=-1, pady=-1)
        self.time_label.place(relx=0.5, rely=.8, anchor="n")
        self.time_remaining_label = tk.Label(self.black_frame, text=f"{self.seconds_left}", font=('Bell Gothic Std Black', 16, 'bold'), background="black", foreground="white", padx=-1, pady=-1)
        self.time_remaining_label.place(relx=0.5, rely=.85, anchor="n")
        self.display_players(red_frame, green_frame)
        #starting the countdown
        self.update_timer()
        self.update_ui()

        #run neccessary code to interact with the traffic generator once the game beings
        self.start_server_traffic()

    def back_to_entry_screen(self, appear):
         if(appear == True):
            #send game over code to the traffic generator three times to stop the game
            [udpclient.send_udp_message(f"{221}") for _ in range(3)]

            #make back_button appear
            back_button = tk.Button(self.black_frame, text="End Game", command=self.switch_to_entry, font=("Arial", 12), bg="white")
            back_button.place(relx=0.5, rely=0.9, anchor="n")