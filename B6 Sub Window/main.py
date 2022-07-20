from shutil import unregister_archive_format
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow
from sub_gui import Ui_Form

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho các nút bấm
        self.uic.btn_exit.clicked.connect(self.func_openSubWindow)

        #Cấu hình lại đường dẫn cho ảnh, icon
        

    ##################### Các chức năng #############################
    def func_openSubWindow(self): # mở cửa sổ thứ 2
        self.second_window = QtWidgets.QMainWindow()
        self.uic1 = Ui_Form()
        self.uic1.setupUi(self.second_window)
        self.second_window.show()
        #Cấu hình chức năng cho các nút bấm trong cửa sổ phụ
        self.uic1.btn_ok.clicked.connect(self.func_closeWindow)
    
    def func_closeWindow(self):
        self.main_win.close()
        self.second_window.close()
    #################################################################    

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
