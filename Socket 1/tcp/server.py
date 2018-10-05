#This server is for tcp
from socket import *
serverPort = 13001 #use soemthing different than the udp code
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ("the server is ready to recieve")
while 1:
	connectionSocket, addr = serverSocket.accept()

	sentence = connectionSocket.recv(1024).decode()
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence.encode())
	connectionSocket.close()
