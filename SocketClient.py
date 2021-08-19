import socket 

host = "127.0.0.1"

port = 8888

ClientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ClientSocket.connect((host, port))

print(ClientSocket.recv(1024).decode(),)

ClientSocket.send("Hello Server".encode())

ClientSocket.close()







