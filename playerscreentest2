import tkinter as tk
 
root=tk.Tk()

#setting name of window
root.title("[test] Player Entry")

#setting the windows size
root.geometry("720x500")

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
    print("Red Team Names: ")
    print(name_List)
    print("Red Team IDs: ")
    print(id_List)
    
    #print green teams information
    print("Green Team Names: ")
    print(name_List2)
    print("Green Team IDs: ")
    print(id_List2)
    
    
#top labels for name and id columns
name_label = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'))
id_label = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'))
name_label2 = tk.Label(root, text = 'Name', font=('calibre',12, 'bold'))
id_label2 = tk.Label(root, text = 'ID', font=('calibre',12, 'bold'))

#red team side slots
for i in range(15):
    #takes user inputs (name_vars) and sets up row number
    num_label = tk.Label(root, text = f"{i+1}. ", font=('Arial',12, 'bold'))
    name_entry = tk.Entry(root, textvariable = name_vars[i], font = ('calibre',10, 'normal'))
    id_entry = tk.Entry(root, textvariable = id_vars[i], font = ('calibre',10, 'normal'))
    
    #sets positions of entries and labels
    #add team label
    id_label.grid(row=0,column=1)
    name_label.grid(row=0,column=2)
    num_label.grid(row=i+1, column=0)
    name_entry.grid(row=i+1, column=2)
    id_entry.grid(row=i+1, column=1)

#green team
for i in range(15):
    #takes user inputs (name_vars2) and sets up row number
    num_label = tk.Label(root, text = f"{i+1}. ", font=('Arial',12, 'bold'))
    name_entry = tk.Entry(root, textvariable = name_vars2[i], font = ('calibre',10, 'normal'))
    id_entry = tk.Entry(root, textvariable = id_vars2[i], font = ('calibre',10, 'normal'))
    
    #sets positions of entries and labels
    #add team label
    id_label2.grid(row=0,column=6)
    name_label2.grid(row=0,column=7)
    num_label.grid(row=i+1, column=5)
    name_entry.grid(row=i+1, column=7)
    id_entry.grid(row=i+1, column=6)

#make key press also activate submit as a test of sorts (LATER)
#button to activate the submit function
sub_btn=tk.Button(root,text = 'Submit', command = submit)
#button placement
sub_btn.grid(row=16,column=5)

#infinite loop for program to work
root.mainloop()
