#!/usr/bin/python
# -*- coding: utf-8 -*-

from socket import *
#serverName = '127.0.0.1'
serverName = '192.168.0.100'
serverPort = 62078
clientSocket = socket(AF_INET, SOCK_STREAM)
# 3次握手
# 若服务端没有运行，会以第二次握手（服务端发送包含RST的标志位的分组）结束
clientSocket.connect((serverName, serverPort))
sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
print('From Server: ', modifiedSentence.decode())
#print(modifiedSentence.decode())
# 链接的关闭实际上由server端先发起，在server端调用send后，就调用了close
# 4次挥手（可能只需3次）
clientSocket.close()

# 在客户端程序已经退出时，服务端再调用close，会收到RST分组

