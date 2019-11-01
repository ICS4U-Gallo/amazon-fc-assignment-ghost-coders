from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import GUI, GUI_2, GUI_3, GUI_4, GUI_box_type, GUI_final

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.GUI = GUI.GUI()
        self.GUI_2 = GUI_2.GUI_2()
        self.GUI_3 = GUI_3.GUI_3()
        self.GUI_4 = GUI_4.GUI_4()
        self.GUI_box_type = GUI_box_type.GUI_box_type()
        self.GUI_final = GUI_final.GUI_final()
        self.startGUI()
    
    def startGUI(self):
        self.GUI.setupUi(self)
        self.GUI.cont.clicked.connect(self.startGUI_2())
        self.show()
        
    def startGUI2(self):
        self.gui_2.setupUi(self)
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

