import socket

# Create a UDP socket (SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Define target server address and port
server_address = ("103.37.201.135", 1337)
# server_address = ("127.0.0.1", 1337)
message = b"Hello UDP Server"
print(message)

while(1): 
    s.sendto(message, server_address)
# Send the datagram
s.close()
