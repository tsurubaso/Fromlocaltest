

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
        self.title = "HBox Layout"
        self.top = 200
        self.left = 400
        self.width = 400
        self.height = 100
        self.iconName = "icon.png"
        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.iconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.CreateLayout()
        vbox = QVBoxLayout()
        
        label = QLabel("This Is PyQt5 Labels")
        vbox.addWidget(label)
        label2 = QLabel("This Is PyQt5 GUI Applicaition Development, Hello")
        label2.setFont(QtGui.QFont("Sanserif", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)
		
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.onPressed)
        self.label3 = QLabel(self)
        self.label3.setFont(QtGui.QFont("Sanserif", 15))
        vbox.addWidget(self.label3)
        vbox.addWidget(self.lineedit)


        textEdit = QTextEdit(self)
        vbox.addWidget(textEdit)
        
        self.btn = QPushButton("Open Second Dialog")
        self.btn.setFont(QtGui.QFont("Sanserif", 15))
        self.btn.clicked.connect(self.openSecondDialog)
 
        vbox.addWidget(self.btn)




        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    def onPressed(self):
        self.label3.setText(self.lineedit.text())
        
        
        
    def openSecondDialog(self):
        mydialog = QDialog(self)
        #mydialog.setModal(True)
        #mydialog.exec()
 
        mydialog.show()


    def CreateLayout(self):
        self.groupBox = QGroupBox("What Is Your Favorite Programming Language")
        gridLayout = QGridLayout()
        self.button = QPushButton("Python", self)
        
        self.button.setWhatsThis("This is a button that you can click on this button")
        self.button.setIcon(QtGui.QIcon("pythonicon.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        gridLayout.addWidget(self.button, 0,0)
        self.button2 = QPushButton("C++", self)
        self.button2.setIcon(QtGui.QIcon("cpp.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2, 0,1)
        self.button3 = QPushButton("Java", self)
        self.button3.setIcon(QtGui.QIcon("java.png"))
        self.button3.setIconSize(QtCore.QSize(40, 40))
        self.button3.setMinimumHeight(40)
        gridLayout.addWidget(self.button3,1,0)
        self.button4 = QPushButton("C#", self)
        self.button4.setIcon(QtGui.QIcon("csharp.png"))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.setMinimumHeight(40)
        gridLayout.addWidget(self.button4, 1, 1)
        self.groupBox.setLayout(gridLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())