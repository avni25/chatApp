import socket
import sys
from winreg import QueryInfoKey
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from regex import R
from clientWin import Ui_clientWindow
from datetime import datetime
from PIL import Image
import json
import time

PORT = 5005
SERVER = "192.168.56.1"
# SERVER = "127.0.0.1"
ADDR = (SERVER, PORT)
# client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client = socket.socket()
fileDialog_default_dir = "c:\\Users\\Avni\\Desktop"

class Worker(QThread):
    update_signal = pyqtSignal(str)    
    def run(self):
        while True:
            arr = []
            try:
                msg = client.recv(1024).decode("utf-8")
                if(msg !=""):
                    arr.append(msg)
                while len(arr)>0:
                    self.update_signal.emit(arr[0])
                    arr.pop(0)
            except Exception as e:
                print(f"[!] Error: {e}")
                break
                      

class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_clientWindow()
        self.ui.setupUi(self)
        self.ui.btn_client_send.clicked.connect(self.run)
        self.ui.btn_send_img.clicked.connect(self.sendImg)
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
    
    def sendImg(self):
        fileName = QFileDialog.getOpenFileName(self,
    "Open Image", fileDialog_default_dir, "Image Files (*.png *.jpg)")
        print(fileName)        
        self.ui.textEdit.insertHtml("<img src='"+fileName[0]+"' width='100' height='100'> <br>")
        # file = open(fileName[0], "rb")
        # client.sendFile(file, 1024)
        # img_data = file.read(1024)
        # print(img_data)
        # while img_data:
        #     client.send(img_data)
        #     img_data = file.read(1024)
        # file.close()
        print("Image sent")
        
        
    def listen_for_messages(self, msg):        
        try: 
            r = self.chatBoxText+"\n"
            
            self.chatBoxText =  r +" "+ msg + "\n"
            # self.ui.textEdit.setText(self.chatBoxText)
            self.ui.textEdit.insertHtml(msg+"<br>")
            self.ui.textEdit.verticalScrollBar().setValue(self.ui.textEdit.verticalScrollBar().maximum())
            print(f"{msg}") 
        except Exception as e:
            print("Error: ", e)
          
    def send(self, msg): 
        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        timestamp = time.time()
        # msg_row = "["+now+"] "+self.nickName + ": " + msg  
        obj = '{"time": "'+str(timestamp)+'", "user": "'+self.nickName+'", "msg": "'+msg+'" }'    
        client.send(obj.encode("utf-8"))
         

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



