#!/usr/bin/env python
# coding: utf-8
#

# URLの追加
# タブ
# reload


import sys
#
# I do not use pyside but pyqt
# That's because Anaconda does not include pyside defaultly.
# 
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5 import QtWebEngineWidgets

def mainPyQt5():
    url = 'https://www.google.co.jp'
    app = QtWidgets.QApplication(sys.argv)
    
    # QWebEgineViewによるWebページ表示
    browser = QtWebEngineWidgets.QWebEngineView()
    browser.load(QtCore.QUrl(url))
    browser.show()

    # Application Main Loop
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    mainPyQt5()
