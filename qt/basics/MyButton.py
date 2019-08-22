import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QtWidgets.QMainWindow):

    def __init__(self):
        super(Window, self).__init__()
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle("Learn Qt")
        self.setWindowIcon(QtGui.QIcon("python logo.png"))


app = QtWidgets.QApplication([])
window = Window()
window.show()
sys.exit(app.exec())
