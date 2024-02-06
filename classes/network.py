import socket
import os
from dotenv import load_dotenv


load_dotenv()

IP = os.getenv("IPADD")
PORT = int(os.getenv("PORT"))
class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IP
        self.port = PORT
        self.addr = (self.server, self.port)
        self.pos = self.connect()
        
       
    def getPos(self):
        return self.pos
    
    def read_pos(self, str):
        str = str.split(",")
        return float(str[0]), float(str[1])

    def make_pos(self,tup):
        return str(tup[0]) + "," + str(tup[1])

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)
