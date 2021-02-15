import sys
from PyQt5 import QtWidgets, uic

from bib import *

class MainWindow(QtWidgets.QMainWindow):
    
    def __init__(self):
        super().__init__()
        uic.loadUi('init.ui', self)

        self.init_widgets()
        
        self.show()
    
    def init_widgets(self):
        pass



if __name__ == '__main__':
   app = QtWidgets.QApplication(sys.argv)
   d = MainWindow()
   app.exec_()