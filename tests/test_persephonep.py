#!/usr/bin/env python
# coding: utf-8
#

import pytest
import unittest
import sys
import os
import argparse
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTabWidget, QApplication,
                             QVBoxLayout, QLabel, QDesktopWidget, QStatusBar)
from PyQt5.QtGui import QIcon
import PyQt5.QtCore

from persephonep import * 
from func_persephonep import *

def test_add_button(qtbot):
    return 0
'''
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    # ui = PersephonepMainWindow()
    ui = create_main_window(app)

    qWarning('test')

    qtbot.addWidget(ui)
    qtbot.mouseClick(ui.table_widget.add_button, PyQt5.QtCore.Qt.LeftButton)
    assert ui.table_widget.add_button.text() == '+'
'''


''''
def test_check_url_protocol():

    # mainPyQt5()
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ex = PersephonepWindow()

    # assert ex.check_url_protocol('http://127.0.0.1') == True
    #assert ex.check_url_protocol('https://127.0.0.1') == True
    #assert ex.check_url_protocol('ftp://127.0.0.1') == True
    #assert ex.check_url_protocol('file://127.0.0.1') == True


class TestPersephonep(unittest.TestCase):

    def setUp(self):
        app = QApplication(sys.argv)

        # setWindowIcon is a method for QApplication, not for QWidget
        path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
        app.setWindowIcon(QIcon(path))

        # app.setApplicationName('IE')
        # app.setApplicationVersion('1.0')

        self.ui = PersephonepMainWidget()
        sys.exit(app.exec_())

    def test_persephonep_table_widget(self):
        self.ui._addTab(1)
        self.ui.closeTab(1)

        # We must write destracter?
'''