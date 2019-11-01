from PyQt5 import QtCore, QtGui, QtWidgets
import json

class GUI_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 180, 411, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(190, 30, 791, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(30)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Enter = QtWidgets.QPushButton(self.centralwidget)
        self.Enter.setGeometry(QtCore.QRect(500, 310, 201, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(30)
        self.Enter.setFont(font)
        self.Enter.setObjectName("Enter")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter the Barcode that will go to the bin"))
        self.Enter.setText(_translate("MainWindow", "Enter"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())