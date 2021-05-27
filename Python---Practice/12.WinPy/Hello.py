# -*- coding: utf-8 -*-
"""
Created on Tue May 26 13:54:36 2020

@author: Mark_T
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget 

def main():
    app = QApplication(sys.argv)
    w = QWidget()    
    #w.setGeometry(300,300,250,150)    
    w.setWindowTitle("Hello World")
    w.show()
    
    sys.exit(app.exec_())
    
if __name__ == '__main__':
    main()
    