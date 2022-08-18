from locale import normalize
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore
from PyQt5.QtWidgets import QDialog, QApplication, QWidget


class mainWindow(qtw.QWidget):
    # Sprint-1 Step-1: Initializer function
    def __init__(self):
        super().__init__()
        self.setStyleSheet("background-color: #c2c2a3;")
        self.setWindowTitle('Mountain')
        self.setWindowIcon(
            qtg.QIcon("C:\Andre-Projects\Python-Projects\mountain.jpg"))
        # self.setGeometry(100, 100, 1000, 300)
        # self.setFixedSize(1024, 1024)

        # Sprint-1 Step-2: Variables
        self.data = {

        }
        self.n_rows = []
        self.rowData = []
        self.n_columns = []
        self.columnData = []
        self.grid_data = []

        self.terrainData = []
        self.maxNum = -sys.maxsize
        self.minNum = sys.maxsize

        # Sprint-1 Step-3: Read input file

        def getDimentions():
            with open('trivial.txt', 'r') as data_file:

                for line in data_file

                # for line in data_file[0]:
                #     dataDimentions = line.split()
                #     self.grid_data.append(dataDimentions)

                # for height in self.grid_data[0]:
                #     self.n_rows = height.split()

                # for width in self.grid_data[0]:
                #     self.n_columns = width.split()

                # for data in self.grid_data[1]:
                #     self.terrainData.append(data)

                # print(type(self.terrainData[0]))
                # print(i)
                # print(data)

                # print(type(self.n_rows[0]))
                # print(type(self.grid_data[1]))

                print(self.maxNum, self.minNum, self.grid_data,
                      self.n_columns, self.n_rows)

                return {
                    'height': self.n_rows,
                    'width': self.n_columns,
                    'minNum': self.minNum,
                    'maxNum': self.maxNum,
                    'pointData': self.terrainData
                }

        getDimentions()

        # def drawTerrain():
        #     getDimentions()
        #     canvasHeight = self.n_rows
        #     canvasWidth = self.n_columns
        #     for row in self.terrainData:
        #         nRow = float(row)
        #         # print(type(nRow))
        #         print(type(row))
        #         for column in self.terrainData:
        #             nColumn = float(column)
        #             print(type(column))
        #             value = self.terrainData[float(row)][float(column)]

        #         print(value)

        # drawTerrain()
        # Sprint-1 Step-4: Extract the values of line-1 into

        # Sprint-1 Step-5:
        # Extract the values of line-2 into a two-dimensional list
        # called self.grid_data
        # Important! Make sure each value is stored as a valid
        #            float with two decimals

        # with open('trivial.txt', 'r') as data_file:
        #     for row in data_file:
        #         data = row.split()
        #         self.n_rows.append(data)
        #         # print(self.n_rows)

        # with open('trivial.txt', 'r') as data_file:
        #     for column in data_file:
        #         data = column.split()
        #         self.n_columns.append(data)
        #         # print(self.n_columns)

        # Sprint-1 Step-6:
        # Set window title and icon
        # Create self.label1 to be used to display the canvas
        # Create self.canvas based on the size of self.n_columns and self.n_rows
        # Set self.canvas as the image for label1
        # Create the layout and display the UI

        # Sprint-2 Step-1:
        # Prepare items that can be used to lookup/compile the color
        # of each data_point when it is plotted.
        # These colors must be based on the data_point's elevation which
        # is stored in self.grid_data

        # Sprint-1 Step-7:
        # Link a painter to label1's image and plot the data_points in
        # self.grid_data (the items in the sub-lists) on the canvas.
        # Use "#c2c2a3" as color

        # Sprint-2 Step-2:
        # While plotting each data_point, compile its color based
        # on what you prepared in Sprint-2 Step-1

        self.show()


# *****************************************
# This is the Main Code section of the app.
# *****************************************
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
# Create a mainWindow object
    mw = mainWindow()
    sys.exit(app.exec_())


# Notes
# read line 1 and then line 2
# line 1 = 4 4
# line 2 = 0.20 0.00 0.30 0.25 0.30 0.40 0.45 0.10 0.00 0.50 0.40 0.25 0.40 0.10 0.25 0.30

# width/height in line 1
# split line 1  result = array [ 4, 4]
#  width = splitResult[0]
# height = splitResult[1]
#
#
