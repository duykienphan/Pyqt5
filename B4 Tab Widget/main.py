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
        self.uic.btn_tab1.clicked.connect(self.func_showTab1)
        self.uic.btn_tab2.clicked.connect(self.func_showTab2)
        self.uic.btn_tab3.clicked.connect(self.func_showTab3)
        self.uic.btn_close.clicked.connect(self.func_closeWindow)


        #Cấu hình lại đường dẫn cho ảnh, icon
        self.uic.lbl_img1.setPixmap(QtGui.QPixmap(r"D:\Kien Phan\Python\Pyqt5\B3 Stacked Widget\eiffel.jpg"))
        self.uic.lbl_img2.setPixmap(QtGui.QPixmap(r"D:\Kien Phan\Python\Pyqt5\B3 Stacked Widget\riviera.jpg"))

    ##################### Các chức năng #############################
    def func_showTab1(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab)
    def func_showTab2(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_2)
    def func_showTab3(self):
        self.uic.tabWidget.setCurrentWidget(self.uic.tab_3)
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
