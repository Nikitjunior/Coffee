import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import (QApplication, QPushButton, QTableWidget, QTableWidgetItem,
                             QHeaderView, QStatusBar, QMainWindow)
from PyQt5.QtCore import Qt


class CoffeeView(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(['ID', 'Название', 'степень обжарки', 'молотый/в зернах',
                                              'описание вкуса', 'цена', 'объем упаковки'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.btn.clicked.connect(self.view_coffee)

    def view_coffee(self):
        con = sqlite3.connect("coffee.sqlite")
        cur = con.cursor()
        result = cur.execute(f"""
        SELECT * FROM coffee
            WHERE title = '{self.title.text()}'""").fetchall()
        self.table.setRowCount(0)
        for i in result:
            row = self.table.rowCount()
            self.table.insertRow(row)
            for j, value in enumerate(i):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, j, item)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CoffeeView()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())