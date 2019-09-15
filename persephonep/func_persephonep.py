#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
from PyQt5.QtWidgets import (QWidget, QLineEdit,
                             QGridLayout, QLabel, QDialog,
                             QHBoxLayout,
                             QApplication, QPushButton, QDesktopWidget)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView


__program__ = 'PERSEPHONEP'

''' This is a single page of the browser.
    This class equals a tab of PersephonepTableWidget.
    This class can run only this python script, however,
    that is not recomended.
    (This ability might be deleted in the near future.)
'''


def program_name():
    return __program__

class DownloadWindow(QWidget):

    def __init__(self, item, parent=None):
        # こいつがサブウィンドウの実体？的な。ダイアログ
        super(DownloadWindow, self).__init__()
        self.w = QDialog(parent)
        self.label = QLabel()
        self.item = item
        self.label.setText('Downloading {}'.format(self.item.path()))
        layout = QHBoxLayout()
        layout.addWidget(self.label)
        self.item.accept()
        print(self.item.totalBytes())
        self.item.finished.connect(self.finish_download)
        # item = QWebEngineDownloadItem has 4 Signals, downloadProgress, finished, isPausedChanged, stateChanged.
        self.w.setLayout(layout)

    def show(self):
        self.w.exec_()

    def finish_download(self):
        self.label.setText('Finish to download {}'.format(self.item.path()))
        print('finish')


class PersephonepWindow(QWidget):

    def __init__(self, parent=None):
        super(PersephonepWindow, self).__init__()

        self.initUI(parent=parent)

    def initUI(self, parent=None):

        # config
        initurl = 'https://www.google.co.jp'

        # setting window
        self.window = QWebEngineView()

        # disguise
        # profile = QWebEngineProfile()
        # profile.setHttpUserAgent('IE')
        # page = QWebEnginePage(profile)
        # self.window.setPage(page)
        # print(
        #    # Set user agent "{}"
        #   .format(
        #        self.window.page().profile().httpUserAgent()
        #    )
        #)

        # condig url
        self.window.load(QUrl(initurl))
        self.window.resize(1000, 600)
        self.window.move(200, 200)
        self.window.setWindowTitle(program_name())

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
        self.url_edit.returnPressed.connect(self.loadPage)
        self.home_button = QPushButton('home')
        self.home_button.setToolTip('Move to the home page.')
        self.home_button.clicked.connect(self.loadHomePage)

        # signal catch from moving web pages.
        self.window.urlChanged.connect(self.updateCurrentUrl)
        self.window.page().profile().\
            downloadRequested.connect(self._downloadRequested)

        # setting layout
        grid = QGridLayout()
        grid.setSpacing(0)
        grid.addWidget(self.back_button, 1, 0)
        grid.addWidget(self.forward_button, 1, 1)
        grid.addWidget(self.reload_button, 1, 2)
        grid.addWidget(self.url_edit, 1, 3, 1, 10)
        grid.addWidget(self.move_button, 1, 14)
        grid.addWidget(self.home_button, 1, 15)
        grid.addWidget(self.window, 2, 0, 5, 16)
        self.setLayout(grid)

        if parent is None:
            self.resize(1200, 800)
            self.center()
            self.setWindowTitle(program_name())
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
        If the head of move_url equals 'http://' or 'https://',
        query to google search form.
        If the head of move_url doed not include above protocol,
         but the style of *.*.*.*, add http:// to its_head
        '''
        move_url = self.url_edit.text()
        if self.check_url_protocol_ipv4(move_url):
            move_url = 'http://' + move_url
        elif not self.check_url_protocol(move_url):
            search_word = move_url.replace(' ', '+').replace('　', '+')
            google_search_url = \
                'https://www.google.co.jp' \
                '/search?ie=utf-8&oe=utf-8&q={}&' \
                'hl=ja&btnG=search'.format(search_word)
            move_url = google_search_url
        move_url = QUrl(move_url)
        self.window.load(move_url)
        self.updateCurrentUrl()

    def check_url_protocol(self, move_url):
        if (move_url[0:7] == 'http://' or
                move_url[0:8] == "https://" or
                move_url[0:8] == 'file:///' or
                move_url[0:6] == 'ftp://'):
            return True
        else:
            return False

    def check_url_protocol_ipv4(self, move_url):
        ''' return True if move_url is IPv4 using Regular expression
        '''
        pattern = '(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\\.)' \
                  '{3}([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'
        return re.match(pattern, move_url)

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

    def _downloadRequested(self, item):  # QWebEngineDownloadItem
        # print('downloading to', item.path)
        item.accept()
        
        dw = DownloadWindow(item)
        dw.show()
        

if __name__ == '__main__':
    # mainPyQt5()
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__),
                        'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ex = PersephonepWindow()
    sys.exit(app.exec_())
