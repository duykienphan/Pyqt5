import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui import Ui_MainWindow

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
import matplotlib.pyplot as plt
import numpy as np

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_start.clicked.connect(self.func_start)
        
        #Cấu hình lại đường dẫn cho ảnh, icon
        

    ##################### Các chức năng #############################
    def func_start(self):
        # Show diagram
        self.uic.verticalLayout.addWidget(show_chart())
    
    #################################################################

    def show(self):
        self.main_win.show()


class show_chart(FigureCanvasQTAgg):
    def __init__(self):
        self.fig, self.ax = plt.subplots()
        super().__init__(self.fig)

        labels = ['Men', 'Woman', 'Child', 'Older', 'Other']
        colors = ['red', 'yellow', 'pink', 'green', 'black']
        value = [20, 34, 40, 35, 27]

        x = np.arange(len(labels))
        width = 0.35 # the width of the bars
        rects1 = self.ax.bar(labels, value, width, label= 'Statitics', color=colors) # Show label of each column
        self.ax.bar_label(rects1) # Show value of each column
        self.fig.suptitle('men and women', size=15)

        # Add some text for labels, title and custom y-axis tick labels, etc
        self.ax.set_ylabel('scores')
        self.ax.legend()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())