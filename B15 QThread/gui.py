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
        MainWindow.resize(620, 167)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget.setGeometry(QtCore.QRect(10, 10, 600, 70))
        self.gridWidget.setObjectName("gridWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.btn_start1 = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start1.sizePolicy().hasHeightForWidth())
        self.btn_start1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_start1.setFont(font)
        self.btn_start1.setObjectName("btn_start1")
        self.gridLayout.addWidget(self.btn_start1, 0, 0, 1, 1)
        self.btn_stop1 = QtWidgets.QPushButton(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop1.sizePolicy().hasHeightForWidth())
        self.btn_stop1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_stop1.setFont(font)
        self.btn_stop1.setObjectName("btn_stop1")
        self.gridLayout.addWidget(self.btn_stop1, 0, 1, 1, 1)
        self.lcdNum_1 = QtWidgets.QLCDNumber(self.gridWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNum_1.sizePolicy().hasHeightForWidth())
        self.lcdNum_1.setSizePolicy(sizePolicy)
        self.lcdNum_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lcdNum_1.setObjectName("lcdNum_1")
        self.gridLayout.addWidget(self.lcdNum_1, 0, 2, 1, 1)
        self.gridWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.gridWidget1.setGeometry(QtCore.QRect(10, 85, 600, 70))
        self.gridWidget1.setObjectName("gridWidget1")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridWidget1)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.btn_stop2 = QtWidgets.QPushButton(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_stop2.sizePolicy().hasHeightForWidth())
        self.btn_stop2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_stop2.setFont(font)
        self.btn_stop2.setObjectName("btn_stop2")
        self.gridLayout_2.addWidget(self.btn_stop2, 0, 1, 1, 1)
        self.btn_start2 = QtWidgets.QPushButton(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_start2.sizePolicy().hasHeightForWidth())
        self.btn_start2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_start2.setFont(font)
        self.btn_start2.setObjectName("btn_start2")
        self.gridLayout_2.addWidget(self.btn_start2, 0, 0, 1, 1)
        self.lcdNum_2 = QtWidgets.QLCDNumber(self.gridWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdNum_2.sizePolicy().hasHeightForWidth())
        self.lcdNum_2.setSizePolicy(sizePolicy)
        self.lcdNum_2.setObjectName("lcdNum_2")
        self.gridLayout_2.addWidget(self.lcdNum_2, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.btn_start1.setText(_translate("MainWindow", "Start"))
        self.btn_stop1.setText(_translate("MainWindow", "Stop"))
        self.btn_stop2.setText(_translate("MainWindow", "Stop"))
        self.btn_start2.setText(_translate("MainWindow", "Start"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())