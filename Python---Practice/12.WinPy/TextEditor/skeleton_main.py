# -*- coding: utf-8 -*-
"""
Created on Thu May 28 01:54:50 2020

@author: Mark_T
"""

import sys,os,time
from PyQt5.QtWidgets import (QMainWindow, QPlainTextEdit, QAction, QApplication,
                             QFileDialog, QMenu, QFontComboBox, QComboBox, QLabel,
                             QMessageBox,QDialog,QTextEdit,QPushButton,QCheckBox)

from PyQt5.QtGui import QIcon,QTextDocument,QFont,QFontDatabase
from PyQt5.QtCore import Qt
from PyQt5.QtPrintSupport import QPrintPreviewDialog,QPrintDialog#, QPrinter
from splash import SplashScreen

cs = False
wwo = False
fnd = False

timeStr = str(time.asctime())

class Find(QDialog):
    def __init__(self,parent = None):
        QDialog.__init__(self, parent)
        
         
        self.initUI()
 
    def initUI(self):
 
        self.lb1 = QLabel("Search for: ",self)
        self.lb1.setStyleSheet("font-size: 15px; ")
        self.lb1.move(10,10)
 
        self.te = QTextEdit(self)
        self.te.move(10,40)
        self.te.resize(250,25)
 
        self.src = QPushButton("Find",self)
        self.src.move(270,40)
        
        if fnd: 
            self.lb2 = QLabel("Replace all by: ",self)
            self.lb2.setStyleSheet("font-size: 15px; ")
            self.lb2.move(10,80)
     
            self.rp = QTextEdit(self)
            self.rp.move(10,110)
            self.rp.resize(250,25)
     
            self.rpb = QPushButton("Replace",self)
            self.rpb.move(270,110)
 
        self.opt1 = QCheckBox("Case sensitive",self)
        self.opt1.move(10,160)
        self.opt1.stateChanged.connect(self.CS)
         
        self.opt2 = QCheckBox("Whole words only",self)
        self.opt2.move(10,190)
        self.opt2.stateChanged.connect(self.WWO)
 
        self.close = QPushButton("Close",self)
        self.close.move(270,220)
        self.close.clicked.connect(self.Close)
         
         
        self.setGeometry(300,300,360,250)
        
    def CS(self, state):
        global cs
 
        if state == Qt.Checked:
            cs = True
        else:
            cs = False
 
    def WWO(self, state):
        global wwo
        print(wwo)
 
        if state == Qt.Checked:
            wwo = True
        else:
            wwo = False
 
    def Close(self):
        self.hide()
 

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.initUI()


    def initUI(self):
        
        self.textEditor = QTextEdit()  
        self.textEditor.setTabStopWidth(12)        
        self.setCentralWidget(self.textEditor)
        
        # Setup the QTextEdit editor configuration
        fixedfont = QFontDatabase.systemFont(QFontDatabase.FixedFont)
        fixedfont.setPointSize(12)
        self.textEditor.setFont(fixedfont)
#        
        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.filePath = None
        
#-------- Menu Bar --------------------------------------------------------
    #-------- File Menu --------------------------------------------------------
        
        newAct = QAction(QIcon('new1.png'), 'New...', self)
        newAct.setShortcut('Ctrl+N')
        newAct.setStatusTip('Exit application')
        newAct.triggered.connect(self.newFile)
        
        newWindowAct = QAction(QIcon('exit24.png'), 'New Window', self)
        newWindowAct.setShortcut('Ctrl+Q')
        newWindowAct.setStatusTip('Exit application')
        newWindowAct.triggered.connect(self.newWindow)
        
        openAct = QAction(QIcon('new1.png'), 'Open...', self)
        openAct.setShortcut('Ctrl+O')
        openAct.setStatusTip('Open a File')
        openAct.triggered.connect(self.openFileNameDialog)
        
        saveAct = QAction(QIcon('save1.png'), 'Save', self)
        saveAct.setShortcut('Ctrl+S')
        saveAct.setStatusTip('Save Changes')
        saveAct.triggered.connect(self.saveFile)
        
        saveAsAct = QAction(QIcon('save1.png'), 'Save As', self)
        saveAsAct.setShortcut('Ctrl+Shift+S')
        saveAsAct.setStatusTip('Save As')
        saveAsAct.triggered.connect(self.saveFileAsDialog)
        
        pageSetupAct = QAction(QIcon('save1.png'), 'Page Setup', self)
        #pageSetupAct.setShortcut('Ctrl+S')
        pageSetupAct.setStatusTip('Save Changes')
        pageSetupAct.triggered.connect(self.pageSetup)
        
        printAct = QAction(QIcon('save1.png'), 'Print', self)
        printAct.setShortcut('Ctrl+P')
        printAct.setStatusTip('Save As')
        printAct.triggered.connect(self.printFile)

        exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        exitAct.setShortcut('Alt+F4')
        exitAct.setStatusTip('Exit application')
        exitAct.triggered.connect(self.close)
        
        #-------- Edit Menu --------------------------------------------------------
        undoAct = QAction(QIcon('new1.png'), 'Undo', self)
        undoAct.setShortcut('Ctrl+Z')
        undoAct.setStatusTip('Exit application')
        undoAct.triggered.connect(self.Undo)
        
        redoAct = QAction(QIcon('new1.png'), 'Redo', self)
        #redoAct.setShortcut('Ctrl+N')
        redoAct.setStatusTip('Exit application')
        redoAct.triggered.connect(self.Redo)
        
        cutAct = QAction(QIcon('exit24.png'), 'Cut', self)
        cutAct.setShortcut('Ctrl+X')
        cutAct.setStatusTip('Exit application')
        cutAct.triggered.connect(self.Cut)
        
        copyAct = QAction(QIcon('new1.png'), 'Copy', self)
        copyAct.setShortcut('Ctrl+C')
        copyAct.setStatusTip('Open a File')
        copyAct.triggered.connect(self.Copy)
        
        pasteAct = QAction(QIcon('save1.png'), 'Paste', self)
        pasteAct.setShortcut('Ctrl+V')
        pasteAct.setStatusTip('Save Changes')
        pasteAct.triggered.connect(self.Paste)
        
        swbAct = QAction(QIcon('save1.png'), 'Search With Bing', self)
        #swbAct.setShortcut('Ctrl+Shift+S')
        swbAct.setStatusTip('Save As')
        #swbAct.triggered.connect(self.saveFileDialog)
        
        findAct = QMenu('Find', self)
        #findAct.setShortcut('Ctrl+S')
        #findAct.setStatusTip('Save Changes')
        #findAct.triggered.connect(self.saveFile)      

            #-------- Find Sub Menu -------------------------------------------------
        finderAct = QAction(QIcon('save1.png'), 'Find', self)
        finderAct.setShortcut('Ctrl+F')
        finderAct.setStatusTip('Save Changes')
        finderAct.triggered.connect(self.Finder)
         
        findNextAct = QAction(QIcon('save1.png'), 'Find Next', self)
        #findNextAct.setShortcut('Ctrl+Shift+F')
        findNextAct.setStatusTip('Save As')
        findNextAct.triggered.connect(self.Finder)
        
        findPreviousAct = QAction(QIcon('exit24.png'), 'Find Previous', self)
        #findPreviousAct.setShortcut('Ctrl+Q')
        findPreviousAct.setStatusTip('Exit application')
        findPreviousAct.triggered.connect(self.Finder)
 
        
        findAct.addAction(finderAct)
        findAct.addAction(findNextAct)
        findAct.addAction(findPreviousAct)
            #--------------------------------------------------------------------------
        
        
        replaceAct = QAction(QIcon('save1.png'), 'Replace', self)
        replaceAct.setShortcut('Ctrl+H')
        replaceAct.setStatusTip('Save Changes')
        replaceAct.triggered.connect(self.Replacer)
        
        gotoAct = QAction(QIcon('save1.png'), 'Go to', self)
        gotoAct.setShortcut('Ctrl+G')
        gotoAct.setStatusTip('Save As')
        #gotoAct.triggered.connect(self.saveFileDialog)

        selectAllAct = QAction(QIcon('exit24.png'), 'Select All', self)
        selectAllAct.setShortcut('Ctrl+A')
        selectAllAct.setStatusTip('Exit application')
        selectAllAct.triggered.connect(self.SelectAll)
        
        timeDateAct = QAction(QIcon('exit24.png'), 'Time/Date', self)
        timeDateAct.setShortcut('F5')
        timeDateAct.setStatusTip('Exit application')
        timeDateAct.triggered.connect(self.insertDate)
        
        #-------- Format Menu -------------------------------------------------------- 
        wordWrapAct = QAction(QIcon('exit24.png'), 'Word Wrap', self)
        #wordWrapAct.setShortcut('Ctrl+Q')
        wordWrapAct.setStatusTip('Exit application')
        wordWrapAct.triggered.connect(self.close)
        
        fontAct = QAction(QIcon('exit24.png'), 'Font', self)
        #fontAct.setShortcut('Ctrl+Q')
        fontAct.setStatusTip('Exit application')
        fontAct.triggered.connect(self.close)
        
        #-------- View Menu -------------------------------------------------------- 
        zoomAct = QMenu('Zoom', self)
        #zoomAct.setShortcut('Ctrl+Q')
        #zoomAct.setStatusTip('Exit application')
        #zoomAct.triggered.connect(self.close)
        
            #-------- Zoom Sub Menu -------------------------------------------------
        zoomInAct = QAction(QIcon('exit24.png'), 'Zoom In', self)
        #zoomInAct.setShortcut('Ctrl+Q')
        zoomInAct.setStatusTip('Exit application')
        zoomInAct.triggered.connect(self.close)
        
        zoomOutAct = QAction(QIcon('exit24.png'), 'Zoom Out', self)
        #zoomOutAct.setShortcut('Ctrl+Q')
        zoomOutAct.setStatusTip('Exit application')
        zoomOutAct.triggered.connect(self.close)
        
        restoreZoomAct = QAction(QIcon('exit24.png'), 'Restore Default Zoom', self)
        #restoreZoomAct.setShortcut('Ctrl+Q')
        restoreZoomAct.setStatusTip('Exit application')
        restoreZoomAct.triggered.connect(self.close)
        
        zoomAct.addAction(zoomInAct)
        zoomAct.addAction(zoomOutAct)
        zoomAct.addAction(restoreZoomAct)
            #-------------------------------------------------------------------------
        
        statusBarAct = QAction(QIcon('exit24.png'), 'Status Bar', self)
        #statusBarAct.setShortcut('Ctrl+Q')
        statusBarAct.setStatusTip('Exit application')
        statusBarAct.triggered.connect(self.close)
        
        #-------- Help Menu -------------------------------------------------------- 
        
        viewHelpAct = QAction(QIcon('exit24.png'), 'View Help', self)
        #viewHelpAct.setShortcut('Ctrl+Q')
        viewHelpAct.setStatusTip('Exit application')
        viewHelpAct.triggered.connect(self.close)
        
        sendFeedBackAct = QAction(QIcon('exit24.png'), 'Send FeedBack', self)
        #sendFeedBackAct.setShortcut('Ctrl+Q')
        sendFeedBackAct.setStatusTip('Exit application')
        sendFeedBackAct.triggered.connect(self.close)
        
        aboutNotesAct = QAction(QIcon('exit24.png'), 'About Notes', self)
        #aboutNotesAct.setShortcut('Ctrl+Q')
        aboutNotesAct.setStatusTip('Exit application')
        aboutNotesAct.triggered.connect(self.close)
        
        
        #------- Statusbar ------------------------------------
         
        self.status = self.statusBar()        
        self.textEditor.cursorPositionChanged.connect(self.CursorPosition)
 
 

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(newAct)
        fileMenu.addAction(newWindowAct)
        fileMenu.addAction(openAct)
        fileMenu.addAction(saveAct)
        fileMenu.addAction(saveAsAct)
        fileMenu.addAction(pageSetupAct)
        fileMenu.addAction(printAct)
        fileMenu.addAction(exitAct)
        
        editMenu = menubar.addMenu('&Edit')
        editMenu.addAction(undoAct)
        editMenu.addAction(redoAct)
        editMenu.addAction(cutAct)
        editMenu.addAction(copyAct)
        editMenu.addAction(pasteAct)
        editMenu.addAction(swbAct)
        editMenu.addMenu(findAct)
        editMenu.addAction(replaceAct)
        editMenu.addAction(gotoAct)
        editMenu.addAction(selectAllAct)
        editMenu.addAction(timeDateAct)
        
        formatMenu = menubar.addMenu('&Format')
        formatMenu.addAction(wordWrapAct)
        formatMenu.addAction(fontAct)
                           
        viewMenu = menubar.addMenu('&View')
        viewMenu.addMenu(zoomAct)
        viewMenu.addAction(statusBarAct)        
       
        helpMenu = menubar.addMenu('&Help')
        helpMenu.addAction(viewHelpAct)
        helpMenu.addAction(sendFeedBackAct)
        helpMenu.addAction(aboutNotesAct)               
        
        #-------- FONT Options -------------------------------------------------------
        self.fontFamily = QFontComboBox(self)
        self.fontFamily.currentFontChanged.connect(self.FontFamily)
 
        fontSize = QComboBox(self)
        fontSize.setEditable(True)
        fontSize.setMinimumContentsLength(3)
        fontSize.activated.connect(self.FontSize)
        flist = [6,7,8,9,10,11,12,13,14,15,16,18,20,22,24,26,28,32,36,40,44,48,
                 54,60,66,72,80,88,96]
         
        for i in flist:
            fontSize.addItem(str(i))
            
        space1 = QLabel("  ",self)
        space2 = QLabel(" ",self)
        #space3 = QLabel(" ",self)
         
 
        self.formatbar = self.addToolBar("Format")
        self.formatbar.addWidget(self.fontFamily)
        self.formatbar.addWidget(space1)
        self.formatbar.addWidget(fontSize)
        self.formatbar.addWidget(space2)    
            
        self.setGeometry(100, 100, 500, 500)
        self.updateWindowtitle()
        self.show()
        
        
    #-------- File Actions -------------------------------------------------------    
    def newFile(self):
        self.textEditor.clear()
                 
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog      
        filePath, _ = QFileDialog.getOpenFileName(self, "Open file", "", "Text documents (*.txt);;All files (*.*)", options=options)

        if filePath:
            
            try:
                with open(filePath, 'rU') as f:
                    text = f.read()

            except Exception as e:
                self.exception_Dialog(str(e))

            else:
                self.filePath = filePath
                self.editor.setPlainText(text)
                self.update_title()
                
    def saveFile(self):

        if self.filePath is None:
            # If we do not have a path, we need to use Save As.
            return self.saveFileAsDialog()
        
        self.saveFileToPath(self.filePath)       
              
            
    def saveFileAsDialog(self):
        options = QFileDialog.Options()
        #options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getSaveFileName(self,"Save As","","All Files (*);;Text Files (*.txt)", options=options)
        
        if not filePath:
            # If dialog is cancelled, will return ''
            return

        self.saveFileToPath(filePath)
            
    def saveFileToPath(self,filePath):
        text = self.textEditor.toPlainText()
        try:
            with open(filePath, 'w') as f:
                f.write(text)

        except Exception as e:
            self.exception_Dialog(str(e))

        else:
            self.filePath = filePath
            self.updateWindowtitle()  

    def pageSetup(self):
        preview = QPrintPreviewDialog()        
        preview.paintRequested.connect(self.PrintPageView)
        preview.exec_()  

    def printPageView(self, printer):
        self.text.print_(printer)   

    def printFile(self):
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.text.document().print_(dialog.printer())
      
                        
    #-------- Edit Actions -------------------------------------------------------  
    def Undo(self):
        self.textEditor.undo()
 
    def Redo(self):
        self.textEditor.redo()
 
    def Cut(self):
        self.textEditor.cut()
 
    def Copy(self):
        self.textEditor.copy()
 
    def Paste(self):
        self.textEditor.paste()
        
    def SelectAll(self):
        self.textEditor.selectAll()          
        
    def Finder(self):
        global f 
                 
        find = Find(self)
        find.show()
 
        def handleFind():
 
            f = find.te.toPlainText()
            print(f)
             
            if cs == True and wwo == False:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively
                 
            elif cs == False and wwo == False:
                flag = QTextDocument.FindBackward
                 
            elif cs == False and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindWholeWords
                 
            elif cs == True and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively and QTextDocument.FindWholeWords
             
            self.textEditor.find(f,flag)

        find.src.clicked.connect(handleFind)
    
    def Replacer(self):
        global f,fnd 
        fnd = True 
         
        find = Find(self)
        find.show()
 
        def handleFind():
 
            f = find.te.toPlainText()
            print(f)
             
            if cs == True and wwo == False:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively
                 
            elif cs == False and wwo == False:
                flag = QTextDocument.FindBackward
                 
            elif cs == False and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindWholeWords
                 
            elif cs == True and wwo == True:
                flag = QTextDocument.FindBackward and QTextDocument.FindCaseSensitively and QTextDocument.FindWholeWords
             
            self.textEditor.find(f,flag)
 
        def handleReplace():
            fi = find.te.toPlainText()
            r = find.rp.toPlainText()
            
 
            text = self.textEditor.toPlainText()
             
            newText = text.replace(fi,r)
            print(newText)
 
            self.textEditor.clear()
            self.textEditor.append(newText)
         
        find.src.clicked.connect(handleFind)
        find.rpb.clicked.connect(handleReplace)
                
    def insertDate(self):
        global timeStr
        print(timeStr)
        self.textEditor.append(timeStr)
        
        
         
    def CursorPosition(self):
        line = self.textEditor.textCursor().blockNumber()
        col = self.textEditor.textCursor().columnNumber()
        linecol = ("Line: "+str(line)+" | "+"Column: "+str(col))
        self.status.showMessage(linecol)
 
    def FontFamily(self,font):
        font = QFont(self.fontFamily.currentFont())
        self.textEditor.setCurrentFont(font)
 
    def FontSize(self, fsize):
        size = (int(fsize))
        self.textEditor.setFont(size)
      
    def exception_Dialog(self, s):
        dlg = QMessageBox(self)
        dlg.setText(s)
        dlg.setIcon(QMessageBox.Critical)
        dlg.show()            
        
    def newWindow(self):
        window2 = MainWindow()          
        
   
    def updateWindowtitle(self):
        self.setWindowTitle("%s - Notes" % (os.path.basename(self.filePath) if self.filePath else "Untitled"))

def main():
    app = QApplication(sys.argv)
    app.setApplicationName('Notes')
    splashScreen = SplashScreen()
    #splashScreen.flashSplash()
    window = MainWindow()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()