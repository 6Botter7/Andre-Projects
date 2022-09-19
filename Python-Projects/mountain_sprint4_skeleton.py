import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui     as qtg
from PyQt5 import QtCore    as qtc

class mainWindow(qtw.QWidget):
    # Sprint-4 Step-1
    # This initializer function will execute when an object based on mainWindow is created.
    # Inside this class, self refers to QtWidgets.QMainWindow which is the top level window.
    def __init__(self):
        super().__init__()
        
        # Sprint-4 Step-2
        # Variables to store canvas dimentions
        self.n_rows     = 0
        self.n_columns  = 0
        self.grid_data = []

        # Sprint-4 Step-3
        # Set window title and position
        ...

        # Sprint-4 Step-4
        # Create a QComboBox called comboBox, that contains
        # the input file names.
        self.comboBox = ...

        # Sprint-4 Step-5
        # Create label1 and set its initial image. This label will later 
        # be used to display the canvas. You can use any image of a mountain. 
        self.label1 = ...

        # Sprint-4 Step-6
        # Create label2 to display messages to the user. Set its default
        # text to 'Please wait' and execute its hide() function so that
        # it is not visible when the program starts.
        self.label2 = ...

        # Sprint-4 Step-7
        # Buttons
        # Create a button called loadCanvas_btn. Set its text to 'Display Canvas'.
        # Set its clicked event to execute the loadCanvas function.
        self.loadCanvas_btn = ...      

        # Sprint-4 Step-8
        # Create a small 10x10 pixel canvas which will later be resized (based on the
        # input file's dimentions). Once the user selected an input file, this canvas
        # will replace label1's mountain image
        self.canvas = qtg.QPixmap(10, 10)        

        # Sprint-4 Step-9
        # Create and show() layouts that would display label1 (the mountain image),
        # the comboBox, label2 (hidden) and the loadCanvas_btn.
        ...
        self.show()

    # ---------------------------------------------------------------
    # This is the end of the mainWindow class's initializer function.
    # Following are other class functions that are part of the
    # mainWindow class, that are used after the mainWindow object has
    # been initialized.
    # ---------------------------------------------------------------

    # Sprint-4 Step-10
    def loadCanvas(self):
        # Clear self.grid_data for newly selected map
        self.grid_data = []
        
        # Sprint-4 Step-11
        # Toggle controls visibility
        self.hideControls()
        self.repaint()

        # Sprint-4 Step-12
        # Extract the selected text from comboBox into a variable 
        # called comboText and use it to read the relevant text input file
        comboText = ...
        ...

        # Sprint-4 Step-13 (similar to Sprint-1 Step-4 in 
        #                   the mountain_sprint3_skeleton.py file):
        # Extract the values of line-1 into self.n_rows and self.n_columns
        ...

        # Sprint-4 Step-14 (similar to parts of Sprint-1 Step-5 in 
        #                   the mountain_sprint3_skeleton.py file):
        # Extract the values of line-2 into a two-dimensional list 
        # called self.grid_data
        # Important! Make sure each value is stored as a valid 
        #            float with two decimals
        ...

        # Sprint-4 Step-15 (similar to parts of Sprint-1 Step-5 in 
        #                   the mountain_sprint3_skeleton.py file):
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

        # Sprint-4 Step-16 (similar to parts of Sprint-1 Step-5 in 
        #                   the mountain_sprint3_skeleton.py file):
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

        # Sprint-4 Step-17
        # Resize the canvas based on the values in n_columns and n_rows
        # and set the canvas as the new image for label1
        ...

        # Sprint-4 Step-18 (similar to parts of Sprint-1 Step-7 in 
        #                   the mountain_sprint3_skeleton.py file):
        # Link a painter to label1's image and plot the grid points. 
        painter = qtg.QPainter(self.label1.pixmap())
        for x in range(0, self.n_columns):
            for y in range(0, self.n_rows):
                # Plot the point by extracting its base_color value
                # from the object stored in self.grid_data
                ...
        painter.end()

        # Sprint-4 Step-19
        # Toggle controls visibility
        self.showControls()

    # Functions to disable/hide and enable/show controls
    # Sprint-4 Step-20
    def hideControls(self):
        # Disable comboBox
        ...
        # Show label2
        ...
        # Disable loadCanvas_btn
        ...
    
    # Sprint-4 Step-21
    def showControls(self):
        # Enable comboBox
        ...
        # Hide label2
        ...
        # Enable loadCanvas_btn
        ...

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

# *******************************************************************************
# This is the Main Code section of the app.
# If you want to, you could put this section and the above classes in separate
# files, and then import the classes into this main code section.
# *******************************************************************************
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # Create a mainWindow object
    mw = mainWindow()
    sys.exit(app.exec())
