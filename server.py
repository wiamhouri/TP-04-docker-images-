import socket

host = "0.0.0.0"
port = 5000

s = socket.socket()
s.bind((host, port))
s.listen(5)

print("Server started...")

while True:
    client, addr = s.accept()
    data = client.recv(1024).decode()
    print("Received:", data)
    client.close()