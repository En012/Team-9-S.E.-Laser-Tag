import socket

msgFromClient       = "Hello UDP Server"
bytesToSend         = str.encode(msgFromClient)
serverAddressPort   = ("127.0.0.1", 20001) # port changed from gitexample
bufferSize          = 1024

#creating a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#seting a timeout for the socket
UDPClientSocket.settimeout(5)

try:
    #send to server using created UDP socket
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Message sent to server.")

    #receiving response from server
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    msg = "Message from Server: {}".format(msgFromServer[0].decode())
    print(msg)

except ConnectionResetError:
    print("Connection was reset by the remote host.")
except socket.timeout:
    print("No response from server within the timeout period.")
except Exception as e:
    print("An error occurred: {}".format(e))
finally:
    #closing socket
    UDPClientSocket.close()