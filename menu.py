from PyQt5 import QtCore, QtGui, QtWidgets
from main import *
import GUI, GUI_2, GUI_3, GUI_4, GUI_box_type, GUI_address, GUI_final, json

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.gui = GUI.GUI()
        self.gui_2 = GUI_2.GUI_2()
        self.gui_3 = GUI_3.GUI_3()
        self.gui_4 = GUI_4.GUI_4()
        self.gui_box_type = GUI_box_type.GUI_box_type()
        self.gui_final = GUI_final.GUI_final()
        self.gui_address = GUI_address.Ui_gui_address()
        self.startGUI()
    
    def startGUI(self):
        self.gui.setupUi(self)
        self.gui.cont.clicked.connect(self.startGUI2)
        self.show()
        
        
    def startGUI2(self):
        self.gui_2.setupUi(self)
        self.gui_2.pushButton.clicked.connect(self.startGUI3)
        self.show()   
        self.shelf = Shelf(self.gui_2.shelf_num,self.gui_2.compartment_num)
        self.gui.trolly.remove(self.gui.product)
        self.shelf.add(self.gui_2.shelf_num, self.gui_2.compartment_num, self.gui.product)

    def startGUI3(self):
        self.gui_3.setupUi(self)
        self.gui_3.cont.clicked.connect(self.startGUI4)
        self.show()
        Shelf.remove(self.item)

    def startGUI4(self):
        self.shelf.remove(self.gui.product)
        self.bin = Bin()
        self.bin.add(self.gui.product)
        self.gui_4.setupUi(self)
        self.gui_4.pushButton.clicked.connect(self.startGUIbox)
        self.show()
        
    
    def startGUIbox(self):
        self.gui_box_type.setupUi(self)
        self.gui_box_type.cont.clicked.connect(self.startGUIAddress)
        self.show()
    
    def startGUIAddress(self):
        self.gui_address.setupUi(self)
        self.gui_address.cont.clicked.connect(self.startGUIfinal, self.gui_address.cont)
        self.bin.remove(self.gui.product)
        self.show()

    def startGUIfinal(self):
        self.box = Packaging(self.gui_box_type.box_type, self.gui_address.address, "Truck 1")
        self.gui_final.setupUi(self)
        self.show()
        delay = QtCore.QTimer
        delay.interval(1000)
        GUI_2.GUI_2.barcode.remove(GUI_2.GUI_2.barcode[0])
        with open("barcode.json", "w") as f:
            json.dump(GUI_2.GUI_2.barcode, f)
        if len(GUI_2.GUI_2.barcode) > 0:
            self.startGUI2
        else: 
            self.startGUI
                   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    sys.exit(app.exec_())

