import sys
from threading import Thread
from typing import Counter
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import pyqtSignal, QThread
from PyQt5 import QtCore

from gui import Ui_MainWindow
import time


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        #Cấu hình cho nút bấm
        self.uic.btn_start1.clicked.connect(self.func_start1)
        self.uic.btn_start2.clicked.connect(self.func_start2)
        self.uic.btn_stop1.clicked.connect(self.func_stop1)
        self.uic.btn_stop2.clicked.connect(self.func_stop2)
        
    ##################### Các chức năng #############################
    def func_start1(self):
        self.thread[1] = ThreadClass(index=1)
        self.thread[1].start()
        self.thread[1].signal.connect(self.func_display)
        self.uic.btn_start1.setEnabled(False)
        self.uic.btn_stop1.setEnabled(True)
    
    def func_start2(self):
        self.thread[2] = ThreadClass(index=2)
        self.thread[2].start()
        self.thread[2].signal.connect(self.func_display)
        self.uic.btn_start2.setEnabled(False)
        self.uic.btn_stop2.setEnabled(True) 
    
    def func_stop1(self):
        self.thread[1].stop()
        self.uic.btn_stop1.setEnabled(False)
        self.uic.btn_start1.setEnabled(True)

    def func_stop2(self):
        self.thread[2].stop()
        self.uic.btn_stop2.setEnabled(False)
        self.uic.btn_start2.setEnabled(True)

    def func_display(self, counter):
        m = counter 
        i = self.sender().index
        if (i == 1):
            self.uic.lcdNum_1.display(m)
        if (i == 2):
            self.uic.lcdNum_2.display(m)
    #################################################################

class ThreadClass(QThread):
    signal = pyqtSignal(int)

    def __init__(self, index=0):
        super().__init__()
        self.index = index

    def run(self):
        print('Starting thread...', self.index)
        counter = 0
        while (True):
            counter += 1
            print(counter)
            time.sleep(1)
            if (counter == 5):
                counter = 0
            self.signal.emit(counter)

    def stop(self):
        print('Stop thread...', self.index)
        self.terminate()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())