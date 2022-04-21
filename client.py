import socket
import threading
import sys
from PyQt5 import QtWidgets
from clientWin import Ui_clientWindow

PORT = 5005
# SERVER = "192.168.56.1"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket()
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
            
    def listen_for_messages(self):
        print("listening")
        while True:
            try:
                message = client.recv(1024).decode("utf-8")
                if message == "":
                    break
                r = self.chatBoxText+"\n"
                self.chatBoxText = r +" "+ message + "\n"
                self.ui.textEdit.setText(self.chatBoxText)
                print(f"{message}") 
            except Exception as e:
                print("Error: ", e)
          
    def send(self, msg): 
               
        client.send(msg.encode("utf-8"))
        try:
            message = client.recv(1024).decode("utf-8")
        except Exception as e:
            print("Error: ", e)
        else:
            r = self.chatBoxText+"\n"
            self.chatBoxText = r +" "+ message + "\n"
            self.ui.textEdit.setText(self.chatBoxText)
            print(f"{message}")  

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


