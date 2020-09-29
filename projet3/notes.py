

#4 boutons plusieurs labels and add info on python#4 boutons plusieurs labels and add info on python
# The base is working well
#more and more sexy
# Have to work on this one later https://codeloop.org/pyqt5-qmessagebox-practical-example/
# this one also https://codeloop.org/python-mysql-database-for-beginners/



from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QLabel, QLineEdit, QTextEdit
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):
    def __init__(self):
        super().__init__()
        self.title = "Find the Data you need"
        self.top = 100
        self.left = 200
        self.width = 800
        self.height =600
        self.iconName = "C:\gitproject\projet3\images\OpenDataChallengeDatasets.jpg"
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.CreateLayout()
        
        vbox = QVBoxLayout()
        # Second Big intro Line 
        label2 = QLabel("You will be asked to provide some informations:")
        label2.setFont(QtGui.QFont("Sanserif", 25))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)
        # First Link to search text
        label = QLabel("1) Please insert the link to search")
        label.setFont(QtGui.QFont("Sanserif", 15))
        label.setStyleSheet('color:black')
        vbox.addWidget(label)
		# Insert html line
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)
        vbox.addWidget(self.lineedit)
        # Insert Text for Iteration
        self.label3 = QLabel("2) The number of iteration")
        self.label3.setFont(QtGui.QFont("Sanserif", 15))
        self.label3.setStyleSheet('color:black')
        vbox.addWidget(self.label3)
        # Insert Iteration number line
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit2.returnPressed.connect(self.onPressed)
        vbox.addWidget(self.lineedit2)
        # Insert Text for the word to erase
        self.label4 = QLabel("3) The word to erase")
        self.label4.setFont(QtGui.QFont("Sanserif", 15))
        self.label4.setStyleSheet('color:black')
        vbox.addWidget(self.label4)
        # Insert the word to erase line
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit3.returnPressed.connect(self.onPressed)
        vbox.addWidget(self.lineedit3)
        # Insert Text for the word to erase
        self.label5 = QLabel("4) The name of Csv File")
        self.label5.setFont(QtGui.QFont("Sanserif", 15))
        self.label5.setStyleSheet('color:black')
        vbox.addWidget(self.label5)
        # Insert the word to erase line
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit4.returnPressed.connect(self.onPressed)
        vbox.addWidget(self.lineedit4)
        # Adding the bellow group box
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
    
    def onPressed(self):
        self.label3.setText(self.lineedit.text())

    def CreateLayout(self):
        self.groupBox = QGroupBox("Different actions")
        gridLayout = QGridLayout()
        #First button start
        self.button = QPushButton("Start", self)
        self.button.setWhatsThis("Start the program")
        self.button.setIcon(QtGui.QIcon("C:/gitproject/projet3/images/start.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        gridLayout.addWidget(self.button, 0,0)
        #Second button Show/Hide the Terminal
        self.button2 = QPushButton("Show/Hide", self)
        self.button2.setWhatsThis("Show/Hide the Terminal to see progression")
        self.button2.setIcon(QtGui.QIcon("C:\gitproject\projet3\images\hide.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2, 0,1)
        #Third button No use yet
        self.button3 = QPushButton("No use yet", self)
        self.button3.setIcon(QtGui.QIcon("java.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(40)
        gridLayout.addWidget(self.button3,1,0)
        #Third button No use yet
        self.button4 = QPushButton("No use Yet", self)
        self.button4.setIcon(QtGui.QIcon("csharp.png"))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.setMinimumHeight(40)
        gridLayout.addWidget(self.button4, 1, 1)
        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())