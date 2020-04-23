# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 15:14:52 2017

@author: richardc
"""
from sys import argv
from os import getcwd
from PyQt5 import uic, QtWidgets

form_class = uic.loadUiType("qtGUI2.ui")[0]

class MyWindowClass(QtWidgets.QMainWindow, form_class):
    def __init__(self, parent):
        QtWidgets.QMainWindow.__init__(self, parent)
        self.setupUi(self)

#run the proper program
QtWidgets.QApplication.setStyle("fusion")
app2 = QtWidgets.QApplication(argv)
myWindow = MyWindowClass(None)
myWindow.show()
app2.exec_()