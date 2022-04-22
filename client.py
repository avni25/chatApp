import socket
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from regex import R
from clientWin import Ui_clientWindow
from datetime import datetime


PORT = 5005
# SERVER = "192.168.56.1"
SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket()


class Worker(QThread):
    update_signal = pyqtSignal(str)
    def run(self):
        while True:
            try:
                msg = client.recv(1024).decode("utf-8")
                self.update_signal.emit(msg)
            except Exception as e:
                print(f"[!] Error: {e}")
                break
                      

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_clientWindow()
        self.ui.setupUi(self)
        self.ui.btn_client_send.clicked.connect(self.run)
        self.ui.btn_client_connect.clicked.connect(self.connect)
        self.nickName = "Client"
        self.chatBoxText = ""
        self.worker = Worker()
        self.worker.update_signal.connect(self.listen_for_messages)
        
    def connect(self):
        n = self.ui.lineEdit_nickName.text()
        print(len(n))
        if len(n)>0:
            self.nickName = n
            client.connect(ADDR)
            self.worker.start()
            print(self.nickName)
    
    
            
    def listen_for_messages(self, msg):        
        try: 
            r = self.chatBoxText+"\n"
            self.chatBoxText =  r +" "+ msg + "\n"
            self.ui.textEdit.setText(self.chatBoxText)
            self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())
            print(f"{msg}") 
        except Exception as e:
            print("Error: ", e)
          
    def send(self, msg): 
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg_row = "["+now+"] "+self.nickName + ": " + msg      
        client.send(msg_row.encode("utf-8"))
         

    def run(self):
        q = self.ui.lineEdit_2.text()
        try:
            self.send(q)
        except:
            print("Error")    
        self.ui.lineEdit_2.setText("")
        print(q)




def run():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()    
    sys.exit(app.exec_())
    

if __name__ == "__main__":
    run()



