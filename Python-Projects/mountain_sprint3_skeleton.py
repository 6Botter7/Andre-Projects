import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui     as qtg
from PyQt5 import QtCore    as qtc

class mainWindow(qtw.QWidget):
    # Sprint-1 Step-1: Initializer function
    def __init__(self):
        super().__init__()
        
        # Sprint-1 Step-2: Variables
        self.n_rows     = 0
        self.n_columns  = 0
        self.grid_data  = []

        # Sprint-1 Step-3: Read input file
        file = open('../Data/small.txt','r')

        # Sprint-1 Step-4: Extract the values of line-1 into 
        # self.n_rows and self.n_columns
        ...

        # Sprint-1 Step-5:
        # Extract the values of line-2 into a two-dimensional list 
        # called self.grid_data
        # Important! Make sure each value is stored as a valid 
        #            float with two decimals
        ...

        # Prepare items that can be used to lookup/compile the color
        # of each data_point when it is plotted.
        # These colors must be based on the data_point's elevation which
        # is stored in self.grid_data
        # --------------
        # Get a set of unique data values - to be used for coloring
        # Sort the list using key=float, otherwise the values will be sorted
        # as strings, producing the wrong mountain image
        # Tranform the set into a list - to be able to use its indexes
        ...

        # Load self.grid_data
        ...
            # Extract the data point elevation
            ...
            # Compile the data point's color
            ...
            # Create the DataPoint object and append it to the sublist.
            ...
            # If the sublist reached the required size, append
            # it to self.grid_data and create a new empty sublist
            ...

        # Sprint-1 Step-6: 
        # Set window title and icon
        ...
        # Create self.label1 to be used to display the canvas
        ...
        # Create self.canvas based on the size of self.n_columns and self.n_rows
        ...     
        # Set self.canvas as the image for label1
        ...
        # Create the layout and display the UI
        ...

        # Sprint-2 Step-1:
        # This code has been incorporated into Sprint-1 Step-5

        # Sprint-1 Step-7: 
        # Link a painter to label1's image and plot the data_points in
        # self.grid_data (the items in the sub-lists) on the canvas. 
        painter = qtg.QPainter(self.label1.pixmap())
        for x in range(0, self.n_columns):
            for y in range(0, self.n_rows):
                # Sprint-2 Step-2:
                # The calculation of a data point's color has
                # been incorporated into Sprint-1 Step-5

                # Sprint-3 Step-1:
                # Plot the point by extracting its base_color value
                # from the object stored in self.grid_data
                ...
        painter.end()
    
    # *****************************************************
    # ****** This is the end of the MainWindow class ******
    # *****************************************************

class DataPoint():
    def __init__(self, elevation, color):
        self.elevation      = elevation     # Must be float to cater for data format
        self.base_color     = color
       
    # ****************************************************
    # ****** This is the end of the DataPoint class ******
    # ****************************************************

# *****************************************
# This is the Main Code section of the app.
# *****************************************
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # Create a mainWindow object
    mw = mainWindow()
    sys.exit(app.exec())
