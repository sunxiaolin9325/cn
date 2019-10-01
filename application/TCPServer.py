from socket import *
serverPort = 12001
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024).decode()
	modifiedSentence = sentence.upper()
	connectionSocket.send(modifiedSentence.encode())
	connectionSocket.close()
