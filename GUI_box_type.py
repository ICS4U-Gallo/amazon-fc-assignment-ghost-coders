from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import json

class GUI_box_type(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.small_box = QtWidgets.QPushButton(self.centralwidget)
        self.small_box.setGeometry(QtCore.QRect(100, 200, 241, 211))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.small_box.setFont(font)
        self.small_box.setObjectName("small_box")
        self.fragile_box = QtWidgets.QPushButton(self.centralwidget)
        self.fragile_box.setGeometry(QtCore.QRect(100, 450, 451, 131))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.fragile_box.setFont(font)
        self.fragile_box.setObjectName("fragile_box")
        self.large_box = QtWidgets.QPushButton(self.centralwidget)
        self.large_box.setGeometry(QtCore.QRect(790, 200, 241, 211))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.large_box.setFont(font)
        self.large_box.setObjectName("large_box")
        self.medium_box = QtWidgets.QPushButton(self.centralwidget)
        self.medium_box.setGeometry(QtCore.QRect(460, 200, 241, 211))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.medium_box.setFont(font)
        self.medium_box.setObjectName("medium_box")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(390, 50, 401, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cont = QtWidgets.QPushButton(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(580, 450, 451, 131))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.cont.setFont(font)
        self.cont.setObjectName("Continue")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.small_box.clicked.connect(self.small_box_click)
        self.medium_box.clicked.connect(self.median_box_click)
        self.large_box.clicked.connect(self.large_box_click)
        self.fragile_box.clicked.connect(self.fragile_box_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.small_box.setText(_translate("MainWindow", "Small Box"))
        self.fragile_box.setText(_translate("MainWindow", "Fragile"))
        self.large_box.setText(_translate("MainWindow", "Large Box"))
        self.medium_box.setText(_translate("MainWindow", "Medium Box"))
        self.label.setText(_translate("MainWindow", "Select Box Type"))
        self.cont.setText(_translate("MainWindow", "Continue"))

    def small_box_click(self):
        self.small_box.setStyleSheet("background-color: rgb(0,200,0)")
        self.medium_box.setStyleSheet("background-color: rgb(255,255,255)")
        self.large_box.setStyleSheet("background-color: rgb(255,255,255)")
    
    def median_box_click(self):
        self.small_box.setStyleSheet("background-color: rgb(255,255,255)")
        self.medium_box.setStyleSheet("background-color: rgb(0,200,0)")
        self.large_box.setStyleSheet("background-color: rgb(255,255,255)")
    
    def large_box_click(self):
        self.small_box.setStyleSheet("background-color: rgb(255,255,255)")
        self.medium_box.setStyleSheet("background-color: rgb(255,255,255)")
        self.large_box.setStyleSheet("background-color: rgb(0,200,0)")
    
    def fragile_box_click(self):
        self.fragile_box.setStyleSheet("background-color: rgb(0,200,0)")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_box_type()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())