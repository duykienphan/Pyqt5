from shutil import unregister_archive_format
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
        self.uic.actionOpen.triggered.connect(self.func_openTxtEdit)
        self.uic.actionCredits.triggered.connect(self.func_showCredits)

        #Cấu hình lại đường dẫn cho ảnh, icon
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(r"B7 Icons\icons\scissors.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uic.actionCopy.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(r"B7 Icons\icons\document (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uic.actionPaste.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(r"B7 Icons\icons\open-folder.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uic.actionOpen.setIcon(icon)
        icon.addPixmap(QtGui.QPixmap(r"B7 Icons\icons\more (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.uic.actionCredits.setIcon(icon)

    ##################### Các chức năng #############################
    def func_openTxtEdit(self):
        self.uic.txtEdit.setText("Hello")
    def func_showCredits(self):
        self.uic.txtEdit.setText("~Made by Kien~")
    #################################################################    

    def show(self):
        self.main_win.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
