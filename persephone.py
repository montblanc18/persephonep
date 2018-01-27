#!/usr/bin/env python
# coding: utf-8
#

import sys
from PyQt5.QtWidgets import QWidget, QPushButton, QTabWidget, QApplication, QHBoxLayout, QVBoxLayout

from func_persephone import *

__program__ = 'PERSEPHONE'

class mainUI(QWidget):
    ''' Main UI of PERSEPHONE
    '''

    def __init__(self):
        super(mainUI, self).__init__()
        self.initUI()

    def initUI(self):
        self.add_button = QPushButton('+')
        self.add_button.setStyleSheet('background-color:gray')
        self.add_button.clicked.connect(self._addTab)
        
        self.qtab = QTabWidget()
        self.qtab.setTabsClosable(True);
        self._addTab()
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.add_button)
        vbox.addWidget(self.qtab)

        self.setLayout(vbox)

        self.resize(1200, 800)
        self.center()
        self.setWindowTitle(__program__)
        self.show()

    def _addTab(self):
        ''' add Tab
        '''
        self.qtab.addTab(PersephoneWindow(parent = self), '')
        self.qtab.tabCloseRequested.connect(self.closeTab)

    def closeTab(self, index):
        ''' close Tab. This function has some problem.
        when this is called, some tabs was deleted together.
        '''
        widget = self.qtab.widget(index)
        if widget is not None:
            widget.deleteLater()
        self.qtab.removeTab(index)

    def center(self):
        ''' centering widget
        '''
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # setWindowIcon is a method for QApplication, not for QWidget
    path = os.path.join(os.path.dirname(sys.modules[__name__].__file__), 'icon_persephone.png')
    app.setWindowIcon(QIcon(path))

    
    ui = mainUI()
    sys.exit(app.exec_())
