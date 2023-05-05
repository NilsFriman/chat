import socket
import threading 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
server_port = 1234

server_socket.bind(("", server_port))
server_socket.listen()


clients = []
users = []
names = []


def message_sender(msg: str):
    for client in clients:
        client["connection"].send(msg)


def handle_active_clients(client, ip):
    for client in clients:
        if client["ip"] == ip:
            name = client["name"]

    while True:
        msg = client["connection"].recv(1024)
        message_sender(f"{name}: {msg}".encode())


def connections():
    try:
        while True:
            client_connection, client_address = server_socket.accept()

            if client_connection not in users:
                clients.append({"name": "Guest",
                                "ip": client_address[0],
                                "port": client_address[1],
                                "connection": client_connection})

            message_sender("Guest has entered the chat room".encode())
            thread = threading.Thread(target=handle_active_clients, args=(client_connection, client_address[0]))
            thread.start()

    except Exception:
        for client in clients:
            if "ip" == client_address[0]:
                name = client["name"]
        message_sender(f"{name} left the chat".encode())


connections()
