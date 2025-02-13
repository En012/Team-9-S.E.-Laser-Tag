import tkinter as tk
import tkinter.font as tkFont

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
    title.place(x = int(width/2 - title_width/2), anchor = "nw")
    

    #Place background frames
    red_frame.place(x=0, y = int(title_height), relwidth=.5, height=int(height - title_height), anchor="nw")
    green_frame.place(relx=.5, y = int(title_height), relwidth=.5, height=int(height - title_height), anchor="nw")
    title_frame.place(x = 0, y = 0, relwidth = 1.0, height=int(title_height), anchor="nw")
    root.geometry(f"{width}x{height}")

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
        id_label.grid(row=0,column=1)
        id_label.place(x = num_width + id_width/2, y = title_height)
        name_label.grid(row=0,column=2)
        name_label.place(x = (num_width + id_width + name_width/2), y = title_height)
        num_label.grid(row=i+1, column=0)
        if i < 9:
            num_label.place(x = num_width/4, y = (title_height + id_height + (num_height * i)))
        else:
            num_label.place(y = (title_height + id_height + (num_height * i)))
        name_entry.grid(row=i+1, column=2)
        name_entry.place(x = (num_width + id_width + 20), y = (title_height + id_height + (num_height * i)))
        id_entry.grid(row=i+1, column=1)
        id_entry.place(x = (num_width + 10), y = (title_height + id_height + (num_height * i)))

    #green team
    for i in range(15):
        #takes user inputs (name_vars2) and sets up row number
        num_label = tk.Label(root, text = f"{i+1}. ", font=('Arial',12, 'bold'), background="green")
        name_entry = tk.Entry(root, textvariable = name_vars2[i], font = ('calibre',10, 'normal'))
        id_entry = tk.Entry(root, textvariable = id_vars2[i], font = ('calibre',10, 'normal'))
        
        #sets positions of entries and labels
        #add team label
        """
        id_label2.grid(row=0,column=6)
        name_label2.grid(row=0,column=7)
        num_label.grid(row=i+1, column=5)
        name_entry.grid(row=i+1, column=7)
        id_entry.grid(row=i+1, column=6)
        """
        id_label2.grid(row=0,column=6)
        id_label2.place(x = (width/2 + num_width + id_width/2), y = title_height)
        name_label2.grid(row=0,column=7)
        name_label2.place(x = (width/2 + num_width + id_width + name_width/2), y = title_height)
        num_label.grid(row=i+1, column=5)
        if i < 9:
            num_label.place(x = width/2 + num_width/4, y = (title_height + id_height + (num_height * i)))
        else:
            num_label.place(x = width/2, y = (title_height + id_height + (num_height * i)))
        name_entry.grid(row=i+1, column=7)
        name_entry.place(x = (width/2 + num_width + id_width + 20), y = (title_height + id_height + (num_height * i)))
        id_entry.grid(row=i+1, column=6)
        id_entry.place(x = (width/2 + num_width + 10), y = (title_height + id_height + (num_height * i)))

    #make key press also activate submit as a test of sorts (LATER)
    #button to activate the submit function
    sub_btn=tk.Button(root,text = 'Submit', command = submit, width = 15, height = 3)
    #button placement
    sub_btn_width = sub_btn.winfo_reqwidth()
    sub_btn.grid(row=16,column=5)
    sub_btn.place(x = width/2 - sub_btn_width/2, y = ((3*height)/4))
    #infinite loop for program to work
    #root.mainloop()
