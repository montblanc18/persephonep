#!/usr/bin/env python
# coding: utf-8
#
"""Control tab of browser."""

from PyQt6.QtCore import pyqtSlot
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import (
    # QApplication,
    # QDesktopWidget,
    # QLabel,
    # QMainWindow,
    QPushButton,
    QTabWidget,
    QVBoxLayout,
    QWidget,
)

""" original files
"""
import func_persephonep


class PersephonepTabWidget(QWidget):
    """
    This is a Tab Handle Class for this browser.

    This class is called by PersephonepMainWindow,
    and it has some PersephonepWindos.

    Attributes:
    ----------
    TODO
    """

    def __init__(self, parent):
        """Set up tab."""
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)

        """ initialize tab screen
        """
        self.tabs = QTabWidget()
        self.tab = []  # Store the PersephonepWindow Class
        self.tabs.resize(1200, 800)

        # Add Tabs
        self._addTab(len(self.tab))  # len(self.tab) => 0
        # self.tabs.addTab(self.tab1, 'Tab 1')
        # self.tabs.addTab(self.tab2, 'Tab 2')
        self.add_button = QPushButton("+")
        self.add_button.setStyleSheet("background-color:gray")
        # add tab to last of index
        self.add_button.clicked.connect(lambda: self._addTab(len(self.tab)))
        # app_info_text = '%s is a Web Browser based on Python 3 and PyQt6,' \
        #                 ' developed by @montblanc18.' % func_persephonep.program_name()
        # self.app_info = QLabel(app_info_text)

        # define the delete tab process
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.closeTab)

        self.tabs.setUsesScrollButtons(True)
        # Create first tab
        # self.tab[0].layout = QVBoxLayout(self)
        # self.pushButton1 = QPushButton('PyQt6 button')
        # self.tab[0].layout.addWidget(self.pushButton1)
        # self.tab[0].setLayout(self.tab[0].layout)

        # Add tabs to widget
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.tabs)
        # self.layout.addWidget(self.app_info)
        self.setLayout(self.layout)

    def _addTab(self, index):
        """Add Tab."""
        self.tab.append(func_persephonep.PersephonepWindow(parent=self))
        #  do not match tab index & tab num
        self.tabs.addTab(self.tab[-1], "")
        self.tabs.setTabText(index, "VanilaPage")
        self.tab[-1].window.titleChanged.connect(self.updateTabName)

    def closeTab(self, index):
        """Close Tab."""
        # widget = self.tabs.widget(index)
        self.tab.pop(index)
        self.tabs.removeTab(index)

    def updateTabName(self):
        """Re-set tab name."""
        self.tabs.setTabText(
            self.tabs.currentIndex(), self.tab[self.tabs.currentIndex()].window.title()
        )

    def center(self):
        """Center widget."""
        qr = self.frameGeometry()
        cp = QGuiApplication.primaryScreen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    @pyqtSlot()
    def on_click(self):
        """Catch click event."""
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(
                currentQTableWidgetItem.row(),
                currentQTableWidgetItem.column(),
                currentQTableWidgetItem.text(),
            )
