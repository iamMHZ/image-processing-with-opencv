import cv2
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap, QImage
from qtWithOpencv.OpenCameraView import Ui_MainWindow
import sys


class MyWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def set_image(self):
        # while True:
        _, frame = cv2.VideoCapture(0).read()
        height, width, bytes_per_component = frame.shape
        bytes_per_line = 3 * width
        cv2.cvtColor(frame, cv2.COLOR_BGR2RGB, frame)
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

        q_pix_map = QPixmap(q_img)
        self.ui.label.setPixmap(q_pix_map)


app = QtWidgets.QApplication([])
app.processEvents()
application = MyWindow()
application.show()
application.set_image()
sys.exit(app.exec())
