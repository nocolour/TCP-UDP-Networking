import socket

# Create socket for server
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
print("Do Ctrl+c to exit the program !!")

# Let's send data through UDP protocol
while True:
    send_data = input("Type some text to send =>");
    s.sendto(send_data.encode('utf-8'), ("10.100.100.118", 3333))
    print("\n\n 1. Client Sent : ", send_data, "\n\n")
#    data, address = s.recvfrom(4096)
#    print("\n\n 2. Client received : ", data.decode('utf-8'), "\n\n")
# close the socket
s.close()
