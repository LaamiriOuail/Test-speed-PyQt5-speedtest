from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QWidget):
    def __init__(self,wwith,wheigth,title,iconImage,bakgroundImage,styleCSS,fixedSize):
        super().__init__()
        if fixedSize==True or fixedSize==1 : 
            self.setFixedSize(wwith,wheigth)
        else:
            self.resize(wwith,wheigth)
        self.setStyleSheet(styleCSS)
        self.setWindowTitle(title)
        self.setWindowIcon(QIcon(iconImage))
        label = QLabel(self)
        pixmap = QPixmap(bakgroundImage).scaled(wwith,wheigth)
        label.setPixmap(pixmap)
        
    def newButton(self,left,top,lwith,lheigth,styleCSS,title,event):
        name =QPushButton(title,self)
        name.setStyleSheet(styleCSS)
        name.setGeometry(left,top,lwith,lheigth)
        name.clicked.connect(event)
        """
        in function with Parameter :
        from functools import partial
        event=partial(nameFunction,parametre1=...,parametre2=...,...) 
        or event=partial(nameFunction,value1,value2,...) avec parametre1=value1,parametre2=value2,...
        """
        return name
    def newLabel(self,left,top,lwith,lheight,styleCSS,titleHTML,textCenter):
        name =QLabel(titleHTML,self)
        name.setGeometry(left,top,lwith,lheight)
        name.setStyleSheet(styleCSS)
        if textCenter==True or textCenter==1 :
           name.setAlignment(Qt.AlignCenter) 
        return name
    def newInput(self,left,top,iwith,iheight,style,placeholder,textCenter,passwordInput):
        name = QLineEdit(self)
        name.setPlaceholderText(placeholder)
        name.setStyleSheet(style)
        name.move(left,top)
        name.resize(iwith,iheight)
        if textCenter==True or textCenter==1 :
           name.setAlignment(Qt.AlignCenter)
        if passwordInput==True or passwordInput==1:
            name.setEchoMode(QLineEdit.Password)
        return name
    

