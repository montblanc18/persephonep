#!/usr/bin/env python
# coding: utf-8
#

# from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
#                             QTabWidget, QApplication,
#                             QVBoxLayout, QLabel, QDesktopWidget, QStatusBar)
# from PyQt5.QtGui import QIcon
import PyQt5.QtCore
import pytest
from pytestqt.qt_compat import qt_api


from persephonep import persephonep

def test_add_button(qtbot):
    # app = QApplication(sys.argv) # これ入れるとセグフォする

    # setWindowIcon is a method for QApplication, not for QWidget
    # path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    # app.setWindowIcon(QIcon(path))
    return 
    # ui = persephonep.PersephonepMainWindow()

    # qt_api.qWarning('test')

    # qtbot.addWidget(ui)
    # qtbot.mouseClick(ui.table_widget.add_button, PyQt5.QtCore.Qt.LeftButton)
    # assert ui.table_widget.add_button.text() == '+'
