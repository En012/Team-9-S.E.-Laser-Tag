import socket
import threading
import udpclient

#Default server config
udp_server_ip = "127.0.0.1"  # default IP address
udp_server_port = 7501      # default port
buffersize = 1024           # buffer size

#global variables for server
server_running = False
udp_server_socket = None
udp_server_thread = None

def udp_server_loop():
    #listens for messages from client
    global server_running, udp_server_socket
    while server_running:
        try:
            data, addr = udp_server_socket.recvfrom(buffersize)
            message = data.decode()

            #all messages sent to the UDP server should be in the form {integer:integer} 
            #first integer is equipment ID of player transmitting, and the second integer is the equipment ID of the player who got hit
            #the reply message should only be the equipment ID of the player who got hit
            print(f"UDP server received from {addr}:{message}")
            
            #get the second integer from the message
            response = extract_second_int(message)

            #Since the server is on port 7501 and servertraffic expects to recieve messages from port 7500
            #Use the UDP Client we already had running (which is transmitting on port 7500) to respond
            udpclient.send_udp_message(f"{response}")
        except Exception as e: #<-- Code always seems to throw an error even though servertraffic and udpserver are running fine, I'm not sure why
            if server_running:
                print("UDP server error:", e)
            break

def start_udp_server():
    #Starts the UDP server
    global server_running, udp_server_socket, udp_server_thread, udp_server_ip, udp_server_port
    try:
        udp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        udp_server_socket.bind((udp_server_ip, udp_server_port))
        server_running = True
        udp_server_thread = threading.Thread(target=udp_server_loop, daemon=True)
        udp_server_thread.start()
        print(f"UDP server started on {udp_server_ip}:{udp_server_port}")
    except Exception as e:
        print("Failed to start UDP server:", e)

def stop_udp_server():
    #Stops the servers
    global server_running, udp_server_socket
    server_running = False
    if udp_server_socket:
        udp_server_socket.close()
        udp_server_socket = None
        print("UDP server stopped.")

def update_and_restart_server(new_ip, new_port):
    stop_udp_server()  #Stopping the current server
    global udp_server_ip, udp_server_port
    udp_server_ip = new_ip
    udp_server_port = new_port
    start_udp_server()  #Restarting with new configuration (new ip)

# Extract the second integer from the message
def extract_second_int(message):
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


if __name__ == "__main__":
    start_udp_server()
    try:
        while True:
            pass  #keeping the server running
    except KeyboardInterrupt:
        stop_udp_server()