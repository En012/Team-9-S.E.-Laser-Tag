import tkinter as tk
import os
from PIL import Image, ImageTk
from tkinter import messagebox
import tkinter.font as tkFont
import udpclient
import udpserver
import database

#---------------------- udp port functions ------------------------------------------
    
global box, port_entry, port_sub_btn
box, port_entry, port_sub_btn = None, None, None

def change_udp_server_inter():
    change_udp_server(True)

def change_udp_server(show):
        global box, port_entry, port_sub_btn
        # Destroy any existing dialog widgets
        if box:
            box.destroy()
            box = None
        if port_entry:
            port_entry.destroy()
            port_entry = None
        if port_sub_btn:
            port_sub_btn.destroy()
            port_sub_btn = None

        if show:
            box_font = tkFont.Font(family="Calibri", size=16, weight="bold")
            msg = ("Enter new UDP Server IP and Port (format: IP, Port)\n"
                   "Example: 192.168.1.100, 20001")
            box = tk.Label(root, font=box_font, width=50, height=5, text=msg, anchor="n")
            port_entry = tk.Entry(root, font=box_font, width=30)
            port_sub_btn = tk.Button(root, text='Submit', command=submit_udp_server, width=15, height=1)
            box.place(relx=0.5, rely=0.4, anchor="center")
            port_entry.place(relx=0.5, rely=0.42, anchor="center")
            port_sub_btn.place(relx=0.5, rely=0.48, anchor="center")

def submit_udp_server():
        global box, port_entry, port_sub_btn
        #Handles new UDP configuration input from the user.
        val = port_entry.get()
        parts = val.split(',')
        if len(parts) == 2:
            new_ip = parts[0].strip()
            try:
                new_port = int(parts[1].strip())
                udpclient.set_udp_config(new_ip, new_port)
                udpserver.update_and_restart_server(new_ip, new_port)
            except ValueError:
                udp_error_popup()
        else:
            udp_error_popup()
        change_udp_server(False)

def udp_error_popup(message):
    messagebox.showerror(title="Error", message="Invalid port number! Please re-enter a valid integer.")


#----------------------------------------------- end port functions --------------------------------------------------------------

#setup for the player entry screen
def player_entry_screen(root):
    #setting name of window
    root.title("[test] Player Entry")
    root.minsize(800,600)

    #setting the sizes
    title_relheight = 0.1 #10% of the window is for title
    button_relheight = 0.1 #10% for the buttons at the bottom
    row_count = 15
    row_relheight = (1 - title_relheight - button_relheight) / row_count

    #Set background colors
    red_frame = tk.Frame(bd=0, highlightthickness=0, background="red")
    green_frame = tk.Frame(bd=0, highlightthickness=0, background="green")


    #Title Placement
    titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
    title = tk.Label(root, font=titlefont, text="Edit Current Game", background="black", fg = "white")
    #title.place(x = int(width/2 - title_width/2), anchor = "nw") #this title does not scale with window size
    title.place(relx=0.5, rely=0, relwidth=1.0, relheight=title_relheight, anchor="n")
    

    #Place background frames
    red_frame.place(relx=0, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)
    green_frame.place(relx=0.5, rely=title_relheight, relwidth=0.5, relheight=1 - title_relheight)


    #red team user list
    name_List = []
    id_List = []
    #green team user list
    name_List2 = []
    id_List2 = []

    #the tk.StringVar() for _ in range(15) is neccesary for .get() to work

    #red team user inputs
    name_vars = [tk.StringVar() for _ in range(15)]
    id_vars = [tk.StringVar() for _ in range(15)]
    #green team user inputs
    name_vars2 = [tk.StringVar() for _ in range(15)]
    id_vars2 = [tk.StringVar() for _ in range(15)]

    #function activates when submit button is clicked
    #adds input names to a list
    def submit():
        #clearing database before new submit
        database.cleardatabase()
        
        #cleans lists for new updates
        #only works when the .set lines are not being used!!!
        name_List.clear()
        name_List2.clear()
        id_List.clear()
        id_List2.clear()
        
        #for loop to add red names to lists when submitting
        for i in range(row_count):
            red_name = name_vars[i].get().strip()
            red_id = id_vars[i].get().strip()
            if red_name:
                name_List.append(red_name) #adding red names to list if input is present
            if red_id:
                id_List.append(red_id) #adding red ids to list if input is present

        #for loop to add green names to lists
        for i in range(row_count):
            green_name = name_vars2[i].get().strip()
            green_id = id_vars2[i].get().strip()
            if green_name:
                name_List2.append(green_name) #adding green names to list if input is present
            if green_id: 
                id_List2.append(green_id) #adding green ids to list if input is present
        
        #These are for making sure we store the correct info...
        #print red teams information
        print("Red Team IDs: ", id_List)
        print("Red Team Names: ", name_List)
        
        
        #print green teams information
        print("Green Team IDs: ", id_List2)
        print("Green Team Names: ", name_List2)

        #adding some stuff for UDP
        #sending equipment codes (for red team)        
        for code in id_List:
            if code.strip():
                udpclient.send_udp_message(code)

        #sending equipment codes (for green team)
        for code in id_List2:
            if code.strip():
                udpclient.send_udp_message(code)

        #saving players to data base
        database.save_players("Red", name_List, id_List)
        database.save_players("Green", name_List2, id_List2)
        print("Player information saved to database")


    #top labels for name and id columns
    name_label = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="red")
    id_label = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="red")
    name_label2 = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="green")
    id_label2 = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="green")


    for i in range(row_count):
        row_rel_y = title_relheight + (i + 0.5) * row_relheight  # Now within bounds
        num_label = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="red")
        num_label.place(relx=0.05, rely=row_rel_y, anchor="center")
        
        #id labels
        id_label = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="red")
        id_label.place(relx=0.09, rely=row_rel_y, anchor="e")  # `anchor="e"` aligns it to the right

        #id entry
        id_entry = tk.Entry(root, textvariable=id_vars[i], font=('calibre', 10, 'normal'))
        id_entry.place(relx=0.15, rely=row_rel_y, relwidth=0.1, anchor="center")
        
        #name labels
        name_label = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="red")
        name_label.place(relx=0.25, rely=row_rel_y, anchor="e")  # `anchor="e"` aligns it to the right

        #name entry
        name_entry = tk.Entry(root, textvariable=name_vars[i], font=('calibre', 10, 'normal'))
        name_entry.place(relx=0.33, rely=row_rel_y, relwidth=0.15, anchor="center")


    for i in range(row_count):
        row_rel_y = title_relheight + (i + 0.5) * row_relheight  # Adjusted placement
        num_label2 = tk.Label(root, text=f"{i+1}.", font=('Arial', 12, 'bold'), background="green")
        num_label2.place(relx=0.55, rely=row_rel_y, anchor="center")
        
        #id labels
        id_label2 = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="green")
        id_label2.place(relx=0.59, rely=row_rel_y, anchor="e")  # `anchor="e"` aligns it to the right

        id_entry2 = tk.Entry(root, textvariable=id_vars2[i], font=('calibre', 10, 'normal'))
        id_entry2.place(relx=0.65, rely=row_rel_y, relwidth=0.1, anchor="center")
        
        #name labels
        name_label2 = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="green")
        name_label2.place(relx=0.75, rely=row_rel_y, anchor="e")  # `anchor="e"` aligns it to the right

        name_entry2 = tk.Entry(root, textvariable=name_vars2[i], font=('calibre', 10, 'normal'))
        name_entry2.place(relx=0.83, rely=row_rel_y, relwidth=0.15, anchor="center")


    #make key press also activate submit as a test of sorts (LATER)
    #button to activate the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit, width = 15, height = 3)

    #button to activate the change ports function
    port_btn= tk.Button(root, text="Change Port", command=change_udp_server_inter, width = 15, height = 3)
    
    #button placement
    sub_btn.place(relx=0.5, rely=0.95, anchor="center", relwidth=0.2, relheight=0.05)
    port_btn.place(relx=0.2, rely=0.95, anchor="center", relwidth=0.25, relheight=0.05)

    #infinite loop for program to work
    #root.mainloop()
    
#switches from the splash screen (logo.jpg) to the playerentry screen   
def switch():
    player_entry_screen(root) #call function to set up the UI

#main function, code starts here
if __name__ == "__main__":
    #initializing database
    database.init_db()

    root = tk.Tk()
    root.title("Image Display")
    root.configure(bg="black")

    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    img_path = os.path.expanduser("images/logo.jpg")

    img = Image.open("images/logo.jpg")
    img = img.resize((width, height), Image.LANCZOS)
    img = ImageTk.PhotoImage(img)
    label = tk.Label(root, image=img, bg="black")    
    label.pack()
    root.geometry(f"{width}x{height}")
    root.after(3000, switch) #create the main window   
    udpserver.start_udp_server()
    
    #start the event loop
    root.mainloop()              