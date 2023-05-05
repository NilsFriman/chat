import socket
import pickle
import threading 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
server_port = 1234

server_socket.bind(("", server_port))
server_socket.listen()


clients = []
users = []
ipaddresses = []
names = []


def message_sender(msg: str):
    for client in clients:
        client.send(msg)


def connections():
    while True:
        conn, addr = server_socket.accept()

        if conn not in users:
            clients.append(conn)
            ipaddresses.append(addr)

        message_sender("Guest has entered the chat room")
        thread = threading.Thread(target=handle_active_clients, args=(conn,))
        thread.start()


def handle_active_clients(client):
    while True:
        msg = client.recv(1024)
        message_sender(msg.encode())


connections()
