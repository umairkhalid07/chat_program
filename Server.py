import socket
import threading

host = 'localhost'
port = 5000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen()
clients = {}

def Client_Thread_Start(conn):
    while True:
        try:
            message = conn.recv(1024)
            for client in clients:
                client.send(message)
        except:
            conn.close()
            del clients[conn]
            for client in clients:
                if client != conn:
                    message = name + ' has left the room'
                    client.send(message.encode())
            break

while True:
    print('Chat Room')
    conn, addr = s.accept()
    name = conn.recv(1024)
    name = name.decode()
    clients[conn] = name

    for client in clients:
        if client != conn:
            print('/n')
            message = name + ' has entered the chat'
            client.send(message.encode())

    threading.Thread(target = Client_Thread_Start, args= (conn, )).start()
