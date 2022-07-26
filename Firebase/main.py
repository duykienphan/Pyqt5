import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtCore import QTimer

from gui import Ui_MainWindow

from typing_extensions import Self
import pyrebase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.led_check()
        self.uic.btn_led.clicked.connect(self.func_onOff)

    def func_onOff(self):
        database = Firebase()

        temp = database.get_led_value()
        print("temp:", temp)
        if (temp == '0'):
            self.uic.btn_led.setText("On")
            database.update_led("1")
        else:
            self.uic.btn_led.setText("Off")
            database.update_led("0")

        #database.update_led("1")
    
    def led_check(self): # Dùng để thay thế while loop
        timer = QTimer(self)
        timer.timeout.connect(self.status_change)
        timer.start(100)

    def status_change(self):
        database = Firebase()

        led = database.get_led_value()
        if (led == '1'):
            self.uic.btn_led.setText("On")
        elif (led == '0'):
            self.uic.btn_led.setText("Off")
        
        humi = str(database.get_humi_value()) + " %"
        self.uic.lbl_humidityValue.setText(humi)
        temp = str(database.get_temp_value()) + " *C"
        self.uic.lbl_temperatureValue.setText(temp)


class Firebase:

    firebaseConfig = { # Nằm trong General
        'apiKey': "AIzaSyANJLHv-MiuM-7ATuBGwOWiFoZtA9sBtCI",
        'authDomain': "pyqt5-demo.firebaseapp.com",
        'databaseURL': "https://pyqt5-demo-default-rtdb.firebaseio.com",
        'projectId': "pyqt5-demo",
        'storageBucket': "pyqt5-demo.appspot.com",
        'messagingSenderId': "106488053967",
        'appId': "1:106488053967:web:c94cb30d14833467bcb7ba",
        'measurementId': "G-WZQFKE14DS"
    }

    def __init__(self):
        self.firebase = pyrebase.initialize_app(self.firebaseConfig)
        self.db = self.firebase.database()

    def get_led_value(self):
        self.led_value = self.db.child("control").child("led").get().val()
        return self.led_value

    def get_temp_value(self):
        self.temp_value = self.db.child("display").child("temperature").get().val()
        return self.temp_value
    
    def get_humi_value(self):
        self.humi_value = self.db.child("display").child("humidity").get().val()
        return self.humi_value

    def update_led(self, value):
        self.db.child("control").update({"led": value})


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())