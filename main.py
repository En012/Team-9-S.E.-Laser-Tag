import database
from display import Display

# #initalize the database
database.initialize_database()

# Main function
if __name__ == "__main__":
    #this line starts up the udp server upon application start (if not here, server is not running until address swap)
    #udpserver.start_udp_server()

    #create screen object
    screen = Display()

    #Go
    screen.root.mainloop()