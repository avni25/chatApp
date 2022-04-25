import socket
import threading


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
        client.send(msg.encode("utf-8"))
        
   
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    print(addr[1])    
    
    while True: 
        try:
            msg = conn.recv(1024).decode("utf-8")
            print(f"[{addr}] {msg}")
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


