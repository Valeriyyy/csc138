from socket import *
import ssl
import base64
import os
import sys


msg = "\r\n I love computer netowrks"
endmsg = "\r\n.\r\n"

mailserver = 'smtp.csus.edu'
serverPort = 587
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver,serverPort))
recv = clientSocket.recv(1024)
print(recv)
if recv[:3] != "220" :
    print("220 Reply not received from server")

#send HELO command and print server response
heloCommand = "HELO csus.edu\r\n"
clientSocket.send(heloCommand)
recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print("250 reply not recieved from server")

mailfrom = "MAIL FROM: <sun@csus.edu> \r\n"
clientSocket.send(mailfrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
if recv2[:3] != "250":
    print("250 reply not received from server")

rcptto = "RCPT TO: <valeriykutsar@csus.edu>\r\n"
clientSocket.send(rcptto)
recv3 = clientSocket.recv(1024)
print(recv3)
if recv3[:3] != "250":
    print("250 reply not recieved from server")

data = "DATA\r\n"
clientSocket.send(data)
recv4 = clientSocket.recv(1024)
print(recv4)
if recv4[:3] != "354":
    print("354 reply not recived from server")

clientSocket.send("SUBJECT: Greetings!")
clientSocket.send("test again")
clientSocket.send(msg)

clientSocket.send(endmsg)
recv5 = clientSocket.recv(1024)
print(recv5)
if recv5[:3] != "250":
    print("250 reply not recieved from server")

quitcommand = "QUIT\r\n"
clientSocket.send(quitcommand)
recv6 = clientSocket.recv(1024)
if recv6[:3] != "221":
    print("221 reply not recieved from server")
clientSocket.close()