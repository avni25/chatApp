import socket
import threading


PORT = 5050
# SERVER = "192.168.56.1"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
server.listen(10)

clients =[]

def broadcast(msg, conn):
    for client in clients:
        if client != conn:
            try:
                client.send(msg.encode("utf-8"))
            except:
                client.close()
                clients.remove(client)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(addr[1])    
    clients.append(conn)
    while True: 
        try:
            msg = conn.recv(1024).decode("utf-8")
            if msg:
                print(f"[{addr}] {msg}")

                broadcast(msg, conn)        
            else:
                clients.remove(conn)
        except:
            continue
    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def start_thread():
    t2 = threading.Thread(target=start)
    t2.start()

start()


