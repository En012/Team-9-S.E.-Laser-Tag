import database
from display import Display

#initalize the database
database.initialize_database()

# Main function
if __name__ == "__main__":

    #create screen object
    screen = Display()

    #Loop the program
    screen.root.mainloop()