import database
from display import Display
from udpserver import UDPServer

#initalize the database
database.initialize_database()

# Main function
if __name__ == "__main__":

    #create screen object
    screen = Display()

    #creating server object
    udpserver = UDPServer()

    #start server
    udpserver.start_udp_server()

    #Loop the program
    screen.root.mainloop()