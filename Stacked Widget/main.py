import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho các nút bấm
        self.uic.btn_page1.clicked.connect(self.func_showPage1)
        self.uic.btn_page2.clicked.connect(self.func_showPage2)
        self.uic.btn_page3.clicked.connect(self.func_showPage3)
        self.uic.btn_close.clicked.connect(self.func_closeWindow)

        #Cấu hình lại đường dẫn cho ảnh, icon
        self.uic.lbl_img1.setPixmap(QtGui.QPixmap(r"D:\Kien Phan\Python\Pyqt5\Stacked Widget\eiffel.jpg"))
        self.uic.lbl_img2.setPixmap(QtGui.QPixmap(r"D:\Kien Phan\Python\Pyqt5\Stacked Widget\riviera.jpg"))

    ##################### Các chức năng #############################
    def func_showPage1(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page)

    def func_showPage2(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)

    def func_showPage3(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page_3)

    def func_closeWindow(self):
        self.main_win.close()
    #################################################################    

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
