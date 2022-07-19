"""
Pakages:
pip install pyqt5
pip install pyqt-tools
pip install pyqt5designer
pip install PyQt5-stubs==5.15.2.0

"""

#Chuyển file .ui -> .py: pyuic5 -x ".ui path" -o new_name.py

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow
import time

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_start.clicked.connect(self.func_start)
        self.uic.btn_stop.clicked.connect(self.func_stop)
    
    ##################### Các chức năng #############################
    def func_start(self):
        #Đổi text của label chỉ định
        self.uic.lbl_display.setText("Start button clicked!")
    
    def func_stop(self):
        self.main_win.close()

    #################################################################

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
