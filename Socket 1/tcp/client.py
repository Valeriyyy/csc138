#This client is for tcp
from socket import *

serverName = 'localhost' #'130.86.66.66'
serverPort = 13001
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
sentence  = input('input lowercase sentence: ')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024).decode()#utf-8
print ('from server: ', modifiedSentence)
clientSocket.close()
