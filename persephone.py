#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
ZetCode PyQt5 tutorial 

In this example, we create a bit
more complicated window layout using
the QGridLayout manager. 

author: Jan Bodnar
website: zetcode.com 
last edited: January 2015
"""

import sys
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
                             QTextEdit, QGridLayout, QApplication, QPushButton,  QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

__program__ = 'PERSEPHONE'


class PersephoneWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):

        initurl = 'https://www.google.co.jp'
                
        self.browser = QWebEngineView()
        self.browser.load(QUrl(initurl))        
        self.browser.resize(1000,600)
        self.browser.move(200,200)
        self.browser.setWindowTitle(__program__)

        self.back_button = QPushButton('back')
        self.back_button.clicked.connect(self.browser.back)        
        self.forward_button = QPushButton('forward')
        self.forward_button.clicked.connect(self.browser.forward)
        self.reload_button = QPushButton('reload')
        self.reload_button.clicked.connect(self.browser.reload)
        self.url_edit = QLineEdit()
        self.move_button = QPushButton('move')
        print(self.url_edit.text())
        # move_button.clicked.connect(browser.load(QUrl(url_edit.text())))
        self.move_button.clicked.connect(self.loadPage)
        
        self.browser.urlChanged.connect(self.updateCurrentUrl)
        
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.move_button, 1, 14)

        grid.addWidget(self.browser,2, 0, 5, 15)

        self.setLayout(grid) 
        
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle(__program__)
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def loadPage(self):
        move_url = QUrl(self.url_edit.text())
        self.browser.load(move_url)
        self.updateCurrentUrl

    def updateCurrentUrl(self):
        # current_url = self.browser.url().toString()
        self.url_edit.clear()
        self.url_edit.insert(self.browser.url().toString())
    
if __name__ == '__main__':
    # mainPyQt5()
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ex = PersephoneWindow()
    sys.exit(app.exec_())
            
    
    
