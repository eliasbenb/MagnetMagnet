import os
import re
import time

import requests
from bs4 import BeautifulSoup
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import src.mglobals

path = src.mglobals.base_path


class Ui_nyaaMainWindow(object):
    def callback(self):
        def exported_sucess_message():
            successMessageBox = QMessageBox()
            successMessageBox.setIcon(QMessageBox.Information)

            successMessageBox.setText(
                "Magnet links have been successfully exported to the local directory.")
            successMessageBox.setWindowTitle("Task Completed!")
            successMessageBox.setStandardButtons(QMessageBox.Ok)
            icon = QIcon()
            icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
            successMessageBox.setWindowIcon(icon)

            successMessageBox.exec_()

        def error_message():
            errorMessageBox = QMessageBox()
            errorMessageBox.setIcon(QMessageBox.Information)

            errorMessageBox.setText(
                "Something went wrong! Please inform me through GitHub!")
            errorMessageBox.setWindowTitle("Error!")
            errorMessageBox.setStandardButtons(QMessageBox.Ok)
            icon = QIcon()
            icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
            errorMessageBox.setWindowIcon(icon)

            errorMessageBox.exec_()
        try:
            domain = str(self.domainComboBox.currentText())
            category = str(self.categoryComboBox.currentText())

            if category == "All":
                category = "0_0"
            if category == "Anime":
                category = "1_0"
            if category == "Audio":
                category = "2_0"
            if category == "Literature":
                category = "3_0"
            if category == "Live Action":
                category = "4_0"
            if category == "Pictures":
                category = "5_0"
            if category == "Software":
                category = "6_0"

            link = domain + '?c=' + category
            try:
                request = requests.get(link)
                source = request.content
                soup = BeautifulSoup(source, 'lxml')

                magnets = ['==== Made by @eliasbenb ====']
                for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                    magnets.append('\n'+link.get('href'))
                magnets = list(dict.fromkeys(magnets))

                timestr = time.strftime(" %Y%m%d%H%M%S")
                file_name = "Nyaa Results " + timestr + ".txt"
                with open(file_name, 'w') as w1:
                    for magnet in magnets:
                        w1.write(magnet)
                exported_sucess_message()
            except:
                error_message()
        except:
            error_message()

    def setupUi(self, nyaaMainWindow):
        nyaaMainWindow.setObjectName("nyaaMainWindow")
        nyaaMainWindow.setFixedSize(600, 330)
        font = QFont()
        font.setFamily("Bahnschrift Light")
        nyaaMainWindow.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
        nyaaMainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(nyaaMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.domainComboBox = QComboBox(self.centralwidget)
        self.domainComboBox.setGeometry(QRect(150, 60, 300, 22))
        self.domainComboBox.setLayoutDirection(Qt.LeftToRight)
        self.domainComboBox.setObjectName("domainComboBox")
        self.domainComboBox.addItem("")
        self.domainLabel = QLabel(self.centralwidget)
        self.domainLabel.setGeometry(QRect(200, 30, 200, 16))
        font = QFont()
        font.setPointSize(11)
        self.domainLabel.setFont(font)
        self.domainLabel.setAlignment(Qt.AlignCenter)
        self.domainLabel.setObjectName("domainLabel")
        self.categoryComboBox = QComboBox(self.centralwidget)
        self.categoryComboBox.setGeometry(QRect(150, 180, 300, 22))
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryLabel = QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QRect(200, 150, 200, 16))
        font = QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setAlignment(Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.scrapeButton = QPushButton(self.centralwidget)
        self.scrapeButton.setGeometry(QRect(262, 260, 75, 30))
        self.scrapeButton.setObjectName("scrapeButton")
        nyaaMainWindow.setCentralWidget(self.centralwidget)

        self.scrapeButton.clicked.connect(self.callback)

        self.retranslateUi(nyaaMainWindow)
        QMetaObject.connectSlotsByName(nyaaMainWindow)

    def retranslateUi(self, nyaaMainWindow):
        _translate = QCoreApplication.translate
        nyaaMainWindow.setWindowTitle(_translate(
            "nyaaMainWindow", "MagnetMagnet - Nyaa"))
        self.domainComboBox.setItemText(
            0, _translate("nyaaMainWindow", "https://nyaa.si/"))
        self.domainLabel.setText(_translate(
            "nyaaMainWindow", "Choose a Nyaa domain:"))
        self.categoryComboBox.setItemText(
            0, _translate("nyaaMainWindow", "All"))
        self.categoryComboBox.setItemText(
            1, _translate("nyaaMainWindow", "Anime"))
        self.categoryComboBox.setItemText(
            2, _translate("nyaaMainWindow", "Audio"))
        self.categoryComboBox.setItemText(
            3, _translate("nyaaMainWindow", "Literature"))
        self.categoryComboBox.setItemText(
            4, _translate("nyaaMainWindow", "Live Action"))
        self.categoryComboBox.setItemText(
            5, _translate("nyaaMainWindow", "Pictrues"))
        self.categoryComboBox.setItemText(
            6, _translate("nyaaMainWindow", "Software"))
        self.categoryLabel.setText(_translate(
            "nyaaMainWindow", "Choose a category:"))
        self.scrapeButton.setText(_translate("nyaaMainWindow", "Scrape"))
