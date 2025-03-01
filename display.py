import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
import udpclient
import udpserver
import database

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
        
        #initalize self.image and open the splash screen
        self.img = Image.open("images/logo.jpg")
        self.splash_screen()

        #switch to player entry screen after 3000 milliseconds
        self.root.after(3000, self.switchToPlayerEntry)
        

    #code for the splash screen
    def splash_screen(self):
        self.img = self.img.resize((self.width, self.height), Image.LANCZOS)
        self.img = ImageTk.PhotoImage(self.img)
        label = tk.Label(self.root, image=self.img, bg="black")    
        label.pack()
        self.root.geometry(f"{self.width}x{self.height}")
    
    #switch to playerEntryScreen
    def switchToPlayerEntry(self):
        self.player_entry_screen()

    #code for the player entry screen
    def player_entry_screen(self):
        #setting name of window
        self.root.title("Photon")
        self.root.minsize(800,600)

        #setting the sizes
        title_relheight = 0.1  # 10% of the window is for title
        button_relheight = 0.1  # 10% for the buttons at the bottom
        row_count = 15
        row_relheight = (1 - title_relheight - button_relheight) / row_count

        #Set background colors
        red_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="red")
        green_frame = tk.Frame(self.root, bd=0, highlightthickness=0, background="green")

        #Title Placement
        titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
        title = tk.Label(self.root, font=titlefont, text="Edit Current Game", background="black", fg="white")
        title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")

        #Place background frames
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
        id_label2.place(relx=0.658, rely=0.12, anchor="e")

        name_label2 = tk.Label(self.root, text='Name', font=('calibre', 12, 'bold'), background="green")
        name_label2.place(relx=0.848, rely=0.12, anchor="e")
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
        sub_btn = tk.Button(self.root, text='Start Game', command=lambda: self.startGame(), width=15, height=3)

        # button to activate the change address function
        #address_btn = tk.Button(self.root, text="Change Address", command=udpfunctions.change_udp_client_inter, width=15, height=3)

        # button for adding a player to the game
        add_btn = tk.Button(self.root, text='Add Player',
                            command=lambda: self.addPlayer(),
                            width=15, height=3)

        # Button placement
        sub_btn.place(relx=0.5, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        #address_btn.place(relx=0.2, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)
        add_btn.place(relx=0.8, rely=0.96, anchor="center", relwidth=0.2, relheight=0.05)

    #function for starting the game, to be fully implemented later
    def startGame(self):
        numRedPlayers = 0
        numGreenPlayers = 0

        #check to make sure that a player is on each team
        for i in range(15):
            if self.redIDList[i] != "None":
                numRedPlayers += 1
            
            if self.greenIDList[i] != "None":
                numGreenPlayers += 1

        #if both teams dont have at least one player, throw an error
        if numRedPlayers == 0 or numGreenPlayers == 0:
            messagebox.showerror(title="Error", message="You must have at least one player on each team to start a game!")
            return
        #otherwise, start the game
        else:
            messagebox.showinfo(title="Notification", message="Start will be implemented in a future sprint!")

    # called when the addPlayer button is pressed
    def addPlayer(self):
        # Get Id from the idPopUp Window
        playerId = self.idPopUp()

        # If enteredId = None, then getting the id failed so return with no changes
        if playerId == "None":
            return

        # Check if player with id is already in the game
        if playerId in self.redIDList or playerId in self.greenIDList:
            messagebox.showerror(title="Error", message=f"Player with ID: {playerId} is already in the game")
            return

        # STEP 2: check against the database to see if the id is there
        inDatabase = database.checkInDatabase(playerId)

        # If playerID is not there, ask for a codename
        if not inDatabase:
            playerCodeName = self.codeNamePopUp()

            # If Codename = None, then getting the codename failed, so return
            if playerCodeName == "None":
                return
            # Otherwise, add the playerID and codename as an entry in the database
            else:
                database.addPlayer(playerId, playerCodeName)
        else:
            # If playerID is there, get the codename
            playerCodeName = database.getCodeName(playerId)

            # If retrieving playerID from the database failed, return
            if playerCodeName is None:
                return

        # STEP 4: Get equipment ID from the player
        playerEquipmentId = self.equipmentPopUp()

        # If playerEquipmentId = None, then getting the equipment ID failed so return with no changes
        if playerEquipmentId == "None":
            return

        # This logs the message being sent to the server, essential for debugging
        udpclient.send_udp_message(f"{playerEquipmentId}")

        # STEP 5: Add the player info to the player entry screen
        # If playerEquipmentId is odd, add the player to red team
        if int(playerEquipmentId) % 2 == 1:
            # Make sure that red team isn't full before adding the player
            if self.redIDList[14] != "None":
                messagebox.showerror(title="Error", message="Red Team is full!")
                return
            # Go through the list of id's and place the player in the next available spot
            for i in range(15):
                if self.redIDList[i] == "None":
                    self.redIDList[i] = playerId
                    self.redNameList[i] = playerCodeName

                    self.id_vars[i].set(self.redIDList[i])
                    self.name_vars[i].set(self.redNameList[i])
                    break
        else:
            # Make sure that green team isn't full before adding the player
            if self.greenIDList[14] != "None":
                messagebox.showerror(title="Error", message="Green Team is full!")
                return
            # Go through the list of id's and place the player in the next available spot
            for i in range(15):
                if self.greenIDList[i] == "None":
                    self.greenIDList[i] = playerId
                    self.greenNameList[i] = playerCodeName

                    self.id_vars2[i].set(self.greenIDList[i])
                    self.name_vars2[i].set(self.greenNameList[i])
                    break

    # code for the idPopUp menu
    def idPopUp(self):
        player_id = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")  # Set window size

        # Center the popup window
        popup.update_idletasks()  # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 300
        window_height = 150

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Label for the player ID input
        tk.Label(popup, text="Enter Player ID:", font=("Arial", 12)).pack(pady=10)

        # Entry field for player ID
        player_id_var = tk.StringVar()
        player_id_entry = tk.Entry(popup, textvariable=player_id_var, font=("Arial", 12))
        player_id_entry.pack(pady=5)

        # Function to handle submission
        def submit_id():
            nonlocal player_id
            player_id = player_id_var.get()
            if not player_id.isdigit():
                messagebox.showerror(title="Error", message="ID's should only consist of digits. Please reenter the ID")
                player_id = "None"
            else:
                popup.destroy()  # Close the popup

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submit_id, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root)  # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return player_id

    # code for the namePopUp menu
    def codeNamePopUp(self):
        codeName = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")  # Set window size

        # Center the popup window
        popup.update_idletasks()  # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 300
        window_height = 150

        # Center the popup window
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Label for the codename input
        tk.Label(popup, text=f"ID is new. Please enter a codename:", font=("Arial", 12)).pack(pady=10)

        # Entry field for codename
        codeName_var = tk.StringVar()
        codeName_entry = tk.Entry(popup, textvariable=codeName_var, font=("Arial", 12))
        codeName_entry.pack(pady=5)

        # Function to handle submission
        def submitCodename():
            nonlocal codeName
            codeName = codeName_var.get()
            popup.destroy()  # Close the popup

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submitCodename, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root)  # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return codeName

    # code for the equipmentPopUp menu
    def equipmentPopUp(self):
        equipmentId = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")  # Set window size

        # Center the popup window
        popup.update_idletasks()  # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 300
        window_height = 150

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Label for the equipment ID input
        tk.Label(popup, text="Enter Equipment ID:", font=("Arial", 12)).pack(pady=10)

        # Entry field for equipment ID
        equipment_var = tk.StringVar()
        equipment_entry = tk.Entry(popup, textvariable=equipment_var, font=("Arial", 12))
        equipment_entry.pack(pady=5)

        # Function to handle submission
        def submit_id():
            nonlocal equipmentId
            equipmentId = equipment_var.get()

            # Check to make sure that the user only entered numbers into the ID field
            if not equipmentId.isdigit():
                messagebox.showerror(title="Error", message="ID's should only consist of digits. Please reenter the ID")
                equipmentId = "None"
            else:
                popup.destroy()  # Close the popup

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submit_id, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root)  # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return equipmentId


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
