#!/bin/bash
from PyQt5 import uic
from PyQt5 import QtCore 
from PyQt5 import QtGui
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.Qt import Qt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QMessageBox
from PyQt5.QtWidgets import  QSplashScreen, QMainWindow
import resources
import datetime
from timeapi import apptime
import subprocess,requests
import sys, base64,os,json,time


CUSTOMER = "IRCO"
PROJECT  = "AODD"

PROGRAMS_PATH = os.path.expanduser('~')+ r'/programs/'
ASSY_LOG_PATH = os.path.expanduser('~')+ r'/assy_log/'
WPROJECT_PATH = fr"E:/CUSTOMER_DEV/{CUSTOMER}/{PROJECT}"
LPROJECT_PATH = r"/etc/mviis"

if "win" in sys.platform:
    os.chdir(WPROJECT_PATH)
else:
    os.chdir(LPROJECT_PATH)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    return os.path.join(os.getcwd(), relative_path)


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        file_path = resource_path('ui/main.ui')
        uic.loadUi(file_path, self)


class MovieSplashScreen(QSplashScreen):

    def __init__(self, movie, parent = None):
    
        movie.jumpToFrame(0)
        pixmap = QPixmap(movie.frameRect().size())
        
        QSplashScreen.__init__(self, pixmap)
        self.movie = movie
        self.movie.frameChanged.connect(self.repaint)
        
    
    def showEvent(self, event):
        self.movie.start()
    
    def hideEvent(self, event):
        self.movie.stop()
    
    def paintEvent(self, event):
    
        painter = QPainter(self)
        pixmap = self.movie.currentPixmap()
        

        self.setMask(pixmap.mask())
        painter.drawPixmap(0, 0, pixmap.a())
    
    def sizeHint(self):
        return self.movie.scaledSize()
