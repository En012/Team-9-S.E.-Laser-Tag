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
        #update the GUI
        self.root.mainloop()
    

#declare main object
m = Main()

#create main loop
running = True
while running:

    #run update methods
    m.update()
