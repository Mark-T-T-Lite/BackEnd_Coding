# -*- coding: utf-8 -*-
"""
Created on Thu May 28 00:06:45 2020

@author: Mark_T
"""

import sys
from PyQt5.QtWidgets import QApplication, QLabel 
from PyQt5.QtCore import QTimer, Qt 

if __name__ == '__main__': 
    app = QApplication(sys.argv) 
    label = QLabel("""<img src = splash.jpg
                   <font color=red size=12> 
                   <p>Hello PyQt， The window will disappear after 5 seconds！</p> 
                   </font>>""") 
   
    # SplashScreen - Indicates that the window is a splash screen.This is the default type for .QSplashScreen 
    # FramelessWindowHint - Creates a borderless window. The user cannot move or resize the borderless window through the window system. 
    label.setWindowFlags(Qt.SplashScreen | Qt.FramelessWindowHint) 
    label.show() 
    # Automatically exit after 5 seconds 
    QTimer.singleShot(5000, app.quit) 
    sys.exit(app.exec_())