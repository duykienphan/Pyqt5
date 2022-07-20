import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_exit.clicked.connect(self.func_close)
        self.uic.btn_login.clicked.connect(self.func_login)
        
        #Cấu hình lại đường dẫn cho ảnh, icon
        self.uic.lbl_passIcon.setPixmap(QtGui.QPixmap(r"B10 Login Screen\unlock.png"))
        self.uic.lbl_accIcon.setPixmap(QtGui.QPixmap(r"B10 Login Screen\account.png"))
        self.uic.lbl_image.setPixmap(QtGui.QPixmap(r"B10 Login Screen\user.png"))

    ##################### Các chức năng #############################
    def func_close(self):
        self.main_win.close()
    
    def func_login(self):
        pass

    #################################################################

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

#Chèn vô def setupUi()
#MainWindow.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)