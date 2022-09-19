import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui     as qtg
from PyQt5 import QtCore    as qtc
# Sprint-5 Step-1
import pyodbc

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

        # Sprint-5 Step-2 (extend Sprint-4 Step-7 
        #                  from the mountain_sprint4_skeleton.py file)
        # Buttons
        # Create a button called loadCanvas_btn. Set its text to 'Display Canvas'.
        # Set its clicked event to execute the loadCanvas function.
        self.loadCanvas_btn = ...
        # Create a button called loadDb_btn. Set its text to 'Load DB'.
        # Set its clicked event to execute the loadDb function.
        self.loadDb_btn = ...

        # Sprint-4 Step-8
        # Create a small 10x10 pixel canvas which will later be resized (based on the
        # input file's dimentions). Once the user selected an input file, this canvas
        # will replace label1's mountain image
        self.canvas = qtg.QPixmap(10, 10)        

        # Sprint-5 Step-3 (extend Sprint-4 Step-9
        #                  from the mountain_sprint4_skeleton.py file)
        # Create and show() layouts that would display label1 (the mountain image),
        # the comboBox, label2 (hidden), loadCanvas_btn and loadDb_btn.
        ...
        self.show()

    # ---------------------------------------------------------------
    # This is the end of the mainWindow class's initializer function.
    # Following are other class functions that are part of the
    # mainWindow class, that are used after the mainWindow object has
    # been initialized.
    # ---------------------------------------------------------------

    # Sprint-5 Step-4
    def loadDb(self):
        # Toggle controls visibility
        self.hideControls()
        self.repaint()

        # Sprint-5 Step-5 (similar to Sprint-4 Step-12
        #                  in the mountain_sprint4_skeleton.py file)
        # Extract the selected text from comboBox into a variable 
        # called comboText and use it to read the relevant text input file
        comboText = ...
        ...

        # Sprint-5 Step-6 (same as Sprint-4 Step-13
        #                  in the mountain_sprint4_skeleton.py file)
        # Extract the values of line-1 into self.n_rows and self.n_columns
        ...

        # Sprint-5 Step-7 (same as Sprint-4 Step-14
        #                  in the mountain_sprint4_skeleton.py file)
        # Extract the values of line-2 into a two-dimensional list 
        # called self.grid_data
        # Important! Make sure each value is stored as a valid 
        #            float with two decimals
        ...

        # Sprint-5 Step-8 (similar to Sprint-4 Step-15
        #                  in the mountain_sprint4_skeleton.py file)
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

        # Sprint-5 Step-9
        # Create a connection (called connection) to your MountainDB 
        ...
        connection = ...
        
        # Sprint-5 Step-10
        # Write the meta data of the text input file to the Files table - if such
        # record does not already exist (perhaps it was created during a previous
        # execution of the app).
        # Start by testing to see if such record already exist. Do this by 
        # trying to read a record from the Files table where File_name contains the same
        # value as comboText. 
        cursor = connection.cursor()
        query = ...
        cursor.execute(query)
        file_record = cursor.fetchone()

        # Sprint-5 Step-11
        # If the record could not be read from the Files table, try to write the file meta
        # data to the Files table - as well as the elevations and color values to the
        # DataPoints table.
        if file_record is None:
            try:
                # Sprint-5 Step-12
                # Insert the record into the Files table. You don't have to pass a
                # value for File_id, since that column is auto generated by the database.
                ...

                # Sprint-5 Step-13
                # Extract and store the auto generated File_id, since we need to add it
                # to the DataPoints records as a foreign key. 
                ...
                
                # Sprint-5 Step-14
                # Insert Grid_Points records. Start by creating a loop that will 
                # execute X number of times - where X is equal to the number of
                # elevation values in the text file.
                for ...
                    # Sprint-5 Step-15 (similar to parts of Sprint-4 Step-16
                    #                  in the mountain_sprint4_skeleton.py file)
                    # Extract the data point elevation
                    ...
                    # Compile the data point's color
                    ...
                    
                    # Sprint-5 Step-16
                    # Insert the DataPoints record for the current elevation and color value
                    # in the loop. You don't have to pass a value for DataPoint_id, since
                    # that column is auto generated by the database.
                    query  = ...
                    params = ...
                    cursor.execute(query, params)

                # Sprint-5 Step-17
                # Commit the transaction if all went well, else undo.
                connection.commit()
            except Exception as ex:
                print('Exception Message: '+ str(ex))
                connection.rollback()

        # Sprint-5 Step-18
        # Terminate the connection to your database.
        connection = None

        # Toggle controls visibility
        self.showControls()

    # Sprint-5 Step-21 (similar to parts of Sprint-4 Step-10
    #                  in the mountain_sprint4_skeleton.py file)
    def loadCanvas(self):
        # Clear self.grid_data for newly selected map
        self.grid_data = []

        # Toggle controls visibility
        self.hideControls()
        self.repaint()

        # Sprint-5 Step-22
        # Extract the selected text from comboBox into a variable 
        # called comboText
        comboText = ...

        # Sprint-5 Step-23
        # Create a connection (called connection) to your MountainDB
        ... 
        connection = ...

        # Sprint-5 Step-24
        # Read the record in the Files table where File_name has the same
        # value as comboText
        cursor = connection.cursor()
        query = ...
        cursor.execute(query)
        file_record = cursor.fetchone()

        # Sprint-5 Step-25
        # Extract the value of File_id from the record - into an integer variable 
        # called file_id.
        # You should use this as filter value when you read the DataPoints records.
        file_id = ...

        # Sprint-5 Step-26
        # Extract the valies of self.n_rows and self.n_columns from the record.
        # Convert the values to integers before storing them in the variables.
        self.n_rows     = ...
        self.n_columns  = ...

        # Sprint-5 Step-27
        # Read the DataPoints records associated with the Files record you read above.
        # Remember to filter the records based on the foreign key: File_id = file_id
        # Remember to order the records based on the primary key: DataPoint_id
        query = ...
        cursor.execute(query)
        dataPoint_records = cursor.fetchall()

        # Sprint-5 Step-28 (similar to parts of Sprint-4 Step-16 in 
        #                   the mountain_sprint4_skeleton.py file):
        # Load self.grid_data
        sublist = []
        # Create a loop that will iterate over all the DataPoints records you read 
        i = 0
        for record in dataPoint_records:
            # Create a DataPoint object and populate its variables with the
            # values from the current record in the loop.
            # Ensure that you convert the elevation to a float and the color to a string
            dpObj = DataPoint(... , ...)
            # Append the object to the sublist
            sublist.append(dpObj)
            # If the sublist reached the required size, append
            # it to self.grid_data and create a new empty sublist
            if(((i+1) % self.n_columns) == 0):
                self.grid_data.append(sublist)
                sublist = []
            i = i + 1

        # Sprint-4 Step-17
        # Resize the canvas based on the values in n_columns and n_rows
        # and set the canvas as the new image for label1
        ...

        # Sprint-4 Step-18
        # Link a painter to label1's image and plot the grid points. 
        painter = qtg.QPainter(self.label1.pixmap())
        for x in range(0, self.n_columns):
            for y in range(0, self.n_rows):
                # Plot the point by extracting its base_color value
                # from the object stored in self.grid_data
                ...
        painter.end()

        # Toggle controls visibility
        self.showControls()

    # Functions to disable/hide and enable/show controls
    # Sprint-5 Step-19 (extend Sprint-4 Step-20 in 
    #                   the mountain_sprint4_skeleton.py file)
    def hideControls(self):
        # Disable comboBox
        ...
        # Show label2
        ...
        # Disable loadCanvas_btn
        ...
        # Disable loadDb_btn
        ...
    
    # Sprint-5 Step-20 (extend Sprint-4 Step-21 in 
    #                   the mountain_sprint4_skeleton.py file)
    def showControls(self):
        # Enable comboBox
        ...
        # Hide label2
        ...
        # Enable loadCanvas_btn
        ...
        # Enable loadDb_btn
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
