class Main:
    
    #default constructor
    #add member variables as needed
    def __init__(self):
        pass

    #update any member variables here
    def update(self):
        pass
    

#declare main object
m = Main()

#create main loop
running = True
while running:

    #temporary code until we get the GUI setup
    userValue = input("Enter q to leave \n")

    if userValue == "q":
        running = False

    m.update()

    #adfdfs