import socket
import threading

def Client(s):
    while True:
        try:
            data = s.recv(1024)
        except:
            print("disconnected from server")
            break
        if data != "":
            print(str(data.decode("utf-8")))
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.connect((host, port))
ClientThread = threading.Thread(target=Client, args=(s,))
ClientThread.start()

while True:
    message = input()
    s.sendall(str.encode(message))