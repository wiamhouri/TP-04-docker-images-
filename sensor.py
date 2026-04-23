import time
import socket

host = "server"
port = 5000

while True:
    try:
        s = socket.socket()
        s.connect((host, port))
        message = "Temperature: 30"
        s.send(message.encode())
        s.close()
        time.sleep(3)
    except:
        time.sleep(3)