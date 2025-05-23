import socket

#default configuration
udp_server_ip = "127.0.0.1"
udp_server_port = 7500
buffersize = 1024

def send_udp_message(message, server_ip=None, server_port=None):
    #sends a UDP message to the server and prints the reply.
   
    ip = server_ip if server_ip is not None else udp_server_ip
    port = server_port if server_port is not None else udp_server_port
    bytesToSend = str.encode(message)
    UDPClientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    UDPClientSocket.settimeout(5)
    try:
        UDPClientSocket.sendto(bytesToSend, (ip, port))
        print(f"Message sent to server: '{message}'")

        #Commented this out because I believe this is the culpret for our timeout issues (why we got counted off on sprint 3)
        #the client will always time out because its expecting a response back from the server, but the traffic gen will not provide one

        #msgFromServer = UDPClientSocket.recvfrom(buffersize)
        #reply = msgFromServer[0].decode()
        #print(f"Reply from server: {reply}")
    except Exception as e:
        print(f"Error sending UDP message: {e}")
    finally:
        UDPClientSocket.close()

def set_udp_config(ip):
    #Updates the default UDP server configuration for the client.
    global udp_server_ip
    udp_server_ip = ip      #ip: New server IP address.
    print(f"UDP client configuration updated to {udp_server_ip}")