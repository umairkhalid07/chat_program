import socket
import threading

host = 'localhost'
port = 5000
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((host, port))

name = input('Enter your name : ')
c.send(name.encode())

def Sending_MSG_Thread(c):
    while True:
        msg = input("")
        message = name + ' : ' + msg 
        c.send(message.encode())

def Recieving_MSG_Thread(c):
    while True:
        try:
            message = c.recv(1024).decode()
            print(message)
        except:
            c.close()
            break

threading.Thread(target= Sending_MSG_Thread, args= (c,) ).start()
threading.Thread(target= Recieving_MSG_Thread, args= (c,) ).start()
