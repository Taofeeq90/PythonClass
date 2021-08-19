import socket 
import time


 
host = "127.0.0.1"
port= 8888
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))

    s.listen (2)
    # def countdown(t):
        # while t:
            # mins, secs = divmod(t, 60)
            # timer = '{:02d}:{:02d}'.format(mins, secs)
            # print(timer, end = "\r")
            # time.sleep(1)
            # t -= 1
    # countdown(30)
    s.settimeout(30)
    print(s.settimeout)

    conn, addr = s.accept()
 
    print(addr, "connectiom is establish")

    conn.send("Hello Client!".encode())

    conn.close()

except socket.timeout:

    print("client not connected!")

    s.close
        
