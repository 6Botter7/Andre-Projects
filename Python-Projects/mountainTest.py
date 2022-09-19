import math
import PyQt5 as P
from PyQt5.QtWidgets import QApplication, QLabel, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt
from PyQt5 import QtGui as qtg
from PyQt5 import QtWidgets as qtw


class mainWindow(QtWidgets.QMainWindow):
    # Sprint-1 Step-1: Initializer function

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Mountain')
        self.setWindowIcon(
            qtg.QIcon("C:\Andre-Projects\Python-Projects\mountain.jpg"))
        count = 1
        self.n_rows = 0
        self.n_columns = 0
        self.grid_data = [[]]
        self.maxNum = -sys.maxsize
        self.minNum = sys.maxsize

        # self.elevation = elevation  # Must be float to cater for data format
        # self.base_color = color
        self.subList = {}

        file = open('trivial.txt', 'r')

        for line in file:
            if count == 1:
                count = 0
                self.n_rows = int(line[0:(line.find(' '))])
                self.n_columns = int(line[(line.find(' ')+1):])
            else:

                line = line.split(' ', self.n_columns*self.n_rows)
                line = [line[i:i+self.n_columns]
                        for i in range(0, len(line), self.n_columns)]
                self.grid_data = line

        self.grid_data = [[float(string) for string in inner]
                          for inner in self.grid_data]

        self.label = P.QtWidgets.QLabel()
        canvas = P.QtGui.QPixmap(self.n_rows, self.n_columns)
        self.label.setPixmap(canvas)
        self.setCentralWidget(self.label)
        self.DataPoint()

    def DataPoint(self):
        # def __init__(self, elevation, color):
        self.elevation = 0.0  # Must be float to cater for data format
        self.base_color = ""
        self.subList = []

        painter = P.QtGui.QPainter(self.label.pixmap())
        pen = P.QtGui.QPen()
        pen.setWidth(1)
        painter.setPen(pen)

        for row in range(self.n_rows):
            for col in range(self.n_columns):
                if (self.grid_data[row][col]) > self.maxNum:
                    self.maxNum = (self.grid_data[row][col])
                elif (self.grid_data[row][col]) < self.minNum:
                    self.minNum = (self.grid_data[row][col])

        for row in range(self.n_rows):
            for col in range(self.n_columns):
                self.elevation = (self.grid_data[row][col])
                self.subList.append([self.elevation])
                norm_val = (self.elevation-self.minNum) / \
                    (self.maxNum-self.minNum)
                cValue = math.trunc(255 * norm_val)
                hexValue = '#{:02X}{:02X}{:02X}'.format(cValue, cValue, cValue)
                self.base_color = hexValue
                self.subList.append([self.base_color])
                pen.setColor(QtGui.QColor(hexValue))
                painter.setPen(pen)
                painter.drawPoint(row, col)

        print(self.subList)

        print(self.grid_data)


app = QApplication(sys.argv)
Window = mainWindow()
Window.show()
app.exec_()
