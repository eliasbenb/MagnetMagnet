from PyQt5 import QtCore, QtGui, QtWidgets
from search import Ui_searchMainWindow
from imagebytes import *
import os, requests, re

path = '%s\\eliasbenb' %  os.environ['APPDATA']
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(path+r'\images'):
    os.makedirs(path+r'\images')
if not os.path.exists(path+r'\images\eliasbenb.png'):
    with open(path+r'\images\eliasbenb.png','wb') as w1:
        w1.write(eliasbenb_image_bytes)
if not os.path.exists(path+r'\images\github.png'):
    with open(path+r'\images\github.png','wb') as w2:
        w2.write(github_image_bytes)
if not os.path.exists(path+r'\images\icon.png'):
    with open(path+r'\images\icon.png','wb') as w3:
        w3.write(icon_image_bytes)
if not os.path.exists(path+r'\images\kat.png'):
    with open(path+r'\images\kat.png','wb') as w4:
        w4.write(kat_image_bytes)
if not os.path.exists(path+r'\images\nyaa.png'):
    with open(path+r'\images\nyaa.png','wb') as w5:
        w5.write(nyaa_image_bytes)
if not os.path.exists(path+r'\images\rarbg.png'):
    with open(path+r'\images\rarbg.png','wb') as w6:
        w6.write(rarbg_image_bytes)
if not os.path.exists(path+r'\images\tpb.png'):
    with open(path+r'\images\tpb.png','wb') as w7:
        w7.write(tpb_image_bytes)
if not os.path.exists(path+r'\images\website.png'):
    with open(path+r'\images\website.png','wb') as w8:
        w8.write(website_image_bytes)
if not os.path.exists(path+r'\images\x1377.png'):
    with open(path+r'\images\x1377.png','wb') as w9:
        w9.write(x1377_image_bytes)


class Ui_homeMainWindow(object):
    def setupUi(self, homeMainWindow):
        homeMainWindow.setObjectName("homeMainWindow")
        homeMainWindow.setWindowModality(QtCore.Qt.NonModal)
        homeMainWindow.setEnabled(True)
        homeMainWindow.setFixedSize(1000, 500)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(26)
        font.setBold(False)
        font.setWeight(50)
        homeMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(homeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(0, 0, 1000, 200))
        self.searchButton.setObjectName("searchButton")
        self.x1377Button = QtWidgets.QPushButton(self.centralwidget)
        self.x1377Button.setGeometry(QtCore.QRect(0, 200, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(18)
        self.x1377Button.setFont(font)
        self.x1377Button.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path+r"/images/x1377.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x1377Button.setIcon(icon1)
        self.x1377Button.setIconSize(QtCore.QSize(64, 64))
        self.x1377Button.setDefault(False)
        self.x1377Button.setFlat(False)
        self.x1377Button.setObjectName("x1377Button")
        self.katButton = QtWidgets.QPushButton(self.centralwidget)
        self.katButton.setGeometry(QtCore.QRect(200, 200, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(18)
        self.katButton.setFont(font)
        self.katButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(path+r"/images/kat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.katButton.setIcon(icon2)
        self.katButton.setIconSize(QtCore.QSize(64, 54))
        self.katButton.setObjectName("katButton")
        self.nyaaButton = QtWidgets.QPushButton(self.centralwidget)
        self.nyaaButton.setGeometry(QtCore.QRect(400, 200, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(18)
        self.nyaaButton.setFont(font)
        self.nyaaButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(path+r"/images/nyaa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nyaaButton.setIcon(icon3)
        self.nyaaButton.setIconSize(QtCore.QSize(80, 80))
        self.nyaaButton.setObjectName("nyaaButton")
        self.rarbgButton = QtWidgets.QPushButton(self.centralwidget)
        self.rarbgButton.setGeometry(QtCore.QRect(600, 200, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(18)
        self.rarbgButton.setFont(font)
        self.rarbgButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(path+r"/images/rarbg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rarbgButton.setIcon(icon4)
        self.rarbgButton.setIconSize(QtCore.QSize(90, 90))
        self.rarbgButton.setObjectName("rarbgButton")
        self.tpbButton = QtWidgets.QPushButton(self.centralwidget)
        self.tpbButton.setGeometry(QtCore.QRect(800, 200, 200, 200))
        font = QtGui.QFont()
        font.setFamily("Moon")
        font.setPointSize(18)
        self.tpbButton.setFont(font)
        self.tpbButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(path+r"/images/tpb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tpbButton.setIcon(icon5)
        self.tpbButton.setIconSize(QtCore.QSize(72, 72))
        self.tpbButton.setObjectName("tpbButton")
        self.eliasbenbButton = QtWidgets.QPushButton(self.centralwidget)
        self.eliasbenbButton.setGeometry(QtCore.QRect(250, 400, 500, 100))
        self.eliasbenbButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.eliasbenbButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(path+r"/images/eliasbenb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.eliasbenbButton.setIcon(icon6)
        self.eliasbenbButton.setIconSize(QtCore.QSize(64, 64))
        self.eliasbenbButton.setObjectName("eliasbenbButton")
        self.websiteButton = QtWidgets.QPushButton(self.centralwidget)
        self.websiteButton.setGeometry(QtCore.QRect(0, 400, 250, 100))
        self.websiteButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(path+r"/images/website.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.websiteButton.setIcon(icon7)
        self.websiteButton.setIconSize(QtCore.QSize(60, 60))
        self.websiteButton.setObjectName("websiteButton")
        self.githubButton = QtWidgets.QPushButton(self.centralwidget)
        self.githubButton.setGeometry(QtCore.QRect(750, 400, 250, 100))
        self.githubButton.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(path+r"/images/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubButton.setIcon(icon8)
        self.githubButton.setIconSize(QtCore.QSize(60, 60))
        self.githubButton.setObjectName("githubButton")
        homeMainWindow.setCentralWidget(self.centralwidget)

        self.searchButton.clicked.connect(homeMainWindow.search)
        self.x1377Button.clicked.connect(homeMainWindow.x1377)
        self.katButton.clicked.connect(homeMainWindow.kat)
        self.nyaaButton.clicked.connect(homeMainWindow.nyaa)
        self.rarbgButton.clicked.connect(homeMainWindow.rarbg)
        self.tpbButton.clicked.connect(homeMainWindow.tpb)
        
        self.eliasbenbButton.clicked.connect(homeMainWindow.website)
        self.websiteButton.clicked.connect(homeMainWindow.website)
        self.githubButton.clicked.connect(homeMainWindow.github)

        self.retranslateUi(homeMainWindow)
        self.searchButton.clicked['bool'].connect(homeMainWindow.setAnimated)
        QtCore.QMetaObject.connectSlotsByName(homeMainWindow)

    def retranslateUi(self, homeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        homeMainWindow.setWindowTitle(_translate("homeMainWindow", "MagnetMagnet - @eliasbenb"))
        self.searchButton.setText(_translate("homeMainWindow", "Search"))
