import socket
import threading
import firebase_admin
from firebase_admin import credentials, firestore
from pprint import pprint
import re
import json
import time
from datetime import datetime


#---------------- FIREBASE CONFIGS---------------------------------

COLLECTION_MSG = "messages"
COLLECTION_USERS = "users"

cred = credentials.Certificate("config.json")
firebase_admin.initialize_app(cred)

db = firebase_admin.firestore.client()

def add(collection_name, data):
    db.collection(collection_name).add(data)
    
def read(collection_name):
    arr =[]
    l = db.collection(collection_name).order_by("time").stream()
    for doc in l:
        arr.append(doc.to_dict())
    return arr

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

def convertTimestampToDateTime(ts):
    s = int(str(ts).split(".")[0])
    return datetime.utcfromtimestamp(s).strftime('%Y-%m-%d %H:%M:%S')
   
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(addr[1])    
    arr = read(COLLECTION_MSG)
    s1=""
    for data in arr:
        s1 = "["+convertTimestampToDateTime(data["time"])+"] "+data["user"]+": "+data["msg"]
        # conn.send(str.encode(str(data)+"\n"))
        conn.send(str.encode(s1))
        time.sleep(0.02)
        
    while True: 
        try:
            msg = conn.recv(1024) ##.decode("utf-8")
            s = "".join(map(chr, msg))
            data = json.loads(s)
            s2 = "["+convertTimestampToDateTime(data["time"])+"] "+data["user"]+": "+data["msg"]
            print(s2)            
            add(COLLECTION_MSG, {"msg":data["msg"], "time": float(data["time"]), "user": data["user"]})
        except Exception as e:
            print(f"[!] Error: {e}")      
            clients.remove(conn)
                    
        broadcast(str.encode(s2))
    
    
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
        pprint(read(COLLECTION_MSG))

start()


