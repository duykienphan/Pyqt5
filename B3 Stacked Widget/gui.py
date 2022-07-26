# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 20, 760, 300))
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.Panel)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.stackedWidget.setLineWidth(3)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.lbl_img1 = QtWidgets.QLabel(self.page)
        self.lbl_img1.setGeometry(QtCore.QRect(10, 10, 730, 275))
        self.lbl_img1.setText("")
        self.lbl_img1.setPixmap(QtGui.QPixmap("eiffel.jpg"))
        self.lbl_img1.setScaledContents(True)
        self.lbl_img1.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img1.setObjectName("lbl_img1")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.lbl_img2 = QtWidgets.QLabel(self.page_2)
        self.lbl_img2.setGeometry(QtCore.QRect(10, 10, 735, 275))
        self.lbl_img2.setText("")
        self.lbl_img2.setPixmap(QtGui.QPixmap("riviera.jpg"))
        self.lbl_img2.setScaledContents(True)
        self.lbl_img2.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_img2.setObjectName("lbl_img2")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setStyleSheet("background-color: rgb(170, 255, 127);")
        self.page_3.setObjectName("page_3")
        self.lbl_text = QtWidgets.QLabel(self.page_3)
        self.lbl_text.setGeometry(QtCore.QRect(280, 120, 200, 60))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lbl_text.setFont(font)
        self.lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_text.setObjectName("lbl_text")
        self.stackedWidget.addWidget(self.page_3)
        self.btn_page1 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_page1.setGeometry(QtCore.QRect(50, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page1.setFont(font)
        self.btn_page1.setObjectName("btn_page1")
        self.btn_close = QtWidgets.QPushButton(self.centralwidget)
        self.btn_close.setGeometry(QtCore.QRect(650, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_close.setFont(font)
        self.btn_close.setObjectName("btn_close")
        self.btn_page2 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_page2.setGeometry(QtCore.QRect(270, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page2.setFont(font)
        self.btn_page2.setObjectName("btn_page2")
        self.btn_page3 = QtWidgets.QPushButton(self.centralwidget)
        self.btn_page3.setGeometry(QtCore.QRect(460, 350, 100, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.btn_page3.setFont(font)
        self.btn_page3.setObjectName("btn_page3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lbl_text.setText(_translate("MainWindow", "The end!"))
        self.btn_page1.setText(_translate("MainWindow", "Page 1"))
        self.btn_close.setText(_translate("MainWindow", "Close"))
        self.btn_page2.setText(_translate("MainWindow", "Page 2"))
        self.btn_page3.setText(_translate("MainWindow", "Page 3"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
