import socket
import signal
import sys

localIP     = "127.0.0.1"
localPort   = 20001
bufferSize  = 1024
msgFromServer       = "Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

#creating a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#binding to address and IP
UDPServerSocket.bind((localIP, localPort))

# Set a timeout on the socket
UDPServerSocket.settimeout(1)

print("UDP server up and listening")

#signal handler for graceful shutdown
def signal_handler(_sig, _frame):
    print("\nShutdown signal received. Shutting down server...")
    UDPServerSocket.close()
    sys.exit(0)

#registering signal from user (i.e ctrl + c)
signal.signal(signal.SIGINT, signal_handler)

#listening for incoming datagrams from client
while True:
    try:
        #wait for data with a timeout
        bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        clientMsg = "Message from Client: {}".format(message.decode())
        clientIP  = "Client IP Address: {}".format(address)
        
        print(clientMsg)
        print(clientIP)

        #sending a reply back to client
        UDPServerSocket.sendto(bytesToSend, address)
        print("Reply sent to client: {}".format(msgFromServer))

    except socket.timeout:
        #timeout
        continue

    except KeyboardInterrupt:
        #handling Ctrl+C explicitly
        print("\nKeyboard interrupt received. Shutting down server...")
        UDPServerSocket.close()
        sys.exit(0)