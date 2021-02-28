#!/usr/bin/env python
# coding: utf-8
#
"""main python script of persephonep."""

import argparse
import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import (
    QApplication,
    # QDesktopWidget,
    # QLabel,
    QMainWindow,
    # QPushButton,
    # QTabWidget,
    # QStatusBar,
    # QWidget,
    # QVBoxLayout,
)

""" original files
"""
sys.path.append(os.path.abspath(os.path.dirname(os.path.abspath(__file__))))

import func_persephonep

import tab_controller


""" functions
"""


def persephonep_parser():
    """Option parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--debug", action="store_true", help="Show debug messages.")
    parser.add_argument(
        "-u",
        "--url",
        type=str,
        default="http://www.google.com",
        help="Set url you want to open at start.",
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="Show details of this browser."
    )
    ret_args = parser.parse_args()
    if ret_args.debug:
        print(ret_args)
    return ret_args


def create_main_window(app):
    """Create main window and return its object."""
    main_window = PersephonepMainWindow()
    available_geometry = app.desktop().availableGeometry(main_window)
    main_window.resize(
        available_geometry.width() * 3 / 4, available_geometry.height() * 3 / 4
    )
    main_window.show()
    return main_window


class PersephonepMainWindow(QMainWindow):
    """
    This is a main window of the browser.

    This class includes PersephonepMainWidget.

    Attributes:
    ----------
    title : str
        Name of this program which equals this browser.
    table_widget :
        TODO
    _zoom_label :
        TODO
    """

    def __init__(self):
        super().__init__()
        self.title = func_persephonep.program_name()
        # self.left = 100
        # self.top = 100
        # self.width = 1200
        # self.height = 800
        # self.setGeometry(self.left, self.top, self.width, self.height)
        self.setWindowTitle(self.title)
        self.table_widget = tab_controller.PersephonepTabWidget(self)
        self.setCentralWidget(self.table_widget)
        # TODO: Add Download Controller
        # app_info_text = (
        #    "%s is a Web Browser based on Python 3 and PyQt5,"
        #    " developed by @montblanc18." % func_persephonep.program_name()
        # )

        # self.statusBar().addPermanentWidget(self._zoom_label)
        # TODO: Add Config Controller
        # TODO: Create Menu


def main():
    """Handle main sequence."""
    global app
    persephonep_parser()

    app = QApplication(sys.argv)
    # setWindowIcon is a method for QApplication, not for QWidget
    # print(sys.modules[__name__].__file__)
    icon_path = os.path.join(
        os.path.dirname(sys.modules[__name__].__file__),
        "../persephonep/icon_persephone.png",
    )
    # print(icon_path)
    app.setWindowIcon(QIcon(icon_path))
    # Show Windows
    create_main_window(app)
    """ Call event loop
        QApplication manages events, resources, and so on.
        PyQt Application needs this object.
        ```QApplication.exec_()```, ```app.exec_()``` in this program, calls event loop.
        By executing this sentence, program hands management of resources to PyQt.
    """
    # TODO: Write save data like setting before finishing program
    exit_code = 1
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
