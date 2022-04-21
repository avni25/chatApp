import socket
import threading
import sys
from PyQt5 import QtWidgets
from clientWin import Ui_clientWindow

PORT = 5050
# SERVER = "192.168.56.1"
SERVER = "192.168.56.1"
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(ADDR)
# nickName = input("Enter your name: ")

# def send(msg):
#         client.send(msg.encode("utf-8"))
#         response = client.recv(1024).decode("utf-8")
#         print(f"{response}")

# while True:
#     text = input("Text: ")    
#     send(nickName+": "+text)


class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_clientWindow()
        self.ui.setupUi(self)
        self.ui.btn_client_send.clicked.connect(self.run)
        self.ui.btn_client_connect.clicked.connect(self.connect)
        self.nickName = "Client"
        self.chatBoxText = ""
        
        
    def connect(self):
        n = self.ui.lineEdit_nickName.text()
        print(len(n))
        if len(n)>0:
            self.nickName = n
            client.connect(ADDR) 
            print(self.nickName)
            
                
    def send(self, msg):
        client.send(msg.encode("utf-8"))
        response = client.recv(1024).decode("utf-8")
        r = self.chatBoxText
        self.chatBoxText = r + response + "\n"
        self.ui.textEdit.setText(self.chatBoxText)
        print(f"{response}")

    def run(self):
        q = self.ui.lineEdit_2.text()
        try:
            self.send(q)
        except:
            print("Error")    
        self.ui.lineEdit_2.setText("")
        print(q)

def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())
    
# thread_app = threading.Thread(target=app)    
# thread_app.start()
app()


