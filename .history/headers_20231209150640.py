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


PROGRAMS_PATH = os.path.expanduser('~')+ r'/programs/'
ASSY_LOG_PATH = os.path.expanduser('~')+ r'/assy_log/'
WPROJECT_PATH = r"E:/CUSTOMER_DEV/KAYNES/mviis_git"
LPROJECT_PATH = r"/etc/mviis"

if "win" in sys.platform:
    os.chdir()
else:
    os.chdir()

