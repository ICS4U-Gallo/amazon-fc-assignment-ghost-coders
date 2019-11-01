from PyQt5 import QtCore, QtGui, QtWidgets
from main import *


class GUI_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Amazon FC")
        MainWindow.setWindowTitle("Amazon FC")
        MainWindow.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compartment_1 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_1.setGeometry(QtCore.QRect(350, 370, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.compartment_1.setFont(font)
        self.compartment_1.setObjectName("compartment_1")
        self.compartment_2 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_2.setGeometry(QtCore.QRect(490, 370, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_2.setFont(font)
        self.compartment_2.setObjectName("compartment_2")
        self.compartment_3 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_3.setGeometry(QtCore.QRect(630, 370, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_3.setFont(font)
        self.compartment_3.setObjectName("compartment_3")
        self.compartment_6 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_6.setGeometry(QtCore.QRect(350, 500, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_6.setFont(font)
        self.compartment_6.setObjectName("compartment_6")
        self.compartment_5 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_5.setGeometry(QtCore.QRect(910, 370, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_5.setFont(font)
        self.compartment_5.setObjectName("compartment_5")
        self.compartment_4 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_4.setGeometry(QtCore.QRect(770, 370, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_4.setFont(font)
        self.compartment_4.setObjectName("compartment_4")
        self.compartment_8 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_8.setGeometry(QtCore.QRect(630, 500, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_8.setFont(font)
        self.compartment_8.setObjectName("compartment_8")
        self.compartment_7 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_7.setGeometry(QtCore.QRect(490, 500, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_7.setFont(font)
        self.compartment_7.setObjectName("compartment_7")
        self.compartment_9 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_9.setGeometry(QtCore.QRect(770, 500, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_9.setFont(font)
        self.compartment_9.setObjectName("compartment_9")
        self.compartment_10 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_10.setGeometry(QtCore.QRect(910, 500, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_10.setFont(font)
        self.compartment_10.setObjectName("compartment_10")
        self.shelf_A = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_A.setGeometry(QtCore.QRect(420, 130, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_A.setFont(font)
        self.shelf_A.setObjectName("shelf_A")
        self.shelf_B = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_B.setGeometry(QtCore.QRect(610, 130, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_B.setFont(font)
        self.shelf_B.setObjectName("shelf_B")
        self.shelf_C = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_C.setGeometry(QtCore.QRect(810, 130, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_C.setFont(font)
        self.shelf_C.setObjectName("shelf_C")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(610, 30, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(560, 290, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 420, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.compartment_1.setText(_translate("MainWindow", "1"))
        self.compartment_2.setText(_translate("MainWindow", "2"))
        self.compartment_3.setText(_translate("MainWindow", "3"))
        self.compartment_6.setText(_translate("MainWindow", "6"))
        self.compartment_5.setText(_translate("MainWindow", "5"))
        self.compartment_4.setText(_translate("MainWindow", "4"))
        self.compartment_8.setText(_translate("MainWindow", "8"))
        self.compartment_7.setText(_translate("MainWindow", "7"))
        self.compartment_9.setText(_translate("MainWindow", "9"))
        self.compartment_10.setText(_translate("MainWindow", "10"))
        self.shelf_A.setText(_translate("MainWindow", "A"))
        self.shelf_B.setText(_translate("MainWindow", "B"))
        self.shelf_C.setText(_translate("MainWindow", "C"))
        self.label.setText(_translate("MainWindow", "Shelf"))
        self.label_2.setText(_translate("MainWindow", "Compartment"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
  
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())