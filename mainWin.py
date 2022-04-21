import sys
from PyQt5 import QtWidgets
from ChatWindow import Ui_ChatWindow
import threading
from server import start_thread



class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)
        self.ui.btn_connect.clicked.connect(self.startServer)
        self.ui.btn_joinRoom.clicked.connect(self.joinRoom)
        self.ui.btn_send.clicked.connect(self.send)
        self.chatBoxText = ""
        
    def startServer(self):
        print("create room")        
        start_thread()
        
    
    def joinRoom(self):
        print("join room")
        
    def send(self):
        q = self.ui.lineEdit_text.text()
        self.chatBoxText += q + "\n"        
        self.ui.textEdit_chatBox.setText(self.chatBoxText)
        self.ui.lineEdit_text.setText("")
  
    
def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())
    
thread_app = threading.Thread(target=app)    
thread_app.start()