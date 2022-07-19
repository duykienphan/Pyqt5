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
        self.uic.btn_copy.clicked.connect(self.func_copy)
    
    ##################### Các chức năng #############################
    def func_start(self):
        #Đổi text của label chỉ định
        self.uic.lbl_display.setText("Hello!")

    def func_copy(self):
        #copy text trên màn hình và lưu vào biến nhớ
        #chuyển dữ liệu trong biến nhớ vào label_display
        copy = self.uic.lbl_display.text()      #gán dữ liệu đang hiển thị trên lbl_display vào biến copy
        copy = self.uic.txtEdit.toPlainText()   #gán dữ liệu được nhập trên txtEdit vào biến copy
        self.uic.lbl_display.setText(copy)
    
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
