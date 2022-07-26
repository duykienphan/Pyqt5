import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtGui
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_open.clicked.connect(self.func_link)
        self.uic.btn_back.clicked.connect(self.func_back)
        self.uic.btn_next.clicked.connect(self.func_next)
        self.list_pics = None
        self.i = 0
    
    ##################### Các chức năng #############################
    def func_link(self):
        files = QFileDialog.getOpenFileNames(None, filter="*.jpg *.png *.jpeg") #import links picture 
        self.list_pics = files[0]
        print(len(self.list_pics))
        self.show_pics(i=0)

    def func_next(self):
        if (self.i < len(self.list_pics)-1):
            self.i += 1
            print(self.i)
            self.show_pics(self.i)
             
    def func_back(self):
        if (self.i > 0):
            self.i -= 1
            print(self.i)
            self.show_pics(self.i)

    def show_pics(self, i):
        self.uic.lbl_screen.setPixmap(QtGui.QPixmap(self.list_pics[i]))
            
    #################################################################

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
