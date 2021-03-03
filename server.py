import socket
import threading

connections = []

class Client(threading.Thread):
    def __init__(self, socket, id, address):
        threading.Thread.__init__(self)
        self.socket = socket
        self.id = id
        self.address = address

    def run(self):
        while True:
            try:
                data = self.socket.recv(1024)
            except:
                print("Client at " + str(self.address) + " has disconnected")
                connections.remove(self)
                break
            if data != "":
                message = "Client at " + str(self.address) + ": " + str(data.decode("utf-8"))
                print(message)
                for connection in connections:
                    if connection.id != self.id:
                        connection.socket.sendall(str.encode(message))
        
def Server(s):
    id = 0
    while True:
        client, address = s.accept()
        connections.append(Client(client, id, address))
        print("Client at " + str(address) + " has connected")
        connections[len(connections) - 1].start()
        id += 1

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
s.bind((host, port))
s.listen(5)
ServerThread = threading.Thread(target= Server, args= (s,))
ServerThread.start()