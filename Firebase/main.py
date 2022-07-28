import sys, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QRunnable, QThreadPool

from gui import Ui_MainWindow
from firebase import Firebase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.database = Firebase()

        self.status_change()
        self.uic.btn_led.clicked.connect(self.func_onOff)
        self.uic.btn_update.clicked.connect(self.func_update)

    def func_onOff(self):
        temp = self.database.get_led_value()
        print("temp:", temp)
        if (temp == '0'):
            self.uic.btn_led.setText("On")
            self.database.update_led("1")
        else:
            self.uic.btn_led.setText("Off")
            self.database.update_led("0")

        #database.update_led("1")

    def status_change(self):
        if (led == '1'):
            self.uic.btn_led.setText("On")
        elif (led == '0'):
            self.uic.btn_led.setText("Off")
        
        self.uic.lbl_humidityValue.setText(humi)
        self.uic.lbl_temperatureValue.setText(temp)

    def func_update(self):
        text = self.uic.lineEdit_noti.text()
        print(text)
        self.database.update_noti(text)

class Runnable(QRunnable):
    def __init__(self):
        super().__init__()
    
    def run(self):
        self.database = Firebase()
        while (True):
            global led, humi, temp
            led = self.database.get_led_value()
            humi = str(self.database.get_humi_value()) + " %"
            temp = str(self.database.get_temp_value()) + " *C"
            time.sleep(0.5)
            

if __name__ == "__main__":
    pool = QThreadPool.globalInstance()
    runnable = Runnable()
    pool.start(runnable)

    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())