import threading
import time
import socket, subprocess,sys 
from datetime import datetime
import thread 
import shelve

"""
First use subprocess.call()statement to clear the screen
second line use to create database with taofeeq.ib file
Third line use to port to be stored in the database file

"""
subprocess.call('clear',shell=True)
shelf = shelve.open("taofeeq.ib") 
data=(shelf['desc'])

"""
Handle the thread inheritance 
"""

class myThread (threading.Thread):
    def __init__(self, threadName,rmip,r1,r2,c):      # function holds 5 values
        threading.Thread.__init__(self)               # thread method call
        self.threadName = threadName                  # store thread name
        self.rmip = rmip                              # remote IP address
        self.r1 = r1                                  # holds first port range
        self.r2 = r2                                  # holds the last port range
        self.c =c                                     # holds the connction mode
		
    def run(self):                                                     # function run
        scantcp(self.threadName,self.rmip,self.r1,self.r2,self.c)      # scantcp method with defined above

"""
Connection and port scanning handling 
"""

def scantcp(threadName,rmip,r1,r2,c):                                                  # scantcp function is called from run above
        try:                                                                               # try is used to handle errors
            for port in range(r1,r2):                                                      # loop the range r1-r2
                sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)                         # create TCP socket
                #sock= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)                         # create UDP socket 
                socket.setdefaulttimeout(c)                                                    # set the timeout
                result = sock.connect_ex((rmip,port))                                          # handle port scanning with result 0 means the port is open and errcode means is closed
                if result==0: 
                    print( "Port Open:---->\t", port,"--", data.get(port, "Not in Database") )   # check for port in the dictionary database     
                    sock.close()
			
        except KeyboardInterrupt:                                                          # Keyboard Interrupt error handling
            print( "You stop this " )     
            sys.exit()

        except socket.gaierror:                                                            # invalid host error handling
            print ("Hostname could not be resolved" )     
            sys.exit()

        except socket.error:                                                               # Connection problem error handling     
            print( "could not connect to server" )     
            sys.exit()
        shelf.close() 

"""
Collection of the required data from the users
"""
print("*"*60) 
print(" \tWelcome this is the Port scanner of Mohit\n  ")

d= input("\ t Press D for Domain Name or Press I for IP Address\t")   
if (d=='D' or d=='d'):
    rmserver = input("\t Enter the Domain Name to scan:\t")
    rmip = socket.gethostbyname(rmserver)
	
elif(d=='I' or d=='i'):  
    rmip = input("\t Enter the IP Address  to scan:  ")
	
else:  
    print("Wrong input" 
	#rmip = socket.gethostbyname(rmserver))
    r11 = int(input("\t Enter the start port number\t")) 
    r21 = int (input("\t Enter the last port number\t"))

    conect=raw_input("For low connectivity press L and High connectivity Press H\t")

    if (conect=='L' or conect=='l'):  
        c =1.5

    elif(conect =='H' or conect=='h'):  
        c=0.5

    else:  
        print( "\t wrong Input")

    print("\n Mohit's Scanner is working on ",rmip)

    print "*"*60 

    t1= datetime.now()
    tp=r21-r11

    tn =30                                           # tn number of port handled by one thread 
    tnum=tp/tn                                       # tnum number of threads
 
    if (tp%tn != 0):  
        tnum= tnum+1

    if (tnum > 300): 
        tn = tp/300
        tn= tn+1
        tnum=tp/tn  
        if (tp%tn != 0):    
            tnum= tnum+1

"""
Thread for the scanning
"""
    threads= []

    try:  
        for i in range(tnum):
            #print("i is ",i)   
            k=i 
            r2=r11+tn     
            # thread=str(i)    
            thread = myThread("T1",rmip,r11,r2,c)
            thread.start() 
        threads.append(thread)  
        r11=r2
	
    except:  
        print("Error: unable to start thread")
	
    print( "\t Number of Threads active:", threading.activeCount())
	
    for t in threads:
        t.join() 
	
    print( "Exiting Main Thread")
    t2= datetime.now()

    total =t2-t1 
    print("scanning complete in " , total)