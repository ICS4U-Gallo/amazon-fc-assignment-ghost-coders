from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class GUI_box_type(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Amazon FC")
        MainWindow.setWindowTitle("Amazon FC")
        MainWindow.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 200, 241, 211))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(250, 450, 641, 131))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(790, 200, 241, 211))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(460, 200, 241, 211))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 50, 531, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Small Box"))
        self.pushButton_5.setText(_translate("MainWindow", "Fragile"))
        self.pushButton_2.setText(_translate("MainWindow", "Large Box"))
        self.pushButton_3.setText(_translate("MainWindow", "Medium Box"))
        self.label.setText(_translate("MainWindow", "Select Box Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_box_type()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())