import socket



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("10.158.18.101", 1234))




while True:
    msg = s.recv(1024)
    print(msg.decode())

print("logus")