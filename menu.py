from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import GUI, GUI_2, GUI_3, GUI_4, GUI_box_type, GUI_final

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.gui = GUI.GUI()
        self.gui_2 = GUI_2.GUI_2()
        self.gui_3 = GUI_3.GUI_3()
        self.gui_4 = GUI_4.GUI_4()
        self.gui_box_type = GUI_box_type.GUI_box_type()
        self.gui_final = GUI_final.GUI_final()
        self.startGUI()
    
    def startGUI(self):
        self.gui.setupUi(self)
        self.gui.cont.clicked.connect(self.startGUI2)
        self.show()
        
    def startGUI2(self):
        self.gui_2.setupUi(self)
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

