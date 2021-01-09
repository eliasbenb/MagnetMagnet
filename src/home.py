import os
import re
import webbrowser

import requests
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import src.mglobals
from src.imagebytes import *
from src.search import Ui_searchMainWindow

if not os.path.exists(src.mglobals.base_path):
    os.makedirs(src.mglobals.base_path)
if not os.path.exists(src.mglobals.images_path):
    os.makedirs(src.mglobals.images_path)
if not os.path.exists(src.mglobals.images_path/'github.png'):
    with open(src.mglobals.images_path/'github.png', 'wb') as w:
        w.write(github_image_bytes)
if not os.path.exists(src.mglobals.images_path/'icon.png'):
    with open(src.mglobals.images_path/'icon.png', 'wb') as w:
        w.write(icon_image_bytes)
if not os.path.exists(src.mglobals.images_path/'kat.png'):
    with open(src.mglobals.images_path/'kat.png', 'wb') as w:
        w.write(kat_image_bytes)
if not os.path.exists(src.mglobals.images_path/'nyaa.png'):
    with open(src.mglobals.images_path/'nyaa.png', 'wb') as w:
        w.write(nyaa_image_bytes)
if not os.path.exists(src.mglobals.images_path/'rarbg.png'):
    with open(src.mglobals.images_path/'rarbg.png', 'wb') as w:
        w.write(rarbg_image_bytes)
if not os.path.exists(src.mglobals.images_path/'tpb.png'):
    with open(src.mglobals.images_path/'tpb.png', 'wb') as w:
        w.write(tpb_image_bytes)
if not os.path.exists(src.mglobals.images_path/'website.png'):
    with open(src.mglobals.images_path/'website.png', 'wb') as w:
        w.write(website_image_bytes)
if not os.path.exists(src.mglobals.images_path/'x1377.png'):
    with open(src.mglobals.images_path/'x1377.png', 'wb') as w:
        w.write(x1377_image_bytes)


class Ui_homeMainWindow(object):
    def setupUi(self, homeMainWindow):
        homeMainWindow.setObjectName("homeMainWindow")
        homeMainWindow.setFixedSize(1000, 500)
        font = QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(20)
        homeMainWindow.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
        homeMainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(homeMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.searchPushButton = QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QRect(0, 0, 1000, 200))
        self.searchPushButton.setObjectName("searchPushButton")
        self.x1377PushButton = QPushButton(self.centralwidget)
        self.x1377PushButton.setGeometry(QRect(0, 200, 200, 200))
        self.x1377PushButton.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(src.mglobals.x1377_icon),
                        QIcon.Normal, QIcon.Off)
        self.x1377PushButton.setIcon(icon1)
        self.x1377PushButton.setIconSize(QSize(80, 36))
        self.x1377PushButton.setObjectName("x1377PushButton")
        self.katPushButton = QPushButton(self.centralwidget)
        self.katPushButton.setGeometry(QRect(200, 200, 200, 200))
        self.katPushButton.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(src.mglobals.kat_icon),
                        QIcon.Normal, QIcon.Off)
        self.katPushButton.setIcon(icon2)
        self.katPushButton.setIconSize(QSize(64, 54))
        self.katPushButton.setObjectName("katPushButton")
        self.nyaaPushButton = QPushButton(self.centralwidget)
        self.nyaaPushButton.setGeometry(QRect(400, 200, 200, 200))
        self.nyaaPushButton.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(src.mglobals.nyaa_icon),
                        QIcon.Normal, QIcon.Off)
        self.nyaaPushButton.setIcon(icon3)
        self.nyaaPushButton.setIconSize(QSize(64, 64))
        self.nyaaPushButton.setObjectName("nyaaPushButton")
        self.rarbgPushButton = QPushButton(self.centralwidget)
        self.rarbgPushButton.setGeometry(QRect(600, 200, 200, 200))
        self.rarbgPushButton.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(src.mglobals.rarbg_icon),
                        QIcon.Normal, QIcon.Off)
        self.rarbgPushButton.setIcon(icon4)
        self.rarbgPushButton.setIconSize(QSize(110, 30))
        self.rarbgPushButton.setObjectName("rarbgPushButton")
        self.tpbPushButton = QPushButton(self.centralwidget)
        self.tpbPushButton.setGeometry(QRect(800, 200, 200, 200))
        self.tpbPushButton.setText("")
        icon5 = QIcon()
        icon5.addPixmap(QPixmap(src.mglobals.tpb_icon),
                        QIcon.Normal, QIcon.Off)
        self.tpbPushButton.setIcon(icon5)
        self.tpbPushButton.setIconSize(QSize(72, 72))
        self.tpbPushButton.setObjectName("tpbPushButton")
        self.websitePushButton = QPushButton(self.centralwidget)
        self.websitePushButton.setGeometry(QRect(0, 400, 500, 100))
        self.websitePushButton.setText("")
        icon6 = QIcon()
        icon6.addPixmap(QPixmap(src.mglobals.website_icon),
                        QIcon.Normal, QIcon.Off)
        self.websitePushButton.setIcon(icon6)
        self.websitePushButton.setIconSize(QSize(64, 64))
        self.websitePushButton.setObjectName("websitePushButton")
        self.githubPushButton = QPushButton(self.centralwidget)
        self.githubPushButton.setGeometry(QRect(500, 400, 500, 100))
        self.githubPushButton.setText("")
        icon7 = QIcon()
        icon7.addPixmap(QPixmap(src.mglobals.github_icon),
                        QIcon.Normal, QIcon.Off)
        self.githubPushButton.setIcon(icon7)
        self.githubPushButton.setIconSize(QSize(64, 64))
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
        QMetaObject.connectSlotsByName(homeMainWindow)

        def update_message():
            updateMessageBox = QMessageBox()
            updateMessageBox.setIcon(QMessageBox.Information)

            updateMessageBox.setText(
                "There is a newer version of MagnetMagnet. Would you like to update?")
            updateMessageBox.setWindowTitle("Update Available!")
            updateMessageBox.setStandardButtons(QMessageBox.Ok)
            updateMessageBox.setStandardButtons(QMessageBox.Ok)
            icon = QIcon()
            icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
            updateMessageBox.setWindowIcon(icon)

            updateMessageBox.buttonClicked.connect(update)

            updateMessageBox.exec_()

        def update():
            webbrowser.open(
                "https://github.com/eliasbenb/MagnetMagnet/releases/latest/")

        __VERSION__ = "7.2"
        try:
            version_request = requests.get(
                "https://github.com/eliasbenb/MagnetMagnet/releases/latest/")
            version_url = version_request.url
            version_url = version_url.split("/")
            latest_version = version_url[7]
            if latest_version > __VERSION__:
                update_message()
        except:
            pass

    def retranslateUi(self, homeMainWindow):
        _translate = QCoreApplication.translate
        homeMainWindow.setWindowTitle(_translate(
            "homeMainWindow", "MagnetMagnet @eliasbenb"))
        self.searchPushButton.setText(_translate("homeMainWindow", "Search"))
