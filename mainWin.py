import sys
from PyQt5 import QtWidgets
from ChatWindow import Ui_ChatWindow
from server import start


# PORT = 5050
# # SERVER = "192.168.56.1"
# SERVER = socket.gethostbyname(socket.gethostname())
# print(SERVER)
# ADDR = (SERVER, PORT)
# server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server.bind(ADDR)


class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)
        self.ui.btn_createRoom.clicked.connect(self.createRoom)
        self.ui.btn_joinRoom.clicked.connect(self.joinRoom)
        self.ui.btn_send.clicked.connect(self.send)
        self.chatBoxText = ""
        
    def createRoom(self):
        print("create room")
        start()
    
    def joinRoom(self):
        print("join room")
        
    def send(self):
        q = self.ui.lineEdit_text.text()
        self.chatBoxText += q + "\n"
        self.ui.textEdit_chatBox.setText(self.chatBoxText)
        self.ui.lineEdit_text.setText("")
    
    # def handle_client(self, conn, addr):
    #     print(f"[NEW CONNECTION] {addr} connected.")
    #     while True:        
    #         msg = conn.recv(1024).decode("utf-8")
    #         if not msg:
    #             break
    #         print(f"[{addr}] {msg}")
    #         conn.send(msg.encode("utf-8"))        
    #     conn.close()

    # def start(self):
    #     server.listen()
    #     print(f"[LISTENING] Server is listening on {SERVER}")
    #     while True:
    #         conn, addr = server.accept()
    #         thread = threading.Thread(target= self.handle_client, args=(conn, addr))
    #         thread.start()
    #         print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")




def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())
    
    
app()