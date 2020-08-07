from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from bs4 import BeautifulSoup
import src.mglobals, os, requests, re, time

path = src.mglobals.base_path

class Ui_rarbgMainWindow(object):
    def callback(self):
        try:
            def exported_sucess_message():
                successMessageBox = QMessageBox()
                successMessageBox.setIcon(QMessageBox.Information)

                successMessageBox.setText("Magnet links have been successfully exported to the local directory.")
                successMessageBox.setWindowTitle("Task Completed!")
                successMessageBox.setStandardButtons(QMessageBox.Ok)
                icon = QIcon()
                icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
                successMessageBox.setWindowIcon(icon)
                    
                successMessageBox.exec_()

            def error_message():
                errorMessageBox = QMessageBox()
                errorMessageBox.setIcon(QMessageBox.Information)

                errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
                errorMessageBox.setWindowTitle("Error!")
                errorMessageBox.setStandardButtons(QMessageBox.Ok)
                icon = QIcon()
                icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
                errorMessageBox.setWindowIcon(icon)
                    
                errorMessageBox.exec_()  

            domain = str(self.domainComboBox.currentText())
            category = str(self.categoryComboBox.currentText())

            if category == "All":
                category = ""
            if category == "Movies - All":
                category = "movies"
            if category == "Movies - UHD":
                category = "50;51;52"
            if category == "Movies - HD":
                category = "44;42;46;54"
            if category == "Movies - Not HD":
                category = "14;48;17;45"
            if category == "TV - All":
                category = "2;18;41;49"
            if category == "TV - UHD":
                category = "49"
            if category == "TV - HD":
                category = "41"
            if category == "Music - All":
                category = "2;23;24;25;26"            
            if category == "XXX - All":
                category = "2;4"

            link = domain + 'rssdd.php?category=' + category
            request = requests.get(link)
            source = request.content
            soup = BeautifulSoup(source, 'xml')

            magnets = ['==== Made by @eliasbenb ====']
            for item in soup.findAll('item'):
                magnets.append('\n'+item.link.text)
            
            timestr = time.strftime(" %Y%m%d%H%M%S")
            file_name = "RARBG Results " + timestr + ".txt"
            with open(file_name,'w') as w1:
                for magnet in magnets:
                    w1.write(magnet)
            exported_sucess_message()
        except:
            error_message()

    def setupUi(self, rarbgMainWindow):
        rarbgMainWindow.setObjectName("rarbgMainWindow")
        rarbgMainWindow.setFixedSize(600, 330)
        font = QFont()
        font.setFamily("Bahnschrift Light")
        rarbgMainWindow.setFont(font)
        icon = QIcon()
        icon.addPixmap(QPixmap(src.mglobals.icon), QIcon.Normal, QIcon.Off)
        rarbgMainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(rarbgMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.domainComboBox = QComboBox(self.centralwidget)
        self.domainComboBox.setGeometry(QRect(150, 60, 300, 22))
        self.domainComboBox.setLayoutDirection(Qt.LeftToRight)
        self.domainComboBox.setObjectName("domainComboBox")
        self.domainComboBox.addItem("")
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
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryLabel = QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QRect(200, 150, 200, 16))
        font = QFont()
        font.setPointSize(11)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setAlignment(Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.scrapeButton = QPushButton(self.centralwidget)
        self.scrapeButton.setGeometry(QRect(262, 260, 75, 30))
        self.scrapeButton.setObjectName("scrapeButton")
        rarbgMainWindow.setCentralWidget(self.centralwidget)

        self.scrapeButton.clicked.connect(self.callback)

        self.retranslateUi(rarbgMainWindow)
        QMetaObject.connectSlotsByName(rarbgMainWindow)

    def retranslateUi(self, rarbgMainWindow):
        _translate = QCoreApplication.translate
        rarbgMainWindow.setWindowTitle(_translate("rarbgMainWindow", "MagnetMagnet - RARBG"))
        self.domainComboBox.setItemText(0, _translate("rarbgMainWindow", "https://rarbg.to/"))
        self.domainComboBox.setItemText(1, _translate("rarbgMainWindow", "https://rarbgmirror.com/"))
        self.domainLabel.setText(_translate("rarbgMainWindow", "Choose a RARBG domain:"))
        self.categoryComboBox.setItemText(0, _translate("rarbgMainWindow", "All"))
        self.categoryComboBox.setItemText(1, _translate("rarbgMainWindow", "Movies - All"))
        self.categoryComboBox.setItemText(2, _translate("rarbgMainWindow", "Movies - UHD"))
        self.categoryComboBox.setItemText(3, _translate("rarbgMainWindow", "Movies - HD"))
        self.categoryComboBox.setItemText(4, _translate("rarbgMainWindow", "Movies - Not HD"))
        self.categoryComboBox.setItemText(5, _translate("rarbgMainWindow", "TV - All"))
        self.categoryComboBox.setItemText(6, _translate("rarbgMainWindow", "TV - UHD"))
        self.categoryComboBox.setItemText(7, _translate("rarbgMainWindow", "TV - HD"))
        self.categoryComboBox.setItemText(8, _translate("rarbgMainWindow", "Music - All"))
        self.categoryComboBox.setItemText(9, _translate("rarbgMainWindow", "XXX - All"))
        self.categoryLabel.setText(_translate("rarbgMainWindow", "Choose a category:"))
        self.scrapeButton.setText(_translate("rarbgMainWindow", "Scrape"))
