import socket

ServerPort = input ("Enter the port number:")

while ServerPort is int: 
    s = socket.getservbyport(ServerPort)

    print (s)
    
else: 
    s = socket.getservbyname(ServerPort)
    
    print(s)
    
