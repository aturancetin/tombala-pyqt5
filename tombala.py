"""
@file: tombala.py

@author: Ali Turan Cetin

@date: June 9, 2021

@brief: Tombala Game with PyQt5
"""


from tombala_ui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys
import os

os.environ['DISPLAY'] = ':0'


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])

MainWindow = mywindow()
MainWindow.show()


sys.exit(app.exec_())
