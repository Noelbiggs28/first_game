import socket
from _thread import *
from player import Player
import pickle
import os
from dotenv import load_dotenv


# Gets ip address and port from .env file
load_dotenv()
IP = os.getenv("IPADD")
PORT = int(os.getenv("PORT"))
server = IP
port = PORT


# starts a server from ipadress and socket and listens for 2 people to join
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


# creates 2 players with x, y, width, height, color
# stores player info in players
players = [Player(0,0,50,50,(255,0,0)), Player(100,100, 50,50, (0,0,255))]



def threaded_client(conn, player):
    # sends player info 
    conn.send(pickle.dumps(players[player]))
    # creates variable to store stuff in
    reply = ""
    # continuously trys to receive data from client
    while True:
        try:
            # recieves data from client
            data = pickle.loads(conn.recv(2048))
            # updates server with information from client
            players[player] = data
            # if it was unable to recieve info print disconnected
            if not data:
                print("Disconnected")
                break
            # send to client info on the other player
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(pickle.dumps(reply))
    # if anything goes wrong. break the loop and close the connections
        except:
            break

    print("Lost connection")
    conn.close()

# sets currentplayer to 0 
currentPlayer = 0
# continuously listens for new people to connect
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)
    # once connected creates a thread
    start_new_thread(threaded_client, (conn, currentPlayer))
    # updates currentplayer so next person is next player
    currentPlayer += 1