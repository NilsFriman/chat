import socket
import threading 


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_host = socket.gethostbyname(socket.gethostname())
server_port = 1234

server_socket.bind(("", server_port))
server_socket.listen()
print("Server is up and running!")


clients = []
users = []
names = []


def message_sender(msg: str):
    for client in clients:
        client["connection"].send(msg)



def handle_active_clients(client):
    available_commands = {"/nick": "fixar resten här senare!",
                          "/admin": "fixar resten här senare!",
                          "/clear": "fixar resten här senare!",
                          }

    while True:
        try:
            msg = client["connection"].recv(1024)


            if msg.decode()[0] == "/":
                print("mogus")
                #available_commands[msg.decode().split()[0]]

            else:
                message_sender(f"{client['name']}: {msg}".encode()) 

        except Exception:
            disconnected_user = client['name']
            clients.remove(client)

            message_sender(f"{disconnected_user} left the room".encode())
            break


def connections():
    try:
        while True:
            client_connection, client_address = server_socket.accept()

            if client_connection not in users:
                user = {"name": "Guest",
                        "ip": client_address[0],
                        "port": client_address[1],
                        "connection": client_connection
                        }

                clients.append(user)
                users.append(user)
                
            message_sender("Guest has entered the chat room".encode())


            thread = threading.Thread(target=handle_active_clients, args=(user,))
            thread.start()

    except Exception:
        pass




connections()
