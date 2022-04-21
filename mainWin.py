import sys
from PyQt5 import QtWidgets
from ChatWindow import Ui_ChatWindow



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
    
    
app()