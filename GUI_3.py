from PyQt5 import QtCore, QtGui, QtWidgets
import json, main, GUI

class GUI_3(object):
    def setupUi(self, MainWindow):
        self.gui = GUI()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1124, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.in_bin = QtWidgets.QPushButton(self.centralwidget)
        self.in_bin.setGeometry(QtCore.QRect(260, 180, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.in_bin.setFont(font)
        self.in_bin.setObjectName("in_bin")
        self.cont = QtWidgets.QPushButton(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(580, 180, 251, 231))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.cont.setFont(font)
        self.cont.setObjectName("cont")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.in_bin.clicked.connect(self.in_bin_click)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.in_bin.setText(_translate("MainWindow", "In Bin"))
        self.cont.setText(_translate("MainWindow", "Continue"))

    def in_bin_click(self):
        self.in_bin.setStyleSheet("background-color: rgb(0,200,0)")
        main.Bin.add(self.gui.product)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GUI_3()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
