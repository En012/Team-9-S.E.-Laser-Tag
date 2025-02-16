import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
import udpclient
import udpserver
import database


#initalize the database
database.init_db()

#---------------------- udp port functions ------------------------------------------

def change_udp_server_inter():
    change_udp_server()

def change_udp_server():
    udp_server_popup(root)

def udp_server_popup(root):
    udp_ip_port = "None"

    # Create a popup window
    popup = tk.Toplevel(root)
    popup.title("Change UDP Server")
    popup.geometry("400x200")  # Set window size

    # Center the popup window
    popup.update_idletasks()  # Ensure the window size is calculated before positioning
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    window_width = 400
    window_height = 200

    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2)
    popup.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    # Label for the UDP server IP and port input
    tk.Label(popup, text="Enter new UDP Server IP and Port (format: IP, Port)\nExample: 192.168.1.100, 20001", font=("Arial", 12)).pack(pady=10)

    # Entry field for UDP server IP and port
    udp_ip_port_var = tk.StringVar()
    udp_ip_port_entry = tk.Entry(popup, textvariable=udp_ip_port_var, font=("Arial", 12))
    udp_ip_port_entry.pack(pady=5)

    # Function to handle submission
    def submit_udp_server():
        nonlocal udp_ip_port
        udp_ip_port = udp_ip_port_var.get()
        parts = udp_ip_port.split(',')
        if len(parts) == 2:
            new_ip = parts[0].strip()
            try:
                new_port = int(parts[1].strip())
                udpclient.set_udp_config(new_ip, new_port)
                udpserver.update_and_restart_server(new_ip, new_port)
            except ValueError:
                messagebox.showerror(title="Error", message="Invalid port number! Please re-enter a valid integer.")
                udp_ip_port = "None"
        else:
            messagebox.showerror(title="Error", message="Invalid input, format must be: IP, Port")
            udp_ip_port = "None"
        popup.destroy()  # Close the popup

    # Submit button
    submit_button = tk.Button(popup, text="Submit", command=submit_udp_server, font=("Arial", 12))
    submit_button.pack(pady=10)

    # Keep the popup focused until closed
    popup.transient(root)  # Make it modal (disable interaction with main window)
    popup.grab_set()
    root.wait_window(popup)

    return udp_ip_port

def udp_error_popup(message):
    messagebox.showerror(title="Error", message=message)

#----------------------------------------------- end port functions --------------------------------------------------------------

#function for starting the game, to be fully implemented later
def startGame(id_List, id_List2):
    numRedPlayers = 0
    numGreenPlayers = 0

    #check to make sure that a player is on each team
    for i in range(15):
        if id_List[i] != "None":
            numRedPlayers += 1
        
        if id_List2[i] != "None":
            numGreenPlayers += 1

    #if both teams dont have at least one player, throw an error
    if numRedPlayers == 0 or numGreenPlayers == 0:
        messagebox.showerror(title="Error", message="You must have at least one player on each team to start a game!")
        return
    #otherwise, start the game
    else:
        messagebox.showinfo(title="Notification", message="Start will be implemented in a future sprint!")

#code for the idPopUp menu
def idPopUp(root):
    player_id = "None"

    # Create a popup window
    popup = tk.Toplevel(root)
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
    popup.transient(root)  # Make it modal (disable interaction with main window)
    popup.grab_set()
    root.wait_window(popup)

    return player_id

#code for the namePopUp menu
def codeNamePopUp(root):

    codeName = "None"

    # Create a popup window
    popup = tk.Toplevel(root)
    popup.title("Add Player")
    popup.geometry("300x500")  # Set window size

    # Center the popup window
    popup.update_idletasks()  # Ensure the window size is calculated before positioning
    screen_width = popup.winfo_screenwidth()
    screen_height = popup.winfo_screenheight()
    window_width = 300
    window_height = 150

    #center the popup window
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
    popup.transient(root)  # Make it modal (disable interaction with main window)
    popup.grab_set()
    root.wait_window(popup)

    return codeName

#code for the equipmentPopUp menu
def equipmentPopUp(root):
    
    equipmentId = "None"

    # Create a popup window
    popup = tk.Toplevel(root)
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

        #check to make sure that the user only entered numbers into the ID field
        if not equipmentId.isdigit():
            messagebox.showerror(title="Error", message="ID's should only consist of digits. Please reenter the ID")
            equipmentId = "None"
        else:
            popup.destroy()  # Close the popup

    # Submit button
    submit_button = tk.Button(popup, text="Submit", command=submit_id, font=("Arial", 12))
    submit_button.pack(pady=10)

    # Keep the popup focused until closed
    popup.transient(root)  # Make it modal (disable interaction with main window)
    popup.grab_set()
    root.wait_window(popup)

    return equipmentId

#called when the addPlayer button is pressed:
def addPlayer(root, id_List, name_List, id_List2, name_List2, id_vars, name_vars, id_vars2, name_vars2):
    
    #get Id from the idPopUp Window
    playerId = idPopUp(root)

    #if enteredId = None, then getting the id failed so return with no changes
    if playerId == "None":
        return
    
    #check if player with id is already in the game
    if playerId in id_List or playerId in id_List2:
        messagebox.showerror(title="Error", message=f"Player with ID: {playerId} is already in the game")
        return


    #STEP 2: check against the database to see if the id is there
    database.check_or_add_player(playerId) #if ID is not in the database, add playerID in along with default values
    playerCodeName = database.get_player_name(playerId) #codeName will either be None (if ID is new), or a different string

    #STEP 3: If id is new, ask for the codename
    if playerCodeName is None:
        playerCodeName = codeNamePopUp(root)

    #if enteredCodeName = None, then getting the codename failed so return with no changes
    if playerCodeName == "None":
        return
    #otherwise, change the codename corresponding to the player ID
    else:
        database.set_player_name(playerId, playerCodeName)

    #STEP 4: Get equipment ID from the player:
    playerEquipmentId = equipmentPopUp(root)
    
    #if playerEquipmentId = None, then getting the equipment ID failed so return with no changes
    if playerEquipmentId == "None":
        return
    
    #STEP 5: Add the player info to the playerentry screen
    #If playerEquipmentId is odd, add the player to red team
    if int(playerEquipmentId) % 2 == 1:

        #make sure that red team isnt full before adding the player
        if id_List[14] != "None":
            messagebox.showerror(title="Error", message="Red Team is full!")
            return
        #go through the list of id's and place the player in the next available spot
        for i in range(15):
            if id_List[i] == "None":
                id_List[i] = playerId
                name_List[i] = playerCodeName

                id_vars[i].set(id_List[i])
                name_vars[i].set(name_List[i])
                break
    else:
        #make sure that green team isnt full before adding the player
        if id_List2[14] != "None":
            messagebox.showerror(title="Error", message="Green Team is full!")
            return
        #go through the list of id's and place the player in the next available spot
        for i in range(15):
            if id_List2[i] == "None":
                id_List2[i] = playerId
                name_List2[i] = playerCodeName

                id_vars2[i].set(id_List2[i])
                name_vars2[i].set(name_List2[i])
                break


def player_entry_screen(root):
    #setting name of window
    root.title("Photon")
    root.minsize(800,600)

    #setting the sizes
    title_relheight = 0.1  # 10% of the window is for title
    button_relheight = 0.1  # 10% for the buttons at the bottom
    row_count = 15
    row_relheight = (1 - title_relheight - button_relheight) / row_count

    #Set background colors
    red_frame = tk.Frame(root, bd=0, highlightthickness=0, background="red")
    green_frame = tk.Frame(root, bd=0, highlightthickness=0, background="green")

    #Title Placement
    titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
    title = tk.Label(root, font=titlefont, text="Edit Current Game", background="black", fg="white")
    title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")

    #Place background frames
    red_frame.place(relx=0, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)
    green_frame.place(relx=0.5, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)

    # Red & Green Team User Lists
    name_List = ["None"] * 15
    id_List = ["None"] * 15
    name_List2 = ["None"] * 15
    id_List2 = ["None"] * 15

    # Create StringVars for dynamic updates
    id_vars = [tk.StringVar(value=id_List[i]) for i in range(15)]
    name_vars = [tk.StringVar(value=name_List[i]) for i in range(15)]
    id_vars2 = [tk.StringVar(value=id_List2[i]) for i in range(15)]
    name_vars2 = [tk.StringVar(value=name_List2[i]) for i in range(15)]

    # Create labels for red team
    for i in range(row_count):
        row_rel_y = title_relheight + (i + 0.5) * row_relheight  

        num_label = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="red")
        num_label.place(relx=0.05, rely=row_rel_y, anchor="center")

        id_label = tk.Label(root, text='ID:', font=('calibre', 12, 'bold'), background="red")
        id_label.place(relx=0.09, rely=row_rel_y, anchor="e")

        id_entry = tk.Label(root, textvariable=id_vars[i], font=('calibre', 10, 'normal'), background="white")
        id_entry.place(relx=0.15, rely=row_rel_y, relwidth=0.1, anchor="center")

        name_label = tk.Label(root, text='Name:', font=('calibre', 12, 'bold'), background="red")
        name_label.place(relx=0.25, rely=row_rel_y, anchor="e")

        name_entry = tk.Label(root, textvariable=name_vars[i], font=('calibre', 10, 'normal'), background="white")
        name_entry.place(relx=0.33, rely=row_rel_y, relwidth=0.15, anchor="center")

    # Create labels for green team
    for i in range(row_count):
        row_rel_y = title_relheight + (i + 0.5) * row_relheight  

        num_label2 = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="green")
        num_label2.place(relx=0.55, rely=row_rel_y, anchor="center")

        id_label2 = tk.Label(root, text='ID:', font=('calibre', 12, 'bold'), background="green")
        id_label2.place(relx=0.59, rely=row_rel_y, anchor="e")

        id_entry2 = tk.Label(root, textvariable=id_vars2[i], font=('calibre', 10, 'normal'), background="white")
        id_entry2.place(relx=0.65, rely=row_rel_y, relwidth=0.1, anchor="center")

        name_label2 = tk.Label(root, text='Name:', font=('calibre', 12, 'bold'), background="green")
        name_label2.place(relx=0.75, rely=row_rel_y, anchor="e")

        name_entry2 = tk.Label(root, textvariable=name_vars2[i], font=('calibre', 10, 'normal'), background="white")
        name_entry2.place(relx=0.83, rely=row_rel_y, relwidth=0.15, anchor="center")

    #Buttons

    #button to activate the start game function
    #lambda prevents the startGame function from being called as soon as the program starts up
    sub_btn=tk.Button(root,text = 'Start Game', command = lambda: startGame(id_List, id_List2), width = 15, height = 3)

    #button to activate the change ports function
    port_btn= tk.Button(root, text="Change Port", command=change_udp_server_inter, width = 15, height = 3)

    #button for adding a player to the game
    add_btn = tk.Button(root, text='Add Player', 
                        command=lambda: addPlayer(root, id_List, name_List, id_List2, name_List2, id_vars, name_vars, id_vars2, name_vars2), 
                        width=15, height=3)

    # Button placement
    sub_btn.place(relx=0.5, rely=0.95, anchor="center", relwidth=0.2, relheight=0.05)
    port_btn.place(relx=0.2, rely=0.95, anchor="center", relwidth=0.2, relheight=0.05)
    add_btn.place(relx=0.8, rely=0.95, anchor="center", relwidth=0.2, relheight=0.05)

def switch():
    player_entry_screen(root)

# Main function
if __name__ == "__main__":

    #setup tkinter GUI elements
    root = tk.Tk()
    root.title("Loading...")
    root.configure(bg="black")

    #get screen width and height
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    #splash screen
    img = Image.open("images/logo.jpg")
    img = img.resize((width, height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img, bg="black")    
    label.pack()
    root.geometry(f"{width}x{height}")

    #switch screens after 3 seconds
    root.after(3000, switch) 

    #Go
    root.mainloop()