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


if "win" in sys.platform:
    os.chdir(r"E:/CUSTOMER_DEV/KAYNES/mviis_git")
else:
    os.chdir(r"/etc/mviis")