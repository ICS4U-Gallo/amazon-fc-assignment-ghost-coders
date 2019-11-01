from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class GUI_4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Amazon FC")
        MainWindow.setWindowTitle("Amazon FC")
        MainWindow.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(210, 190, 701, 211))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("Send TO Packaging")
        MainWindow.setCentralWidget(self.centralwidget)
     

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "TO PACKAGING"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
