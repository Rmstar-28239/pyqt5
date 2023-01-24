import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from Slapsh import Ui_Slapsh
from Webh import Ui_MainWindow
from Webview import Ui_Webview

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Ui_Webview()
    w = QtWidgets.QMainWindow()
    # w.setWindowFlag(QtCore.Qt.FramelessWindowHint)
    # w.setAttribute(QtCore.Qt.WA_TranslucentBackground)
    ex.setupUi(w)
    w.show()
    sys.exit(app.exec_())
