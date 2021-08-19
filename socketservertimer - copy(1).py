import socket
import threading
import time
class SocketServer():
    def __init__(self):
        self.t=30
        self.adr=""
        print("""******************************************************************
    This Server will timeout if no client connect in 30 seconds
*******************************************************************""")
        #let's create a new thread for out server
        # in the main thread, we will print and count seconds....
        self.thread=threading.Thread(target=self.thread)
        self.thread.daemon=True
        self.thread.start()
        self.counter()

    def thread(self):
        HOST = '127.0.0.1'  # The server's hostname or IP address
        PORT = 8888  # The port used by the server
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((HOST, PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print('Connected by', addr)
                #we want to know if someone is connected
                #by set self.adr with something that has len>0 we will informe the main thread that it needs to stop
                self.adr="Connected"
                print ("The client hostname is:" + socket.gethostname() + "\n"+ "The client IP addressis:" + socket.gethostbyname(socket.gethostname()) + "\n"+ "The client machine name is:" +  socket.getfqdn())
                #print(addr.count)
                conn.send("Hello Client!".encode())
                s.close() #if you want to close, or leave it to further connections
    def counter(self):
        for x in range(self.t + 1):
            time.sleep(1)#sleep function
            if (len(self.adr)!=0): #every time we chech if sel.adr is different from 0
                print("Connection is established")
                print("Connected after 00:{:02d}".format(x))
                break #stop
                
            else:
                mins, secs = divmod(self.t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end = "\r")
                self.t -= 1
                #print ('00:{:02d}'.format(x))
               
        print("client not connected!")

#host = raw_input("Enter the server IP addresss:")
SocketServer()