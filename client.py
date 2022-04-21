import socket


PORT = 5050
# SERVER = "192.168.56.1"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    client.send(msg.encode("utf-8"))
    response = client.recv(1024).decode("utf-8")
    print(f"Received: {response}")


while True:
    text = input("Text: ")    
    send(text)
    
    