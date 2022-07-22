import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from gui import Ui_MainWindow

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)

        #Cấu hình cho Table Widget
        self.uic.tableWidget.setRowCount(10)        # Tạo 1 bảng có 10 hàng
        self.uic.tableWidget.setColumnCount(5)      # Tạo 1 bảng có 10 cột
        self.uic.tableWidget.setItem(0, 0, QTableWidgetItem("Ô có địa chỉ [0,0]"))  #Gán giá trị tại ô bất kì
        self.uic.tableWidget.setItem(3, 1, QTableWidgetItem("Ô có địa chỉ [3,1]"))  #Gán giá trị tại ô bất kì
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'])


        ##################### Gán giá trị ô vào biến #############################
        value = self.uic.tableWidget.item(0, 0).text()      # Giá giá trị của ô [0, 0] vào biến value, sẽ lỗi nếu ô đó k có giá trị
        print(value)

        try: # Cách này khắc phục lỗi khi ô được gán không có giá trị (ô trống)
            value = self.uic.tableWidget.item(0, 1).text()
            print(value)
        except:
            value = "None"
            print(value)
        ##########################################################################

        #Cấu hình chức năng cho nút nhấn
        self.uic.btn_addColumn.clicked.connect(self.func_addColumn)
        self.uic.btn_addRow.clicked.connect(self.func_addRow)
        self.uic.btn_readCell.clicked.connect(self.func_readCell)
        self.uic.btn_removeColumn.clicked.connect(self.func_removeColumn)
        self.uic.btn_removeRow.clicked.connect(self.func_removeRow)

        #Cấu hình lại đường dẫn cho ảnh, icon
        

    ##################### Các chức năng #############################
    def func_addColumn(self):
        # last_column = self.uic.tableWidget.columnCount() #Trả về index cột cuối cùng
        current_column = self.uic.tableWidget.currentColumn()
        self.uic.tableWidget.insertColumn(current_column)
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'])


    def func_addRow(self):
        # last_row = self.uic.tableWidget.rowCount() #Trả về index hàng cuối cùng
        current_row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.insertRow(current_row)

    def func_readCell(self):
        current_column = self.uic.tableWidget.currentColumn()
        current_row = self.uic.tableWidget.currentRow()
        
        try:
            value = self.uic.tableWidget.item(current_row, current_column).text()
            self.uic.lbl_readCell.setText(value)
        except:
            value = "None"
            self.uic.lbl_readCell.setText(value)
        
    def func_removeColumn(self):
        current_column = self.uic.tableWidget.currentColumn()
        self.uic.tableWidget.removeColumn(current_column)
        self.uic.tableWidget.setHorizontalHeaderLabels(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7'])

    def func_removeRow(self):
        current_row = self.uic.tableWidget.currentRow()
        self.uic.tableWidget.removeRow(current_row)
    
    #################################################################

    def show(self):
        self.main_win.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())