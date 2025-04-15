import tkinter as tk
from tkinter import messagebox, font as tkFont
from tkinter import ttk
#from playerentry import PlayerEntryScreen
#from PIL import Image, ImageTk # Should probably be commented out since it is not used at the moment
import os
#from actions import Action
#import udp stuff for traffic generatorcl
import udpclient

#This class contains all the code for the player action screen
class PlayerActionScreen:

    #default constructor
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList, master, server):

        #Get root, ID, and Name lists from display.py
        self.root = root

        #IDs
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList
        
        #scores
        self.redScoreList = []
        self.greenScoreList = []
        self.greenTotalScore = 0
        self.redTotalScore = 0
        self.master = master
        self.temp_green = 0
        self.temp_red = 0
        self.timerEnd = False
        self.redHigh = False
        self.greenHigh = False
        self.killfeed_text = ""
        
        #used to prevent reading info from traffic gen once the game is over
        self.endGame = False

        #server stuff
        self.server = server
        self.server.message_callback = self.handle_server_message
        #Testing to reduce time with one variable
        self.Test = True

    #Countdown timer
    def update_timer(self):
        if self.seconds_left >= 0:
            self.timerEnd = False
            if(self.redTotalScore != self.temp_red or self.greenTotalScore != self.temp_green):
                self.temp_green = self.greenTotalScore
                self.temp_red = self.redTotalScore
                self.red_total_score.config(text=f'RED TEAM SCORE: {self.redTotalScore}')
                self.green_total_score.config(text=f'GREEN TEAM SCORE: {self.greenTotalScore}')
                self.flash_high(self.redTotalScore, self.greenTotalScore)
            if(self.greenHigh):
                if self.seconds_left % 2:
                    self.red_total_score.config(foreground='black')
                    self.green_total_score.config(foreground='black')
                else:
                    self.red_total_score.config(foreground='black')
                    self.green_total_score.config(foreground='blue')
            elif(self.redHigh):
                if self.seconds_left % 2:
                    self.red_total_score.config(foreground='black')
                    self.green_total_score.config(foreground='black')
                else:
                    self.red_total_score.config(foreground='blue')
                    self.green_total_score.config(foreground='black')
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
            #red team labels
            self.redScoreLabels = []
            self.redNameLabels = []

            #green team labels 
            self.greenScoreLabels = []
            self.greenNameLabels = []

            initial_score = 0
            # Red team players
            red_length = len(self.redIDList)
            for i in range(red_length):
                player = self.redNameList[i]
                if(player != " "):
                    red_player_name_label = tk.Label(red_frame, text=player, font=('Arial', 12), bg="red", fg="black")
                    red_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                    #pusing the name labels into this array to modify elsewhere
                    self.redNameLabels.append(red_player_name_label)
                    self.redScoreList.append(initial_score)
                    score = self.redScoreList[i]
                    red_player_score_label = tk.Label(red_frame, text=score, font=('Arial', 12), bg="red", fg="black")
                    red_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
                    #pusing the score labels into this array to modify elsewhere
                    self.redScoreLabels.append(red_player_score_label)
                    #gets update elsewhere so it can stay zero
                    self.redTotalScore = 0
            #green team players
            green_length = len(self.greenIDList)
            for i in range(green_length):
                player = self.greenNameList[i]
                if(player != " "):
                    green_player_name_label = tk.Label(green_frame, text=player, font=('Arial', 12), bg="green", fg="black")
                    green_player_name_label.place(relx=0.35, rely=.12 + (i * 0.05), anchor="w")
                    #green name labels into this array to be modified elsewhere
                    self.greenNameLabels.append(green_player_name_label)
                    self.greenScoreList.append(initial_score)
                    score = self.greenScoreList[i]
                    green_player_score_label = tk.Label(green_frame, text=score, font=('Arial', 12), bg="green", fg="black")
                    green_player_score_label.place(relx=0.6, rely=.12 + (i * 0.05), anchor="w")
                    #storing the green score labels to be modified elsewhere
                    self.greenScoreLabels.append(green_player_score_label)
                    #gets updated elsewhere so it can remain zero
                    self.greenTotalScore = 0
    def switch_to_entry(self):
            from display import Display
            for widget in self.root.winfo_children():
                widget.destroy()  # Clear current widgets
            self.master.switchToPlayerEntry()  # Restart Player Entry Screen
    
    #gets things set up to interact with servertraffic.py
    def start_server_traffic(self):
        #send startgame code (202) to servertraffic.py
        udpclient.send_udp_message(f"{202}")

    #this is where playeraction recieves the message from UDPServer and Traffic Gen
    def handle_server_message(self, message):

        #all messages recieved here should be in the form {integer:integer} 
        #first integer is equipment ID of player transmitting (aka the shooter)
        #the second integer is the equipment ID of the player who got hit

        #dont allow the score to change at all after the game is over
        if self.endGame:
            return

        #remember green base = 43, red base = 53 
        try:
            shooter_id, target_id = message.split(":")
        except ValueError:
            print("Invalid message format")
            return
        
        # Convert to string (to make sure shooter/target are strings)
        shooter_id, target_id = map(str, message.split(":"))

        # Create string-converted versions of the ID lists
        red_ids = list(map(str, self.redIDList))
        green_ids = list(map(str, self.greenIDList))

        # Base scoring logic
        if target_id == "43" and shooter_id in red_ids:
            # Red player hit green base
            index = red_ids.index(shooter_id)
            self.redScoreList[index] += 100
            self.redScoreLabels[index].config(text=str(self.redScoreList[index]))
            self.redTotalScore += 100
            name = self.redNameList[index]
            #name change logic
            if not name.startswith("[B] "):
                self.redNameLabels[index].config(text=f"[B] {name}", font = ("Times", 12, "bold italic"), fg = "gold")
            self.killfeed_text = (f"Green Base was hit by {self.redNameList[index]}")
            self.updateEvents(self.killfeed_text)
            return

        if target_id == "53" and shooter_id in green_ids:
            # Green player hit red base
            index = green_ids.index(shooter_id)
            self.greenScoreList[index] += 100
            self.greenScoreLabels[index].config(text=str(self.greenScoreList[index]))
            self.greenTotalScore += 100
            name = self.greenNameList[index]
            #name change logic
            if not name.startswith("[B] "):
                self.greenNameLabels[index].config(text=f"[B] {name}", font = ("Times", 12, "bold italic"), fg = "gold")
            self.killfeed_text = (f"Red Base was hit by {self.greenNameList[index]}")
            self.updateEvents(self.killfeed_text)
            return

        # Identify shooter team and index
        shooter_team = None
        target_team = None

        if shooter_id in red_ids:
            shooter_team = 'red'
            shooter_index = red_ids.index(shooter_id)
        elif shooter_id in green_ids:
            shooter_team = 'green'
            shooter_index = green_ids.index(shooter_id)
        else:
            print("Shooter ID not found.")
            return

        if target_id in red_ids:
            target_team = 'red'
        elif target_id in green_ids:
            target_team = 'green'
        else:
            print("Target ID not found.")
            return

        # Scoring logic
        if shooter_team == target_team:
            # Friendly fire: -10
            if shooter_team == 'red' and shooter_index < len(self.redScoreList):
                target_index = red_ids.index(target_id)
                self.redScoreList[shooter_index] -= 10
                self.redScoreLabels[shooter_index].config(text=str(self.redScoreList[shooter_index]))
                self.redTotalScore -= 10
                self.killfeed_text = (f"{self.redNameList[shooter_index]} hit their own teammate {self.redNameList[target_index]}!")
            elif shooter_team == 'green' and shooter_index < len(self.greenScoreList):
                target_index = green_ids.index(target_id)
                self.greenScoreList[shooter_index] -= 10
                self.greenScoreLabels[shooter_index].config(text=str(self.greenScoreList[shooter_index]))
                self.greenTotalScore -= 10
                self.killfeed_text = (f"{self.greenNameList[shooter_index]} hit their own teammate {self.greenNameList[target_index]}!")
        else:
            # Enemy hit: +10
            if shooter_team == 'red' and shooter_index < len(self.redScoreList):
                target_index = green_ids.index(target_id)
                self.redScoreList[shooter_index] += 10
                self.redScoreLabels[shooter_index].config(text=str(self.redScoreList[shooter_index]))
                self.redTotalScore += 10
                self.killfeed_text = (f"{self.redNameList[shooter_index]} hit {self.greenNameList[target_index]}")
            elif shooter_team == 'green' and shooter_index < len(self.greenScoreList):
                target_index = red_ids.index(target_id)
                self.greenScoreList[shooter_index] += 10
                self.greenScoreLabels[shooter_index].config(text=str(self.greenScoreList[shooter_index]))
                self.greenTotalScore += 10
                self.killfeed_text = (f"{self.greenNameList[shooter_index]} hit {self.redNameList[target_index]}")

        # Update total score labels
        self.red_total_score.config(text=f'RED TEAM SCORE: {self.redTotalScore}')
        self.green_total_score.config(text=f'GREEN TEAM SCORE: {self.greenTotalScore}')
        self.updateEvents(self.killfeed_text)

    def run(self):
        #make sure the program will read scores from traffic gen again
        self.endGame = False

        #change this value to change gameplay time
        if self.Test == True:
            self.seconds_left = 30
        else:
            self.seconds_left = 360 
        
        #clear scores from the previous game
        self.clearScores()

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
        self.red_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="red")
        self.green_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="green")
        self.black_frame = tk.Frame(self.root, bd=1, highlightthickness=1, highlightbackground="black", background="black")

        self.red_frame.place(relx=0, rely=0, relwidth=.33333333333, relheight=1)
        self.black_frame.place(relx=.33333333333, rely=0, relwidth=.333333333334, relheight=1)
        self.green_frame.place(relx=.666666667, rely=0, relwidth=.33333333333, relheight=1)
        #-------------------------------------------------Labels--------------------------------------------------------------------------------
        ##Team labels##
        #red team
        red_team_label = tk.Label(self.red_frame, text='RED TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="red", foreground="black", padx=-1, pady=-1)
        red_team_label.place(relx=.5, rely=.02, anchor="n")
        print(self.redTotalScore)
        self.red_total_score = tk.Label(self.red_frame, text=f'RED TEAM SCORE: {self.redTotalScore}', font=('Bell Gothic Std Black', 15, "bold"), background="red", foreground="black", padx=-1, pady=-1)
        self.red_total_score.place(relx=.49, rely=0.99, anchor="s")

        #green team
        green_team_label = tk.Label(self.green_frame, text='GREEN TEAM', font=('Bell Gothic Std Black', 27, 'bold'), background="green", foreground="black", padx=-1, pady=-1)
        green_team_label.place(relx=.5, rely=.02, anchor="n")
        print(self.greenTotalScore)
        self.green_total_score = tk.Label(self.green_frame, text=f'GREEN TEAM SCORE: {self.greenTotalScore}', font=('Bell Gothic Std Black', 15, "bold"), background="green", foreground="black", padx=-1, pady=-1)
        self.green_total_score.place(relx=.49, rely=0.99, anchor="s")
       #Current score label
        current_score_label_red = tk.Label(self.red_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="red", foreground="cyan", padx=-1, pady=-1)
        current_score_label_red.place(relx=0, rely=0, anchor="nw")
        self.current_score_label_green = tk.Label(self.green_frame, text='Current Scores', font=('Bell Gothic Std Black', 12, 'bold italic'), background="green", foreground="cyan", padx=-1, pady=-1)
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
        self.flash_high(self.redTotalScore, self.greenTotalScore)
        #starting the countdown
        self.display_players(self.red_frame, self.green_frame)
        #event test showcase
        self.showcaseactionEvents()
        self.update_timer()
        self.update_ui()

        #run neccessary code to interact with the traffic generator once the game beings
        self.start_server_traffic()

    def flash_high(self, red_score, green_score):
        if(red_score > green_score):
            self.greenHigh = False
            self.redHigh = True
        elif(green_score > red_score):
            self.greenHigh = True
            self.redHigh = False

    def back_to_entry_screen(self, appear):
         if(appear == True):
            #send game over code to the traffic generator three times to stop the game
            [udpclient.send_udp_message(f"{221}") for _ in range(3)]

            #make sure no other hits are registered from the traffic gen
            self.endGame = True

            #make back_button appear
            back_button = tk.Button(self.black_frame, text="End Game", command=self.switch_to_entry, font=("Arial", 12), bg="white")
            back_button.place(relx=0.5, rely=0.9, anchor="n")

    #resets all score values
    def clearScores(self):

        self.redScoreList.clear()
        self.greenScoreList.clear()

        self.redTotalScore = 0
        self.greenTotalScore = 0
    
    #Event Showcase
    def showcaseactionEvents(self):
        # Showcase box
        eventFrame = tk.Frame(self.root, highlightbackground= "cyan", highlightthickness=2, bg="black", width=350, height=580)  # Keep the current max height
        eventFrame.place(relx=0.5, rely=0.4, anchor="center", relheight=0.63, relwidth=0.33)  # Lowered placement closer to "Remaining Time" / relheight and relwidth scale to window size

        # Stores events in here
        self.eventStorage = []

        # Create 15 labels for events
        for i in range(15):
            events = tk.Label(eventFrame, text="", font=('calibre', 12), bg="black", fg="cyan", width=40)
            events.place(relx=0.5, rely=0.049 + i * 0.065, anchor="center")  # Adjusted spacing to fit 15 labels
            self.eventStorage.append(events)
    
    #Event Updater (changes text within the labels to go upwards)
    def updateEvents(self, yourText):
        for i in range(len(self.eventStorage) - 1):
            placeholderText = self.eventStorage[i + 1]['text']
            self.eventStorage[i].config(text = placeholderText)
        self.eventStorage[-1].config(text = yourText)