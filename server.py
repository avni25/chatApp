import socket
import threading
import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
import re
import json


#---------------- FIREBASE CONFIGS---------------------------------

COLLECTION_MSG = "messages"
COLLECTION_USERS = "users"

cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()

def add(collection_name, data):
    db.collection(collection_name).add(data)
    
def read(collection_name):
    return db.collection(collection_name).get()

#-----------------------------------------------------------------------
regex= "(?<=\[).+?(?=\])"


PORT = 5005
SERVER = "192.168.56.1"
# SERVER = socket.gethostbyname(socket.gethostname())
# SERVER = "0.0.0.0"
print(SERVER)
ADDR = (SERVER, PORT)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)
server.listen(6)

clients =[]

def broadcast(msg):
    for client in clients:        
        client.send(msg) ##.encode("utf-8")
        
   
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(addr[1])    
    # file = open("temp.jpg", "wb")
    # img_data = conn.recv(2048)
    
    while True: 
        try:
            msg = conn.recv(1024) ##.decode("utf-8")
            s = "".join(map(chr, msg))
            data = json.loads(s)
            print(f'{data["time"]}-{data["user"]}-{data["msg"]}')            
            add(COLLECTION_MSG, {"msg":data["msg"], "time": float(data["time"]), "user": data["user"]})
        except Exception as e:
            print(f"[!] Error: {e}")      
            clients.remove(conn)
                    
        broadcast(msg)
    
    
def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        print(f'[+] {addr} connected.')
        clients.append(conn)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        # thread.daemon = True
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")


start()


