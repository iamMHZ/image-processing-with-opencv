# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OpenCameraView.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(643, 499)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.openCameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openCameraBtn.setGeometry(QtCore.QRect(480, 110, 101, 51))
        self.openCameraBtn.setObjectName("openCameraBtn")
        self.closeCamera = QtWidgets.QPushButton(self.centralwidget)
        self.closeCamera.setGeometry(QtCore.QRect(480, 190, 101, 51))
        self.closeCamera.setObjectName("closeCamera")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(34, 35, 321, 231))
        self.label.setText("")
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 643, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.openCameraBtn.clicked.connect(self.on_click)
        self.closeCamera.clicked.connect(self.on_click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def on_click(self):
        print("Button clicked")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.openCameraBtn.setText(_translate("MainWindow", "open camera"))
        self.closeCamera.setText(_translate("MainWindow", "close camera"))
