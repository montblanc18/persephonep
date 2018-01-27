#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, 
                             QTextEdit, QGridLayout, QApplication, QPushButton,  QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineProfile, QWebEngineDownloadItem

__program__ = 'PERSEPHONE'


class PersephoneWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.initUI()
        
        
    def initUI(self):
        
        initurl = 'https://www.google.co.jp'

        # setting window
        self.window = QWebEngineView()
        self.window.load(QUrl(initurl))        
        self.window.resize(1000,600)
        self.window.move(200,200)
        self.window.setWindowTitle(__program__)

        # setting button
        self.back_button = QPushButton('back')
        self.back_button.setToolTip('Go back to previous page.')
        self.back_button.clicked.connect(self.window.back)        
        self.forward_button = QPushButton('forward')
        self.forward_button.setToolTip('Go to the next page.')
        self.forward_button.clicked.connect(self.window.forward)
        self.reload_button = QPushButton('reload')
        self.reload_button.setToolTip('Reload this page.')
        self.reload_button.clicked.connect(self.window.reload)
        self.url_edit = QLineEdit()
        self.url_edit.setToolTip('URL box')
        self.move_button = QPushButton('move')
        self.move_button.setToolTip('Move to the page set at URL box.')
        self.move_button.clicked.connect(self.loadPage)
        self.home_button = QPushButton('home')
        self.home_button.setToolTip('Move to the home page.')
        self.home_button.clicked.connect(self.loadHomePage)
        
        # signal catch from moving web pages.
        self.window.urlChanged.connect(self.updateCurrentUrl)
        self.window.page().profile().downloadRequested.connect(self._downloadRequested)
        
        # setting layout
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.move_button, 1, 14)
        grid.addWidget(self.home_button, 1, 15)
        grid.addWidget(self.window,2, 0, 5, 16)
        self.setLayout(grid) 
        self.resize(1200, 800)
        self.center()
        self.setWindowTitle(__program__)
        self.show()

    
    def center(self):
        ''' centering widget
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        
    def loadPage(self):
        ''' move web page which is set at url_edit
        '''
        move_url = QUrl(self.url_edit.text())
        self.window.load(move_url)
        self.updateCurrentUrl

    def updateCurrentUrl(self):
        ''' rewriting url_edit when you move different web page.
        '''
        # current_url = self.window.url().toString()
        self.url_edit.clear()
        self.url_edit.insert(self.window.url().toString())

    def loadHomePage(self):
        ''' move to the home page
        '''
        initurl = 'https://www.google.co.jp'
        self.window.load(QUrl(initurl))

    def saveFile(self):
        print('download')

    def _downloadRequested(self, item): # QWebEnginDownloadItem
        # print('downloading to', item.path)
        item.accept()
        
        
if __name__ == '__main__':
    # mainPyQt5()
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ex = PersephoneWindow()
    sys.exit(app.exec_())
            
    
    
