
from socket import *
import keyboard
HOST = '192.168.1.20' #  or 'localhost'
PORT = 85
BUFSIZ = 1024
ADDR=(HOST,PORT)
tcpCliSock = socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
while True:
    if keyboard.is_pressed('z'):
        data = "z"
        print('data=',data);
        tcpCliSock.send(data.encode())
    elif keyboard.is_pressed('q'):
        data = "q"
        print('data=',data);
        tcpCliSock.send(data.encode())
    elif keyboard.is_pressed('d'):
        data = "d"
        print('data=',data);
        tcpCliSock.send(data.encode())
    elif keyboard.is_pressed('s'):
        data = "s"
        print('data=',data);
        tcpCliSock.send(data.encode())

        

 