from PyQt5 import QtCore, QtGui, QtWidgets
import mglobals
from search import Ui_searchMainWindow
from imagebytes import *
import os, requests, re, webbrowser

if not os.path.exists(mglobals.base_path):
    os.makedirs(mglobals.base_path)
if not os.path.exists(mglobals.images_path):
    os.makedirs(mglobals.images_path)
if not os.path.exists(mglobals.images_path/'github.png'):
    with open(mglobals.images_path/'github.png','wb') as w:
        w.write(github_image_bytes)
if not os.path.exists(mglobals.images_path/'icon.png'):
    with open(mglobals.images_path/'icon.png','wb') as w:
        w.write(icon_image_bytes)
if not os.path.exists(mglobals.images_path/'kat.png'):
    with open(mglobals.images_path/'kat.png','wb') as w:
        w.write(kat_image_bytes)
if not os.path.exists(mglobals.images_path/'nyaa.png'):
    with open(mglobals.images_path/'nyaa.png','wb') as w:
        w.write(nyaa_image_bytes)
if not os.path.exists(mglobals.images_path/'rarbg.png'):
    with open(mglobals.images_path/'rarbg.png','wb') as w:
        w.write(rarbg_image_bytes)
if not os.path.exists(mglobals.images_path/'tpb.png'):
    with open(mglobals.images_path/'tpb.png','wb') as w:
        w.write(tpb_image_bytes)
if not os.path.exists(mglobals.images_path/'website.png'):
    with open(mglobals.images_path/'website.png','wb') as w:
        w.write(website_image_bytes)
if not os.path.exists(mglobals.images_path/'x1377.png'):
    with open(mglobals.images_path/'x1377.png','wb') as w:
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
        icon.addPixmap(QtGui.QPixmap(mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
        icon1.addPixmap(QtGui.QPixmap(mglobals.x1377_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.x1377PushButton.setIcon(icon1)
        self.x1377PushButton.setIconSize(QtCore.QSize(80, 36))
        self.x1377PushButton.setObjectName("x1377PushButton")
        self.katPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.katPushButton.setGeometry(QtCore.QRect(200, 200, 200, 200))
        self.katPushButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(mglobals.kat_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.katPushButton.setIcon(icon2)
        self.katPushButton.setIconSize(QtCore.QSize(64, 54))
        self.katPushButton.setObjectName("katPushButton")
        self.nyaaPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.nyaaPushButton.setGeometry(QtCore.QRect(400, 200, 200, 200))
        self.nyaaPushButton.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(mglobals.nyaa_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nyaaPushButton.setIcon(icon3)
        self.nyaaPushButton.setIconSize(QtCore.QSize(64, 64))
        self.nyaaPushButton.setObjectName("nyaaPushButton")
        self.rarbgPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.rarbgPushButton.setGeometry(QtCore.QRect(600, 200, 200, 200))
        self.rarbgPushButton.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(mglobals.rarbg_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rarbgPushButton.setIcon(icon4)
        self.rarbgPushButton.setIconSize(QtCore.QSize(110, 30))
        self.rarbgPushButton.setObjectName("rarbgPushButton")
        self.tpbPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.tpbPushButton.setGeometry(QtCore.QRect(800, 200, 200, 200))
        self.tpbPushButton.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(mglobals.tpb_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tpbPushButton.setIcon(icon5)
        self.tpbPushButton.setIconSize(QtCore.QSize(72, 72))
        self.tpbPushButton.setObjectName("tpbPushButton")
        self.websitePushButton = QtWidgets.QPushButton(self.centralwidget)
        self.websitePushButton.setGeometry(QtCore.QRect(0, 400, 500, 100))
        self.websitePushButton.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(mglobals.website_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.websitePushButton.setIcon(icon6)
        self.websitePushButton.setIconSize(QtCore.QSize(64, 64))
        self.websitePushButton.setObjectName("websitePushButton")
        self.githubPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.githubPushButton.setGeometry(QtCore.QRect(500, 400, 500, 100))
        self.githubPushButton.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(mglobals.github_icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
            icon.addPixmap(QtGui.QPixmap(mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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