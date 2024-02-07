import socket
import pickle

import os
from dotenv import load_dotenv



class Network:
    def __init__(self):
        load_dotenv()
        IP = os.getenv("IPADD")
        PORT = int(os.getenv("PORT"))

        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = IP
        self.port = PORT
        self.addr = (self.server, self.port)
        self.p = self.connect()


    # gets player from server and returns it to client
    def getP(self):
        return self.p


    # connects to server and returns player info
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    # sends data to be which is your player object.
    # returns data on other player object
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)