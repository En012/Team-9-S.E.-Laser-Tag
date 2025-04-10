import socket
import threading
import udpclient

class UDPServer:

    #default constructor
    def __init__(self, message_callback=None):

        #variables for server
        self.server_running = False
        self.udp_server_socket = None
        self.udp_server_thread = None

        #Default server config
        self.udp_server_ip = "127.0.0.1"  # default IP address
        self.udp_server_port = 7501      # default port
        self.buffersize = 1024           # buffer size

        #declare a return function in order to pass messages back to playeraction.py
        self.message_callback = message_callback


    def udp_server_loop(self):
        #listens for messages from client
        while self.server_running:
            try:
                data, addr = self.udp_server_socket.recvfrom(self.buffersize)
                message = data.decode()

                #all messages sent to the UDP server should be in the form {integer:integer} 
                #first integer is equipment ID of player transmitting, and the second integer is the equipment ID of the player who got hit
                #the reply message should only be the equipment ID of the player who got hit
                print(f"UDP server received from {addr}:{message}")
                
                #send the message recieved from traffic gen to playeraction.py
                if self.message_callback:
                    self.message_callback(message)
                else:
                    print("Error: message_callback is none")

                #get the second integer from the message
                response = self.extract_second_int(message)

                #Since the server is on port 7501 and servertraffic expects to recieve messages from port 7500
                #Use the UDP Client we already had running (which is transmitting on port 7500) to respond
                udpclient.send_udp_message(f"{response}")
            except Exception as e:  # <-- Code always seems to throw an error even though servertraffic and udpserver are running fine, I'm not sure why
                if self.server_running:
                    print("UDP server error:", e)
                break

    def start_udp_server(self):
        #Starts the UDP server
        try:
            self.udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.udp_server_socket.bind((self.udp_server_ip, self.udp_server_port))
            self.server_running = True
            self.udp_server_thread = threading.Thread(target=self.udp_server_loop, daemon=True)
            self.udp_server_thread.start()
            print(f"UDP server started on {self.udp_server_ip}:{self.udp_server_port}")
        except Exception as e:
            print("Failed to start UDP server:", e)

    def stop_udp_server(self):
        #Stops the servers
        self.server_running = False
        if self.udp_server_socket:
            self.udp_server_socket.close()
            self.udp_server_socket = None
            print("UDP server stopped.")

    def update_and_restart_server(self, new_ip):
        self.stop_udp_server()  #Stopping the current server
        self.udp_server_ip = new_ip
        self.start_udp_server()  #Restarting with new configuration (new ip)

    # Extract the second integer from the message
    def extract_second_int(self, message):
        try:
            parts = message.split(":")
            if len(parts) == 2:
                second_integer = int(parts[1])  # Parse the second part as an integer
                response = str(second_integer)  # Convert it back to a string
            else:
                response = "Error: Invalid message format"
        except ValueError:
            response = "Error: Non-integer value in message"
        
        return response