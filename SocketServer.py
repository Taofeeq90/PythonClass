import socket 
#import datetime
import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end = "\r")
        time.sleep(1)
        t -= 1
t = 30
#countdown(t)

def SocketServer():
 
    host = input ("Enter the server IP addresss:" )
    print ("The server hostname is:" + socket.gethostname() + ":" + socket.gethostbyname(socket.gethostname()))

    port= 8888
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    try:
        s.bind((host, port))

        s.listen (2)
        
        
        s.settimeout(t)
        
        print(""" ***********************************************************
  This Server will timeout if no client connect in 30 seconds
 ************************************************************""")
        countdown(t)
        
        socket.gethostname()
        
        conn, addr = s.accept()
 
        print(addr, "connectiom is establish")

        conn.send("Hello Client!".encode())

        conn.close()

    except socket.timeout:

        print("client not connected!")

        s.close
        
SocketServer()