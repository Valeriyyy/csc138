#This client is for udp

from socket import *

serverName = 'localhost' #130.86.66.66' #ip
serverPort = 12001
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input("input lowercase sentence: ")
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print ('modified message: ' ,  modifiedMessage.decode())
clientSocket.close()
