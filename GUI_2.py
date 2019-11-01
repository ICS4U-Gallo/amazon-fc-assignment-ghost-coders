from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import json

class GUI_2(object):
    with open("barcode.json", "r") as f:
        item = json.load(f)

    def setupUi(self, MainWindow):
        self.item = GUI_2.item
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 670)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.compartment_1 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_1.setGeometry(QtCore.QRect(50, 360, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.compartment_1.setFont(font)
        self.compartment_1.setObjectName("compartment_1")
        self.compartment_2 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_2.setGeometry(QtCore.QRect(190, 360, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_2.setFont(font)
        self.compartment_2.setObjectName("compartment_2")
        self.compartment_3 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_3.setGeometry(QtCore.QRect(330, 360, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_3.setFont(font)
        self.compartment_3.setObjectName("compartment_3")
        self.compartment_6 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_6.setGeometry(QtCore.QRect(50, 490, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_6.setFont(font)
        self.compartment_6.setObjectName("compartment_6")
        self.compartment_5 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_5.setGeometry(QtCore.QRect(610, 360, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_5.setFont(font)
        self.compartment_5.setObjectName("compartment_5")
        self.compartment_4 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_4.setGeometry(QtCore.QRect(470, 360, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_4.setFont(font)
        self.compartment_4.setObjectName("compartment_4")
        self.compartment_8 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_8.setGeometry(QtCore.QRect(330, 490, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_8.setFont(font)
        self.compartment_8.setObjectName("compartment_8")
        self.compartment_7 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_7.setGeometry(QtCore.QRect(190, 490, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_7.setFont(font)
        self.compartment_7.setObjectName("compartment_7")
        self.compartment_9 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_9.setGeometry(QtCore.QRect(470, 490, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_9.setFont(font)
        self.compartment_9.setObjectName("compartment_9")
        self.compartment_10 = QtWidgets.QPushButton(self.centralwidget)
        self.compartment_10.setGeometry(QtCore.QRect(610, 490, 121, 111))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.compartment_10.setFont(font)
        self.compartment_10.setObjectName("compartment_10")
        self.shelf_A = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_A.setGeometry(QtCore.QRect(120, 120, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_A.setFont(font)
        self.shelf_A.setObjectName("shelf_A")
        self.shelf_B = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_B.setGeometry(QtCore.QRect(310, 120, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_B.setFont(font)
        self.shelf_B.setObjectName("shelf_B")
        self.shelf_C = QtWidgets.QPushButton(self.centralwidget)
        self.shelf_C.setGeometry(QtCore.QRect(510, 120, 161, 151))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.shelf_C.setFont(font)
        self.shelf_C.setObjectName("shelf_C")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 141, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(260, 280, 281, 61))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(30)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(790, 420, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.barcode = QtWidgets.QLabel(self.centralwidget)
        self.barcode.setGeometry(QtCore.QRect(750, 30, 321, 81))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(40)
        self.barcode.setFont(font)
        self.barcode.setObjectName("label")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.shelf_A.clicked.connect(self.shelf_A_click)
        self.shelf_B.clicked.connect(self.shelf_B_click)
        self.shelf_C.clicked.connect(self.shelf_C_click)
        self.compartment_1.clicked.connect(self.compartment_1_click)
        self.compartment_2.clicked.connect(self.compartment_2_click)
        self.compartment_3.clicked.connect(self.compartment_3_click)
        self.compartment_4.clicked.connect(self.compartment_4_click)
        self.compartment_5.clicked.connect(self.compartment_5_click)
        self.compartment_6.clicked.connect(self.compartment_6_click)
        self.compartment_7.clicked.connect(self.compartment_7_click)
        self.compartment_8.clicked.connect(self.compartment_8_click)
        self.compartment_9.clicked.connect(self.compartment_9_click)
        self.compartment_10.clicked.connect(self.compartment_10_click)
        

    def shelf_A_click(self):
        self.shelf_A.setStyleSheet("background-color: rgb(0,200,0)")
        self.shelf_B.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_C.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_num = "A"
        return self.shelf_num

    def shelf_B_click(self):
        self.shelf_A.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_B.setStyleSheet("background-color: rgb(0,200,0)")
        self.shelf_C.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_num = "B"
        return self.shelf_num

    def shelf_C_click(self):
        self.shelf_A.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_B.setStyleSheet("background-color: rgb(220,220,220)")
        self.shelf_C.setStyleSheet("background-color: rgb(0,200,0)")
        self.shelf_num = "C"
        return self.shelf_num

    def compartment_1_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "1"
        return self.compartment_num
        
    def compartment_2_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "2"
        return self.compartment_num

    def compartment_3_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "3"
        return self.compartment_num

    def compartment_4_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "4"
        return self.compartment_num

    def compartment_5_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "5"
        return self.compartment_num

    def compartment_6_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "6"
        return self.compartment_num

    def compartment_7_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "7"
        return self.compartment_num

    def compartment_8_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "8"
        return self.compartment_num

    def compartment_9_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_10.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_num = "9"
        return self.compartment_num

    def compartment_10_click(self):
        self.compartment_1.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_2.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_3.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_4.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_5.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_6.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_7.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_8.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_9.setStyleSheet("background-color: rgb(220,220,220)")
        self.compartment_10.setStyleSheet("background-color: rgb(0,200,0)")
        self.compartment_num = "10"
        return self.compartment_num

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
        self.barcode.setText(_translate("MainWindow", f"{GUI_2.item[0]}"))
        self.pushButton.setText(_translate("MainWindow", "Continue"))
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())