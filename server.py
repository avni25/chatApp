import socket
import threading


PORT = 5050
# SERVER = "192.168.56.1"
SERVER = socket.gethostbyname(socket.gethostname())
print(SERVER)
ADDR = (SERVER, PORT)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    while True:        
        msg = conn.recv(1024).decode("utf-8")
        if not msg:
            break
        print(f"[{addr}] {msg}")
        conn.send(msg.encode("utf-8"))
    conn.close()

def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

print(f"[LISTENING] Server is listening on {SERVER}")
start()




