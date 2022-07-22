import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_exit.clicked.connect(self.func_close)
        self.uic.btn_login.clicked.connect(self.func_login)
        self.uic.btn_logOut.clicked.connect(self.func_logOut)

        
        #Cấu hình lại đường dẫn cho ảnh, icon
        self.uic.lbl_passIcon.setPixmap(QtGui.QPixmap(r"B10 Login Screen\unlock.png"))
        self.uic.lbl_accIcon.setPixmap(QtGui.QPixmap(r"B10 Login Screen\account.png"))
        self.uic.lbl_image.setPixmap(QtGui.QPixmap(r"B10 Login Screen\user.png"))

    ##################### Các chức năng #############################
    def func_close(self):
        self.main_win.close()
    
    def func_login(self):
        acc = self.uic.lnEdit_acc.text()
        password = self.uic.lnEdit_pass.text()
        if (acc == "kienphan30103") and (password == "123456"):
            self.uic.stackedWidget.setCurrentWidget(self.uic.page_2)
        else:
            self.showdialog()
            
    def showdialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)

        msg.setText("Username or Password is incorrect!")
        msg.setWindowTitle("Error!")
        msg.setStandardButtons(QMessageBox.Ok)
            
        retval = msg.exec_()
        print("value of pressed message box button:", retval)

    def func_logOut(self):
        self.uic.stackedWidget.setCurrentWidget(self.uic.page)

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