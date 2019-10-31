from PyQt5 import QtCore, QtGui, QtWidgets
import main
import GUI_2

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
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
        self.Continue = QtWidgets.QPushButton(self.centralwidget)
        self.Continue.setGeometry(QtCore.QRect(150, 470, 271, 101))
        font = QtGui.QFont()
        font.setFamily("Sitka")
        font.setPointSize(28)
        self.Continue.setFont(font)
        self.Continue.setObjectName("Continue")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1124, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def enter_click(self):
            pass

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Please Enter Product Barcode"))
        self.Enter.setText(_translate("MainWindow", "Enter"))
        self.Continue.setText(_translate("MainWindow", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())