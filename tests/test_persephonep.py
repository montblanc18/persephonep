#!/usr/bin/env python
# coding: utf-8
#

import unittest
from persephonep import *
import PyQt5.QtCore


def test_perseponep(qtbot):
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    ui = PersephonepMainWidget()

    qtbot.addWidget(ui)
    qtbot.mouseClick(ui.table_widget.add_button, PyQt5.QtCore.Qt.LeftButton)
    assert ui.table_widget.add_button.text() == '+'

'''
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