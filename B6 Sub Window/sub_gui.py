# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sub_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.sub_lbl_text = QtWidgets.QLabel(Form)
        self.sub_lbl_text.setGeometry(QtCore.QRect(80, 70, 241, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.sub_lbl_text.setFont(font)
        self.sub_lbl_text.setAlignment(QtCore.Qt.AlignCenter)
        self.sub_lbl_text.setObjectName("sub_lbl_text")
        self.btn_ok = QtWidgets.QPushButton(Form)
        self.btn_ok.setGeometry(QtCore.QRect(140, 200, 93, 28))
        self.btn_ok.setObjectName("btn_ok")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.sub_lbl_text.setText(_translate("Form", "Want to leave?"))
        self.btn_ok.setText(_translate("Form", "OK!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())