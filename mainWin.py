import sys
from PyQt5 import QtWidgets
from ChatWindow import Ui_ChatWindow



class App(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(App,self).__init__()
        self.ui = Ui_ChatWindow()
        self.ui.setupUi(self)


def app():
    app = QtWidgets.QApplication(sys.argv)
    win = App()    
    win.show()
    sys.exit(app.exec_())
    
    
app()