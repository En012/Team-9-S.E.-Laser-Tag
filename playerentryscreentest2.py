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

    #setting the windows size
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()

    #Set background colors
    red_frame = tk.Frame(bd=0, highlightthickness=0, background="red")
    green_frame = tk.Frame(bd=0, highlightthickness=0, background="green")
    title_frame = tk.Frame(bd=0, highlightthickness=0, background="black")
    #green_frame = tk.Frame(bd=0, highlightthickness=0, background="blue")
    #red_frame.place(x=0, y = title_height, relwidth=.5, height=(height - title_height), anchor="nw")
    #green_frame.place(relx=.5, y = title_height, relwidth=.5, height=(height - title_height), anchor="nw")

    #Title Placement
    titlefont = tkFont.Font(family='Calibri', size=36, weight='bold')
    title = tk.Label(root, font=titlefont, text="Edit Current Game", background="black", fg = "white")
    title_height = title.winfo_reqheight()
    title_width = title.winfo_reqwidth()
    #title.place(x = int(width/2 - title_width/2), anchor = "nw") #this title does not scale with window size
    title.place(relx = 0.5, y = 0, anchor = "n") #this title scales with window size
    

    #Place background frames
    red_frame.place(x=0, y = int(title_height), relwidth=.5, height=int(height - title_height), anchor="nw")
    green_frame.place(relx=.5, y = int(title_height), relwidth=.5, height=int(height - title_height), anchor="nw")
    title_frame.place(x = 0, y = 0, relwidth = 1.0, height=int(title_height), anchor="nw")
    root.geometry(f"{width}x{height}")


    #port number
    port = "127.0.0.1"
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
        
        #variables for user input
        #have to have one set for each one
        #red team user inputs added to list
        for i in range(15): #15 player slots
            name = name_vars[i].get()
            id = id_vars[i].get()
            
            #name_vars[i].set("")
            #id_vars[i].set("")
            
            name_List.append(name)
            id_List.append(id)
            pass
        
        #green team user inputs added to list
        for j in range(15): #15 player slots
            name2 = name_vars2[j].get()
            id2 = id_vars2[j].get()
            
            #name_vars[i].set("")
            #id_vars[i].set("")
            
            name_List2.append(name2)
            id_List2.append(id2)
            pass
        
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
    
    
    # def change_port_inter():
    #     box_bool = True
    #     change_port(box_bool)

    global box, port_entry, port_sub_btn
    box, port_entry, port_sub_btn = None, None, None

    def change_udp_server_inter():
        change_udp_server(True)

    def change_udp_server(show):
            global box, port_entry, port_sub_btn
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
                boxwidth = box.winfo_reqwidth()
                boxheight = box.winfo_reqheight()
                box.place(x=int(width/2 - boxwidth/2), y=int(height/2 - boxheight/2))
                port_entry = tk.Entry(root, font=box_font, width=30)
                textwidth = port_entry.winfo_reqwidth()
                port_entry.place(x=int(width/2 - textwidth/2), y=int(height/2))
                port_sub_btn = tk.Button(root, text='Submit', command=submit_udp_server, width=15, height=1) #submits value to the server
                port_sub_btn_width = port_sub_btn.winfo_reqwidth()
                port_sub_btn.place(x=int(width/2 - port_sub_btn_width/2), y=int(height/2 + 45))

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

    # def change_port(box_bool):
    #     global box, port_entry, port_sub_btn
    #     if box:
    #         box.destroy()
    #         box = None
    #     if port_entry:
    #         port_entry.destroy()
    #         port_entry = None
    #     if port_sub_btn:
    #         port_sub_btn.destroy()
    #         port_sub_btn = None
    #     if(box_bool):
    #         box_font = tkFont.Font(family="Calibri", size=16, weight="bold")
    #         box = tk.Label(root, font=box_font, width=30, height=10, text="Please Type New Port Number", anchor = "n")
    #         boxwidth = box.winfo_reqwidth()
    #         boxheight = box.winfo_reqheight()
    #         box.place(x=int(width/2 - boxwidth/2), y=int(height/2 - boxheight/2))
    #         port_entry = tk.Entry(root, font=box_font, width=10)
    #         textwidth = port_entry.winfo_reqwidth()
    #         port_entry.place(x=int(width/2 - textwidth/2), y=int(height/2))
    #         port_sub_btn=tk.Button(root,text = 'Submit', command = submit_port, width = 15, height = 1)
    #         port_sub_btn_width = port_sub_btn.winfo_reqwidth()
    #         port_sub_btn.place(x = int(width/2 - port_sub_btn_width/2), y = int(height/2 + 45))
            
    #     pass
    # #def submit_port():
    #     global port_entry
    #     port_value = port_entry.get()
    #     change_port(False)
    #     print(f"New port entered: {port_value}")
    #     return port_value
    
    #----------------------------------------------- end port functions --------------------------------------------------------------

    #top labels for name and id columns
    name_label = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="red")
    id_label = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="red")
    name_label2 = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'), background="green")
    id_label2 = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'), background="green")

    #red team side slots
    for i in range(15):
        #takes user inputs (name_vars) and sets up row number
        num_label = tk.Label(root, text = f"{i+1}. ", font=('Arial',12, 'bold'), background="red")
        name_entry = tk.Entry(root, textvariable = name_vars[i], font = ('calibre',10, 'normal'))
        id_entry = tk.Entry(root, textvariable = id_vars[i], font = ('calibre',10, 'normal'))
        
        #consistent spacing
        num_label_space = tk.Label(root, text = f"10", font=('Arial',12, 'bold'), background="red")
        #Grabbing all heights and widths for better placement
        num_width = num_label_space.winfo_reqwidth()
        name_width = name_entry.winfo_reqwidth()
        id_width = id_entry.winfo_reqwidth()
        id_height = id_label.winfo_reqheight()
        num_height = num_label.winfo_reqheight()
        name_height = name_entry.winfo_reqheight()

        #sets positions of entries and labels
        #add team label
        id_label.place(x = num_width + id_width/2, y = title_height)
        name_label.place(x = (num_width + id_width + name_width/2), y = title_height)
        if i < 9:
            num_label.place(x = num_width/4, y = (title_height + id_height + (num_height * i)))
        else:
            num_label.place(y = (title_height + id_height + (num_height * i)))
        name_entry.place(x = (num_width + id_width + 20), y = (title_height + id_height + (num_height * i)))
        id_entry.place(x = (num_width + 10), y = (title_height + id_height + (num_height * i)))

    #green team
    for i in range(15):
        #takes user inputs (name_vars2) and sets up row number
        num_label = tk.Label(root, text = f"{i+1}. ", font=('Arial',12, 'bold'), background="green")
        name_entry = tk.Entry(root, textvariable = name_vars2[i], font = ('calibre',10, 'normal'))
        id_entry = tk.Entry(root, textvariable = id_vars2[i], font = ('calibre',10, 'normal'))
        
        #sets positions of entries and labels
        #add team label
        id_label2.place(x = (width/2 + num_width + id_width/2), y = title_height)
        name_label2.place(x = (width/2 + num_width + id_width + name_width/2), y = title_height)
        if i < 9:
            num_label.place(x = width/2 + num_width/4, y = (title_height + id_height + (num_height * i)))
        else:
            num_label.place(x = width/2, y = (title_height + id_height + (num_height * i)))
        name_entry.place(x = (width/2 + num_width + id_width + 20), y = (title_height + id_height + (num_height * i)))
        id_entry.place(x = (width/2 + num_width + 10), y = (title_height + id_height + (num_height * i)))

    #make key press also activate submit as a test of sorts (LATER)
    #button to activate the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit, width = 15, height = 3)

    #button to activate the change ports function
    port_btn= tk.Button(root, text="Change Port", command=change_udp_server_inter, width = 15, height = 3)
    
    #button placement
    sub_btn_width = sub_btn.winfo_reqwidth()
    port_btn.place(x = width/8, y = ((3*height)/4), anchor="nw")
    sub_btn.place(x = width/2 - sub_btn_width/2, y = ((3*height)/4), anchor = "nw")
    #infinite loop for program to work
    #root.mainloop()
    
#need this to run it on my computer for some reason -Dylan (you can remove it if its harmful)
if __name__ == "__main__":
    root = tk.Tk()               # Create the main window
    player_entry_screen(root)    # Call your function to set up the UI
    root.mainloop()              # Start the event loop