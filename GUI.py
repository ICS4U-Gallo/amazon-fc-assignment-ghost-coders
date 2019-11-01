from PyQt5 import QtCore, QtGui, QtWidgets
from main import *

class GUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Amazon FC")
        MainWindow.setWindowTitle("Amazon FC")
        MainWindow.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 200, 481, 51))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 0, 711, 191))
        font = QtGui.QFont()
        font.setFamily("Sitka Heading")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(160, 310, 261, 81))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(28)
        self.Enter.setFont(font)
        self.Enter.setObjectName("Enter")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(680, 40, 411, 561))
        self.listView.setObjectName("listView")
        self.cont = QtWidgets.QPushButton(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(150, 470, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(28)
        self.cont.setFont(font)
        self.cont.setObjectName("Continue")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        

    def enter_click(self):
            pass
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please Enter Product Barcode"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.cont.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())