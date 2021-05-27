# -*- coding: utf-8 -*-
"""
Created on Wed May 27 17:16:11 2020

@author: Mark_T
@title : Splash Screen UI Element(with dialog box)

"""
import sys, time
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (QDialog, QPushButton, QVBoxLayout,
                             QApplication, QSplashScreen)
from PyQt5.QtCore import QTimer


class SplashScreen(QDialog):
    def __init__(self, parent=None):
       super(SplashScreen,self).__init__(parent)
       self.flashSplash()       
       self.b1 = QPushButton("Display ScreenSaver")
       self.b1.clicked.connect(self.flashSplash)
       layout = QVBoxLayout()
       self.setLayout(layout)
       layout.addWidget(self.b1)
        
        
    def flashSplash(self):
        self.splash = QSplashScreen(QPixmap('splash.jpg')) #Bydefault, SplashScreen will be in center of the screen.
        #You can move it to a specific location if you want.
        #self.splash.move(10,10)        
        self.splash.show()
        for x in range(100,151):
            self.splash.showMessage('Initializing   '+str(x)+'   Initializing')
            time.sleep(0.2)
        #Close Splash Screen after 2 seconds(2000ms)
        QTimer.singleShot(2000,self.splash.close)
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    splashScreen = SplashScreen()
    splashScreen.show()    
    sys.exit(app.exec_())
         
         
 
