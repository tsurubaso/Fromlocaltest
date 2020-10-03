
# Notes
#region
"""

        self.textedit = QTextEdit()
        self.textedit.textChanged.connect(self.save_text)
        layout.addWidget(self.textedit)

    def save_text(self):
        text = self.textedit.toPlainText()
        with open('mytextfile.txt', 'w') as f:
            f.write(text)


            def save_text():
        text=textedit.toPlainText()
    with open('mytextfile.txt', 'w') as f:
        f.write(text)

button.clicked.connect(save_text)

https://stackoverflow.com/questions/47560399/run-function-in-the-background-and-update-ui


"""
#endregion

#Import
#region
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QGridLayout, QGroupBox, QVBoxLayout, QLabel, QTextEdit
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
        self.lineedit = QTextEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.textChanged.connect(self.save_text)
        vbox.addWidget(self.lineedit)

         # Second magical Link  text
        label6 = QLabel("1) Please insert the magical link, and Enter")
        label6.setFont(QtGui.QFont("Sanserif", 15))
        label6.setStyleSheet('color:black')
        vbox.addWidget(label6)
		# Insert html line
        self.lineedit5 = QTextEdit(self)
        self.lineedit5.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit5.textChanged.connect(self.save_text)
        vbox.addWidget(self.lineedit5)

        # Insert Text for Iteration
        self.label3 = QLabel("2) The number of iteration, and Enter")
        self.label3.setFont(QtGui.QFont("Sanserif", 15))
        self.label3.setStyleSheet('color:black')
        vbox.addWidget(self.label3)
        # Insert Iteration number line
        self.lineedit2 = QTextEdit(self)
        self.lineedit2.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit2.textChanged.connect(self.save_text)
        vbox.addWidget(self.lineedit2)

        # Insert Text for the word to erase
        self.label4 = QLabel("3) The word to erase, and Enter")
        self.label4.setFont(QtGui.QFont("Sanserif", 15))
        self.label4.setStyleSheet('color:black')
        vbox.addWidget(self.label4)
        # Insert the word to erase line
        self.lineedit3 = QTextEdit(self)
        self.lineedit3.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit3.textChanged.connect(self.save_text)
        vbox.addWidget(self.lineedit3)
        
        # Insert Text for the CSV name
        self.label5 = QLabel("4) The name of Csv File, and Enter")
        self.label5.setFont(QtGui.QFont("Sanserif", 15))
        self.label5.setStyleSheet('color:black')
        vbox.addWidget(self.label5)
        # Insert the word to erase line
        self.lineedit4 = QTextEdit(self)
        self.lineedit4.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit4.textChanged.connect(self.save_text)
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
        self.button.clicked.connect(self.search1)
        gridLayout.addWidget(self.button, 0,0)
        #Second button Show/Hide the Terminal
        self.button2 = QPushButton("Show/Hide", self)
        self.button2.setWhatsThis("Show/Hide the Terminal to see progression")
        self.button2.setIcon(QtGui.QIcon("C:\gitproject\projet3\images\hide.png"))
        self.button2.setIconSize(QtCore.QSize(40, 40))
        self.button2.setMinimumHeight(40)
        gridLayout.addWidget(self.button2, 0,1)
        

        self.groupBox.setLayout(gridLayout)
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)
        self.show()
        
    def save_text(self):
        if self.lineedit:
            self.text = self.lineedit.toPlainText()
            #print (text)
        if self.lineedit5:
            self.text5 = self.lineedit5.toPlainText()
            #print (text5)
        if self.lineedit:
            self.text2 = self.lineedit2.toPlainText()
            #print (text2)
        if self.lineedit3:
            self.text3 = self.lineedit3.toPlainText()
            #print (text3)
        if self.lineedit4:
            self.text4 = self.lineedit4.toPlainText()
            #print (text4)
        return self.text, self.text2, self.text3, self.text4, self.text5
        
    
    
    
    def search1(self):
        
        for i in range (1,int(self.text2),1):
            gribou=self.text+str(i)
            result2 = requests.get (gribou)
            a=result2.status_code
            print (a)
            soup = BeautifulSoup(result2.text, 'html.parser')
            for a in soup.find_all('a'):
                fullstring= a.get('href')
                if fullstring is None:
                    continue
                if substring in fullstring:
                    my_list.append(self.text5+fullstring)

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
                bloublou2=bloublou2.replace(self.text3, '')
            
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
        df2.to_csv(self.text4+".csv", index=False, encoding="utf_8_sig")


    
        

#Main class
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec())