import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QTimer
from gui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.btn_start.clicked.connect(self.start)
    
    def start(self): # Dùng để thay thế while loop
        timer = QTimer(self)
        timer.timeout.connect(self.loop)
        timer.start(1000)

    def loop(self):
        print('run')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
