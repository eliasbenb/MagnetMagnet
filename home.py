from PyQt5 import QtCore, QtGui, QtWidgets
from search import Ui_searchMainWindow
from imagebytes import *
import os, requests, re, webbrowser

path = '%s\\eliasbenb' %  os.environ['APPDATA']
if not os.path.exists(path):
    os.makedirs(path)
if not os.path.exists(path+r'\images'):
    os.makedirs(path+r'\images')
if not os.path.exists(path+r'\images\github.png'):
    with open(path+r'\images\github.png','wb') as w:
        w.write(github_image_bytes)
if not os.path.exists(path+r'\images\icon.png'):
    with open(path+r'\images\icon.png','wb') as w:
        w.write(icon_image_bytes)
if not os.path.exists(path+r'\images\kat.png'):
    with open(path+r'\images\kat.png','wb') as w:
        w.write(kat_image_bytes)
if not os.path.exists(path+r'\images\nyaa.png'):
    with open(path+r'\images\nyaa.png','wb') as w:
        w.write(nyaa_image_bytes)
if not os.path.exists(path+r'\images\rarbg.png'):
    with open(path+r'\images\rarbg.png','wb') as w:
        w.write(rarbg_image_bytes)
if not os.path.exists(path+r'\images\tpb.png'):
    with open(path+r'\images\tpb.png','wb') as w:
        w.write(tpb_image_bytes)
if not os.path.exists(path+r'\images\website.png'):
    with open(path+r'\images\website.png','wb') as w:
        w.write(website_image_bytes)
if not os.path.exists(path+r'\images\x1377.png'):
    with open(path+r'\images\x1377.png','wb') as w:
        w.write(x1377_image_bytes)

class Ui_homeMainWindow(object):
    def setupUi(self, homeMainWindow):
        homeMainWindow.setObjectName("homeMainWindow")
        homeMainWindow.setFixedSize(1000, 500)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        homeMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        homeMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(homeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(0, 0, 1000, 200))
        self.searchPushButton.setObjectName("searchPushButton")
        self.x1377PushButton = QtWidgets.QPushButton(self.centralwidget)
        self.x1377PushButton.setGeometry(QtCore.QRect(0, 200, 200, 200))
        self.x1377PushButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(path+r"/images/x1377.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x1377PushButton.setIcon(icon1)
        self.x1377PushButton.setIconSize(QtCore.QSize(80, 36))
        self.x1377PushButton.setObjectName("x1377PushButton")
        self.katPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.katPushButton.setGeometry(QtCore.QRect(200, 200, 200, 200))
        self.katPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(path+r"/images/kat.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.katPushButton.setIcon(icon2)
        self.katPushButton.setIconSize(QtCore.QSize(64, 54))
        self.katPushButton.setObjectName("katPushButton")
        self.nyaaPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nyaaPushButton.setGeometry(QtCore.QRect(400, 200, 200, 200))
        self.nyaaPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(path+r"/images/nyaa.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nyaaPushButton.setIcon(icon3)
        self.nyaaPushButton.setIconSize(QtCore.QSize(64, 64))
        self.nyaaPushButton.setObjectName("nyaaPushButton")
        self.rarbgPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rarbgPushButton.setGeometry(QtCore.QRect(600, 200, 200, 200))
        self.rarbgPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(path+r"/images/rarbg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rarbgPushButton.setIcon(icon4)
        self.rarbgPushButton.setIconSize(QtCore.QSize(110, 30))
        self.rarbgPushButton.setObjectName("rarbgPushButton")
        self.tpbPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.tpbPushButton.setGeometry(QtCore.QRect(800, 200, 200, 200))
        self.tpbPushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(path+r"/images/tpb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tpbPushButton.setIcon(icon5)
        self.tpbPushButton.setIconSize(QtCore.QSize(72, 72))
        self.tpbPushButton.setObjectName("tpbPushButton")
        self.websitePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.websitePushButton.setGeometry(QtCore.QRect(0, 400, 500, 100))
        self.websitePushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(path+r"/images/website.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.websitePushButton.setIcon(icon6)
        self.websitePushButton.setIconSize(QtCore.QSize(64, 64))
        self.websitePushButton.setObjectName("websitePushButton")
        self.githubPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.githubPushButton.setGeometry(QtCore.QRect(500, 400, 500, 100))
        self.githubPushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(path+r"/images/github.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.githubPushButton.setIcon(icon7)
        self.githubPushButton.setIconSize(QtCore.QSize(64, 64))
        self.githubPushButton.setObjectName("githubPushButton")
        homeMainWindow.setCentralWidget(self.centralwidget)

        self.searchPushButton.clicked.connect(homeMainWindow.search)
        self.x1377PushButton.clicked.connect(homeMainWindow.x1377)
        self.katPushButton.clicked.connect(homeMainWindow.kat)
        self.nyaaPushButton.clicked.connect(homeMainWindow.nyaa)
        self.rarbgPushButton.clicked.connect(homeMainWindow.rarbg)
        self.tpbPushButton.clicked.connect(homeMainWindow.tpb)
        self.websitePushButton.clicked.connect(homeMainWindow.website)
        self.githubPushButton.clicked.connect(homeMainWindow.github)

        self.retranslateUi(homeMainWindow)
        QtCore.QMetaObject.connectSlotsByName(homeMainWindow)

        def update_message():
            updateMessageBox = QtWidgets.QMessageBox()
            updateMessageBox.setIcon(QtWidgets.QMessageBox.Information)

            updateMessageBox.setText("There is a newer version of MagnetMagnet. Would you like to update?")
            updateMessageBox.setWindowTitle("Update Available!")
            updateMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            updateMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            updateMessageBox.setWindowIcon(icon)

            updateMessageBox.buttonClicked.connect(update)
                
            updateMessageBox.exec_()

        def update():
            webbrowser.open("https://github.com/eliasbenb/MagnetMagnet/releases/latest/")
        
        __VERSION__ = "6.5"
        version_request = requests.get("https://github.com/eliasbenb/MagnetMagnet/releases/latest/")
        version_url = version_request.url
        version_url = version_url.split("/")
        latest_version = version_url[7]
        if latest_version != __VERSION__:
            update_message()

    def retranslateUi(self, homeMainWindow):
        _translate = QtCore.QCoreApplication.translate
        homeMainWindow.setWindowTitle(_translate("homeMainWindow", "MagnetMagnet @eliasbenb"))
        self.searchPushButton.setText(_translate("homeMainWindow", "Search"))