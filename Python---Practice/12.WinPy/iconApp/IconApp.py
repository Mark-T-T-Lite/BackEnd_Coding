# -*- coding: utf-8 -*-
"""
Created on Tue May 26 15:27:47 2020

@author: Mark_T
"""

import sys
from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.QtGui import QIcon

class IconCreate(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()

    def initUI(self):            
        self.setGeometry(300,300,300,220)
        self.setWindowTitle("IconApp")
        self.setWindowIcon(QIcon('icon.png'))
        
        self.show()
        sys.exit(app.exec_())
        
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    icon = IconCreate()
    