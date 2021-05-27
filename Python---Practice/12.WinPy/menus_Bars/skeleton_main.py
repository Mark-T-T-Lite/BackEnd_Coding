# -*- coding: utf-8 -*-
"""
Created on Thu May 28 01:54:50 2020

@author: Mark_T
"""

import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication,QFileDialog
from PyQt5.QtGui import QIcon


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        
        openAct = QAction(QIcon('new1.png'), 'Open...', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open a File')
        openAct.triggered.connect(self.openFileNameDialog)
        
        saveAct = QAction(QIcon('save1.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save Changes')
        #saveAct.triggered.connect(self.saveFile)
        
        saveAsAct = QAction(QIcon('save1.png'), 'Save As', self)
        saveAsAct.setShortcut('Ctrl+Shift+S')
        saveAsAct.setStatusTip('Save As')
        saveAsAct.triggered.connect(self.saveFileDialog)


        self.statusBar()

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(exitAct)

        #toolbar = self.addToolBar('Exit')
        #toolbar.addAction(exitAct)

        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
            
    def saveFileDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            print(fileName)            
        
   

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()