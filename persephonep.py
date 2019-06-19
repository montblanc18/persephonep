#!/usr/bin/env python
# coding: utf-8
#

import sys
import os
import argparse
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTabWidget, QApplication,
                             QVBoxLayout, QLabel, QDesktopWidget, QStatusBar)
from PyQt5.QtGui import QIcon

''' original files
'''
from func_persephonep import program_name
from tab_controller import PersephonepTabWidget


''' functions
'''
def persephonep_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action = 'store_true',help='Show debug messages.')
    parser.add_argument('-u', '--url', type = str, default = 'http://www.google.com', help='Set url you want to open at start.')
    parser.add_argument('-v', '--verbose', action = 'store_true', help ='Show details of this browser.')
    ret_args = parser.parse_args()
    if args.debug:
        print(ret_args)
    return ret_args

def create_main_window():
    main_window = PersephonepMainWindow()
    available_geometry = app.desktop().availableGeometry(main_window)
    main_window.resize(available_geometry.width() * 3 / 4, available_geometry.height() * 3 / 4)
    main_window.show()
    return main_window

''' This is a main window of the browser.
    This class includes PersephonepMainWidget.
'''
class PersephonepMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = program_name()
        '''
        self.left = 100
        self.top = 100
        self.width = 1200
        self.height = 800
        self.setGeometry(self.left, self.top, self.width, self.height)
        '''
        self.setWindowTitle(self.title)
        self.table_widget = PersephonepTabWidget(self)
        self.setCentralWidget(self.table_widget)

        ''' ToDo: Add Download Controller
        '''
        self._zoom_label = QLabel("This is status bar.")
        self.statusBar().addPermanentWidget(self._zoom_label)


        ''' ToDo: Add Config Controller
        '''

        ''' ToDo: Create Menu
        '''


''' This is a Tab Handle Class for this browser.
    This class is called by PersephonepMainWindow,
    and it has some PersephonepWindos.
'''


if __name__ == '__main__':

    ''' parse options 
    '''
    args = persephonep_parser()

    app = QApplication(sys.argv)
    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__),
                        'icon_persephone.png')
    app.setWindowIcon(QIcon(path))
    
    ''' Show Windows
    '''
    main_win = create_main_window()
    
    ''' ToDo: Open URLs which you set by args
    '''

    ''' Call event loop
    Notice: 
        QApplication manages events, resources, and so on.
        PyQt Application needs this object.
        ```QApplication.exec_()```, ```app.exec_()``` in this program, calls event loop.
        By executing this sentence, program hands management of resources to PyQt.
    '''
    exit_code = app.exec_()

    ''' ToDo: Write save data like setting before finishing program
    '''

    sys.exit(exit_code)
