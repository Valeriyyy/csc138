#this server is for udp
import os
from socket import *

serverPort = 12001
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print ("the server is ready to recieve")
while 1:
	message, clientAddress = serverSocket.recvfrom(2048)
	modifiedMessage = message.decode().upper()
	serverSocket.sendto(modifiedMessage.encode(), clientAddress)

#nums = range(2,50)
#for i in range(2,8): nums = filter(lambda x: x == i or x % i, nums)

#make the server run first
#print nums


