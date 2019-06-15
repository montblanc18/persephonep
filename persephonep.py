#!/usr/bin/env python
# coding: utf-8
#

import sys
import os
import argparse
from PyQt5.QtWidgets import (QMainWindow, QWidget, QPushButton,
                             QTabWidget, QApplication,
                             QVBoxLayout, QLabel, QDesktopWidget)
from PyQt5.QtGui import QIcon

''' original files
'''
from func_persephonep import program_name
from tab_controller import PersephonepTableWidget


''' functions
'''
def persephonep_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', action = 'store_true',help='Show debug messages.')
    parser.add_argument('-u', '--url', type = str, default = 'http://www.google.com', help='Set url you want to open at start.')
    parser.add_argument('-v', '--verbose', action = 'store_true', help ='Show details of this browser.')
    args = parser.parse_args()
    if args.debug: print(args)
    return args

def create_main_window():
    main_window = PersephonepMainWindow()
    main_window.show()
    return main_window

''' This is a main window of the browser.
    This class includes PersephonepMainWidget.
'''
class PersephonepMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = program_name()
        self.left = 100
        self.top = 100
        self.width = 1200
        self.height = 800
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.table_widget = PersephonepTableWidget(self)
        self.setCentralWidget(self.table_widget)


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
    main_window = create_main_window()
    
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
