#This program has spacers (grid)

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_onOff.clicked.connect(self.func_onOff)
        
    
    ##################### Các chức năng #############################
    def func_onOff(self):
        temp = self.uic.lbl_text.text()
        if (temp == '0'):
            self.uic.btn_onOff.setText("On")
            self.uic.lbl_text.setText("1")
        else:
            self.uic.btn_onOff.setText("Off")
            self.uic.lbl_text.setText("0")

    #################################################################

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
