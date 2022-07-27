import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer

from gui import Ui_MainWindow
from firebase import Firebase

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.status_check()
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
    
    def status_check(self):
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



if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())