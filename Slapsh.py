import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from Tools.demo.sortvisu import steps


class Ui_Slapsh(object):
    def setupUi(self, Slapsh):
        Slapsh.setObjectName("Slapsh")
        Slapsh.resize(758, 416)
        Slapsh.setStyleSheet("border-radius:14px;")
        self.centralwidget = QtWidgets.QWidget(Slapsh)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background-color: rgb(85, 170, 255);\n"
"color: rgb(255, 255, 255);\n"
"border-radius:10px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 30, 711, 81))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.progressBar = QtWidgets.QProgressBar(self.frame)
        self.progressBar.setGeometry(QtCore.QRect(30, 310, 671, 31))
        self.progressBar.setStyleSheet("QProgressBar\n"
"{\n"
"border: solid grey;\n"
"border-radius: 10px;\n"
"color: black;\n"
"   background-color: rgb(255, 255, 255);\n"
"}\n"
"QProgressBar::chunk \n"
"{\n"
"background-color: #ff0000;\n"
"border-radius :10px;\n"
"}   ")
        maxt=100;
        self.progressBar.setProperty("value", 5)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setMaximum(maxt)
        self.progressBar.setMaximum(0)
        for i in range(maxt):
            time.sleep(0.01)
            self.progressBar.setValue(i+1)

        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(34, 360, 661, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 711, 41))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.frame)
        Slapsh.setCentralWidget(self.centralwidget)

        self.retranslateUi(Slapsh)
        QtCore.QMetaObject.connectSlotsByName(Slapsh)

    def retranslateUi(self, Slapsh):
        _translate = QtCore.QCoreApplication.translate
        Slapsh.setWindowTitle(_translate("Slapsh", "Loan"))
        self.label.setText(_translate("Slapsh", "Welcome"))
        self.label_3.setText(_translate("Slapsh", "Starting....."))
        self.label_2.setText(_translate("Slapsh", "Loan Mangement Application"))


