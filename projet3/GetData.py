
# Notes
#region
#4 boutons plusieurs labels and add info on python#4 boutons plusieurs labels and add info on python
# The base is working well
#more and more sexy
# Have to work on this one later https://codeloop.org/pyqt5-qmessagebox-practical-example/
# this one also https://codeloop.org/python-mysql-database-for-beginners/
#endregion

#Import
#region
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QLabel, QLineEdit
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

import requests
from bs4 import BeautifulSoup
import pandas as pd
import urllib.request
#endregion

#Values
#region
my_list = []
substring = "detail"
adress1=""
nbrBoucle=0
eraseName=""
nameCsv=""
adress2=""
#endregion

#Window Class
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
        
        
        
        vbox = QVBoxLayout()
        # Second Big intro Line 
        label2 = QLabel("You will be asked to provide some informations:")
        label2.setFont(QtGui.QFont("Sanserif", 25))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label2)

        # First Link to search text
        label = QLabel("1) Please insert the link to search, and Enter")
        label.setFont(QtGui.QFont("Sanserif", 15))
        label.setStyleSheet('color:black')
        vbox.addWidget(label)
		# Insert html line
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        adress1=self.lineedit.text()
        vbox.addWidget(self.lineedit)

         # Secong magical Link  text
        label6 = QLabel("1) Please insert the magical link, and Enter")
        label6.setFont(QtGui.QFont("Sanserif", 15))
        label6.setStyleSheet('color:black')
        vbox.addWidget(label6)
		# Insert html line
        self.lineedit5 = QLineEdit(self)
        self.lineedit5.setFont(QtGui.QFont("Sanserif", 15))
        adress2=self.lineedit5.text()
        vbox.addWidget(self.lineedit5)

        # Insert Text for Iteration
        self.label3 = QLabel("2) The number of iteration, and Enter")
        self.label3.setFont(QtGui.QFont("Sanserif", 15))
        self.label3.setStyleSheet('color:black')
        vbox.addWidget(self.label3)
        # Insert Iteration number line
        self.lineedit2 = QLineEdit(self)
        self.lineedit2.setFont(QtGui.QFont("Sanserif", 15))
        nbrBoucle=self.lineedit2.text()
        vbox.addWidget(self.lineedit2)
        # Insert Text for the word to erase
        self.label4 = QLabel("3) The word to erase, and Enter")
        self.label4.setFont(QtGui.QFont("Sanserif", 15))
        self.label4.setStyleSheet('color:black')
        vbox.addWidget(self.label4)
        # Insert the word to erase line
        self.lineedit3 = QLineEdit(self)
        self.lineedit3.setFont(QtGui.QFont("Sanserif", 15))
        eraseName=self.lineedit3.text()
        vbox.addWidget(self.lineedit3)
        # Insert Text for the word to erase
        self.label5 = QLabel("4) The name of Csv File, and Enter")
        self.label5.setFont(QtGui.QFont("Sanserif", 15))
        self.label5.setStyleSheet('color:black')
        vbox.addWidget(self.label5)
        # Insert the word to erase line
        self.lineedit4 = QLineEdit(self)
        self.lineedit4.setFont(QtGui.QFont("Sanserif", 15))
        nameCsv=self.lineedit4.text()
        vbox.addWidget(self.lineedit4)

        # Adding the bellow group box

        self.groupBox = QGroupBox("Different actions")
        gridLayout = QGridLayout()
        #First button start
        self.button = QPushButton("Start", self)
        self.button.setWhatsThis("Start the program")
        self.button.setIcon(QtGui.QIcon("C:/gitproject/projet3/images/start.png"))
        self.button.setIconSize(QtCore.QSize(40, 40))
        self.button.setMinimumHeight(40)
        self.button.clicked.connect( self.search1(adress1, adress2, nbrBoucle, eraseName, nameCsv))
        # 
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
        # button No use yet
        self.button4 = QPushButton("No use Yet", self)
        self.button4.setIcon(QtGui.QIcon("csharp.png"))
        self.button4.setIconSize(QtCore.QSize(40, 40))
        self.button4.setMinimumHeight(40)
        gridLayout.addWidget(self.button4, 1, 1)

        self.groupBox.setLayout(gridLayout)
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    
    
    
    
    def search1(self,adress1, adress2, nbrBoucle, eraseName, nameCsv):
        nbrBoucle=int(nbrBoucle)
        for i in range (1,nbrBoucle,1):
            gribou=adress1+str(i)
            result2 = requests.get (gribou)
            a=result2.status_code
            print (a)
            soup = BeautifulSoup(result2.text, 'html.parser')
            for a in soup.find_all('a'):
                fullstring= a.get('href')
                if fullstring is None:
                    continue
                if substring in fullstring:
                    my_list.append(adress2+fullstring)

        df = pd.DataFrame(my_list, columns = ['col1'])
        df.sort_values(by=['col1'])
        df.drop_duplicates(keep='first', inplace=True)
        count_row = df.shape[0]  # gives number of row count
        count_col = df.shape[1]
        print (count_row )
        print (count_col )
        print (len(my_list))
        #df.to_csv('HopitalList.csv', index=False)

        df2 = pd.DataFrame(columns=['Name', 'Phone','post code','adress','Url','Client Adress'])
        for i in range (1,len(my_list),1):
            url = my_list[i]
            page=urllib.request.urlopen(url)
            soup = BeautifulSoup(page, 'html.parser')
            bloublou4=soup.find_all('td')
            print('                         ')
            bloublou2=soup.find('h1',attrs={"class":"page_title"})
            if bloublou2 is None:
                bloublou2='None'
            else:
                bloublou2=bloublou2.text
                bloublou2=bloublou2.replace(eraseName, '')
            
            if bloublou4[0] is None:
                bloublou4[0]='None'
            else:
                bloublou4[0]=bloublou4[0].text
                bloublou4[0]=bloublou4[0].replace('地図を見る', '')
                bloublou4a=bloublou4[0][10:]
                bloublou4b=bloublou4[0][:9]

            if bloublou4[1] is None:
                bloublou4[1]='None'
            else:
                bloublou4[1]=bloublou4[1].text
                bloublou4[1]=bloublou4[1][:13]
            
            if len(bloublou4) <31:
                glagla='None'
            try:
                glagla=bloublou4[31].text.strip()
        
            except IndexError:
                glagla='None'

            df2.loc[i] = [ bloublou2,bloublou4[1], bloublou4b,bloublou4a, glagla, url]
            
        df2.sort_values(by=['Name'])
        df2.drop_duplicates(keep='first', inplace=True)
        df2.to_csv(nameCsv+".csv", index=False, encoding="utf_8_sig")


    
        

#Main class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())