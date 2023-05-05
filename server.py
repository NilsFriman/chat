import socket
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
        client_connection, client_address = server_socket.accept()

        if client_connection not in users:
            clients.append(client_connection)
            ipaddresses.append(client_address)

        message_sender("Guest has entered the chat room")
        thread = threading.Thread(target=handle_active_clients, args=(client_connection, "VAD SKA VARA HÄR"))
        thread.start()


def handle_active_clients(client):
    while True:
        msg = client.recv(1024)
        message_sender(msg.encode())


connections()
