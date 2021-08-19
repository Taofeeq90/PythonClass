import socket 
import sys
rmip = input("Enter ip address of the host to scan:") 
#portlist =[21,22,23,25,80,443,445,139,53,3389,8080,8888]
st1 = int(input("Enter the Starting port Number ")) 
en1 = int(input("Enter the Last port Number "))
en1=en1+1
for port in range (st1,en1):  
    sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
    result = sock.connect_ex((rmip,port)) 
    if result == 0:
        print (port,":", "--> is open" + "\n" +"   " + "Service: " + socket.getservbyport(port)) 
    else:
        print (port,":", "--> is closed" ) 
   
    sock.close()
