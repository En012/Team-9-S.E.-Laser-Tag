import tkinter as tk
import tkinter.font as tkFont
import socket

#-------------------------udp configuration defaulting----------------------------
udp_server_ip = "127.0.0.1" #default ip  (need to default stuff in this file as well I guess)
udp_server_port = 20001     #default port
buffersize = 1024           #buffer size for messages through UDP
#--------------------------------------------------------------------------------

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
        #cleans lists for new updates
        #only works when the .set lines are not being used!!!
        name_List.clear()
        name_List2.clear()
        id_List.clear()
        id_List2.clear()
        
        
        #These are for making sure we store the correct info...
        #print red teams information
        print("Red Team IDs: ")
        print(id_List)
        print("Red Team Names: ")
        print(name_List)
        
        
        #print green teams information
        print("Green Team IDs: ")
        print(id_List2)
        print("Green Team Names: ")
        print(name_List2)

        #adding some stuff for UDP
        #sending equipment codes (for red team)        
        for code in id_List:
            if code.strip():
                send_udp_message(code)

        #sending equipment codes (for green team)
        for code in id_List2:
            if code.strip():
                send_udp_message(code)

    
    #---------------------- udp port functions ------------------------------------------
    
    def send_udp_message(message):
        """Send a UDP message (equipment code) to the server."""
        bytesToSend = str.encode(message)
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPClientSocket.settimeout(5)
        try:
            UDPClientSocket.sendto(bytesToSend, (udp_server_ip, udp_server_port))
            print(f"Message send to server: '{message}'")
            msgFromServer = UDPClientSocket.recvfrom(buffersize)
            reply = msgFromServer[0].decode()
            print(f"Reply from server: {reply}")
        except Exception as e: #error handling
            print(f"Error sending UDP message {e}") #error right now, timing out before sending message
        finally:               #closing socket after 
            UDPClientSocket.close()
    

    global box,outline, port_entry, port_sub_btn
    box, port_entry, port_sub_btn = None, None, None

    def change_udp_server_inter():
        change_udp_server(True)

    def change_udp_server(show):
            global box, outline, port_entry, port_sub_btn
            #removing previous dialog if its there
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
                box_font = tkFont.Font(family="Calibri", size = 16, weight="bold")
                msg = ("Enter new UDP Server IP and Port (format: IP, Port)\n" #instruction message for user
                       "Example: 192.168.1.100, 20001")
                box = tk.Label(root, font=box_font, width=50, height=5, text=msg, anchor="n")
                #outline = tk.Frame(bd=0, highlightthickness=0, background="black")
                port_entry = tk.Entry(root, font=box_font, width=30)
                #textwidth = port_entry.winfo_reqwidth()
                port_sub_btn = tk.Button(root, text='Submit', command=submit_udp_server, width=15, height=1) #submits value to the server
                #port_sub_btn_width = port_sub_btn.winfo_reqwidth()
                #outline.place(relx=0.5, rely=0.4, width=100,height=100, anchor="center")
                box.place(relx=0.5, rely=0.4, anchor="center")
                port_entry.place(relx=0.5, rely=0.42, anchor="center")
                port_sub_btn.place(relx=0.5, rely=0.48, anchor="center")


    def submit_udp_server():
        #updating udp server according to user input
        global udp_server_ip, udp_server_port
        val = port_entry.get()
        parts = val.split(',')
        if len(parts) == 2: #checking the if the input looks like "IP, Port" IP = 0, Port = 1
            new_ip = parts[0].strip()
            try:
                new_port = int(parts[1].strip())
                udp_server_ip = new_ip
                udp_server_port = new_port
                print(f"New UDP server set to {udp_server_ip}:{udp_server_port}")
            except ValueError:
                print("Invalid port number! Please re-enter a valid integer.")
        else:
            print("Invalid input, Format must be: IP, Port")
        change_udp_server(False)

    
    #----------------------------------------------- end port functions --------------------------------------------------------------

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
    
#need this to run it on my computer for some reason -Dylan (you can remove it if its harmful)
if __name__ == "__main__":
    root = tk.Tk()               # Create the main window
    player_entry_screen(root)    # Call your function to set up the UI
    root.mainloop()              # Start the event loop