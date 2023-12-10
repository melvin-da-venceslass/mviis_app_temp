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
import sys, base64,os,json,time
from timeapi import apptime
import admin_console
import hantas_bridge
from marker_ import Canvas
import resources
import datetime
# from gpiozero import Button
import subprocess,requests
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QApplication, QSplashScreen, QMainWindow