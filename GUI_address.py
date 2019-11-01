from PyQt5 import QtCore, QtGui, QtWidgets
import main

class Ui_gui_address(object):
    def setupUi(self, gui_address):
        gui_address.setObjectName("gui_address")
        gui_address.resize(1124, 672)
        self.centralwidget = QtWidgets.QWidget(gui_address)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(60, 130, 461, 471))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 481, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.cont = QtWidgets.QPushButton(self.centralwidget)
        self.cont.setGeometry(QtCore.QRect(630, 220, 391, 261))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(24)
        self.cont.setFont(font)
        self.cont.setObjectName("cont")
        gui_address.setCentralWidget(self.centralwidget)

        self.retranslateUi(gui_address)
        QtCore.QMetaObject.connectSlotsByName(gui_address)
        self.address = self.lineEdit.text()
        
    def retranslateUi(self, gui_address):
        _translate = QtCore.QCoreApplication.translate
        gui_address.setWindowTitle(_translate("gui_address", "MainWindow"))
        self.label.setText(_translate("gui_address", "Please enter Shipping Address"))
        self.cont.setText(_translate("gui_address", "Continue"))
       
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui_address = QtWidgets.QMainWindow()
    ui = Ui_gui_address()
    ui.setupUi(gui_address)
    gui_address.show()
    sys.exit(app.exec_())
