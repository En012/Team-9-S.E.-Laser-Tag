import tkinter as tk
from screen import Screen

class Main:

    #default constructor
    #add member variables as needed
    def __init__(self):
        self.root = tk.Tk()  
        self.screen = Screen(self.root)
        

    #update any member variables here
    def update(self):
        self.root.mainloop()
    

#declare main object
m = Main()

#create main loop
running = True
while running:

    #temporary code until we get the GUI setup
   # userValue = input("Enter q to leave \n")

    #if userValue == "q":
     #   running = False

    #run update methods
    m.update()
