import tkinter as tk
from tkinter import messagebox

import udpclient
import database

#Handles all the code that is run when the AddPlayerButton is pressed
#DOES NOT handle displaying the button to the screen
class AddPlayerButton:

    #default constructor get root, IDList, and NameList
    def __init__(self, root, redIDList, greenIDList, redNameList, greenNameList):
        self.root = root
        self.redIDList = redIDList
        self.greenIDList = greenIDList
        self.redNameList = redNameList
        self.greenNameList = greenNameList

    #handles the process for adding a player to the game
    def addPlayer(self, id_vars, name_vars, id_vars2, name_vars2):
        
        #call idPopup to get ID from the player
        playerId = self.idPopUp()

        #if playerId == None, getting the id failed, so return
        if playerId == "None":
            return

        print(self.redIDList)
        #check to see if player with the same id is already in the game
        if playerId in self.redIDList or playerId in self.greenIDList:
            messagebox.showerror(title="Error", message=f"Player with ID: {playerId} is already in the game")
            return

        #check to see if the player is already in the database
        inDatabase = database.checkInDatabase(playerId)

        #if player is not already in the database, get the players codename
        if not inDatabase:
            playerCodeName = self.codeNamePopUp()

            #if playerCodeName == None, then getting the codename failed, so return
            if playerCodeName == "None":
                return
            #otherwise, add the playerID and playerCodeName to the database
            else:
                database.addPlayer(playerId, playerCodeName)
        #if player is already in teh database, get there codename
        else:
            playerCodeName = database.getCodeName(playerId)

            #if retrieving the codename from the database fails, then return
            if playerCodeName is None:
                return

        #Get the equipment ID from the user
        playerEquipmentId = self.equipmentPopUp()

        #if equipmentID == "None", getting the equipment ID failed, so return
        if playerEquipmentId == "None":
            return
        
        #send the equipmentID to the UDP server
        udpclient.send_udp_message(f"{playerEquipmentId}")

        #Finally, add the player to the playerentryscreen
        if int(playerEquipmentId) % 2 == 1:
            if self.redIDList[14] != " ":
                messagebox.showerror(title="Error", message="Red Team is full!")
                return
            for i in range(15):
                if self.redIDList[i] == " ":
                    self.redIDList[i] = playerId
                    self.redNameList[i] = playerCodeName

                    id_vars[i].set(self.redIDList[i])
                    name_vars[i].set(self.redNameList[i])
                    break
        else:
            if self.greenIDList[14] != " ":
                messagebox.showerror(title="Error", message="Green Team is full!")
                return
            for i in range(15):
                if self.greenIDList[i] == " ":
                    self.greenIDList[i] = playerId
                    self.greenNameList[i] = playerCodeName

                    id_vars2[i].set(self.greenIDList[i])
                    name_vars2[i].set(self.greenNameList[i])
                    break

    #popup menu to get the ID from the user
    def idPopUp(self):
        player_id = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")

        # Center the popup window
        popup.update_idletasks() # Ensure the window size is calculated before positioning
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
                popup.destroy()

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submit_id, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root) # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return player_id

    #Pop up menu to get the codename from the user
    def codeNamePopUp(self):
        codeName = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")

        # Center the popup window
        popup.update_idletasks() # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 300
        window_height = 150

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
            if codeName.strip() == "":
                messagebox.showerror(title="Error", message="Codename cannot be only spaces. Please enter another codename")
                codeName = "None"
            else:
                popup.destroy()

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submitCodename, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root) # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return codeName

    #popup menu to get the equipment code from the player
    def equipmentPopUp(self):
        equipmentId = "None"

        # Create a popup window
        popup = tk.Toplevel(self.root)
        popup.title("Add Player")
        popup.geometry("300x150")

        # Center the popup window
        popup.update_idletasks() # Ensure the window size is calculated before positioning
        screen_width = popup.winfo_screenwidth()
        screen_height = popup.winfo_screenheight()
        window_width = 350
        window_height = 175

        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Label for the equipment ID input
        tk.Label(popup, text="Enter Equipment ID:", font=("Arial", 12)).pack(pady=10)
        tk.Label(popup, text="(Red Team = Odd ID; Green Team = Even ID)", font=("Arial", 12)).pack(pady=5)

        # Entry field for equipment ID
        equipment_var = tk.StringVar()
        equipment_entry = tk.Entry(popup, textvariable=equipment_var, font=("Arial", 12))
        equipment_entry.pack(pady=5)

        # Function to handle submission
        def submit_id():
            nonlocal equipmentId
            equipmentId = equipment_var.get()

            if not equipmentId.isdigit():
                messagebox.showerror(title="Error", message="ID's should only consist of digits. Please reenter the ID")
                equipmentId = "None"
            else:
                popup.destroy()

        # Submit button
        submit_button = tk.Button(popup, text="Submit", command=submit_id, font=("Arial", 12))
        submit_button.pack(pady=10)

        # Keep the popup focused until closed
        popup.transient(self.root) # Make it modal (disable interaction with main window)
        popup.grab_set()
        self.root.wait_window(popup)

        return equipmentId