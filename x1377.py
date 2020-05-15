from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import mglobals, os, requests, re, time

path = mglobals.base_path

class Ui_x1337MainWindow(object):
    def callback(self):
        try:
            def exported_sucess_message():
                successMessageBox = QtWidgets.QMessageBox()
                successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

                successMessageBox.setText("Magnet links have been successfully exported to the local directory.")
                successMessageBox.setWindowTitle("Task Completed!")
                successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                successMessageBox.setWindowIcon(icon)
                    
                successMessageBox.exec_()  
            
            def error_message():
                errorMessageBox = QtWidgets.QMessageBox()
                errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

                errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
                errorMessageBox.setWindowTitle("Error!")
                errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                errorMessageBox.setWindowIcon(icon)
                    
                errorMessageBox.exec_()  

            domain = str(self.domainComboBox.currentText())
            category = str(self.categoryComboBox.currentText())

            if category == "Movies":
                category = "popular-movies"
            if category == "TV":
                category = "popular-tv"
            if category == "Games":
                category = "popular-games"
            if category == "Music":
                category = "popular-music"
            if category == "Applications":
                category = "popular-apps"
            if category == "Anime":
                category = "popular-anime"
            if category == "Documentaries":
                category = "popular-documentaries"
            if category == "Other":
                category = "popular-other"
            if category == "XXX":
                category = "popular-xxx"
            
            link = domain + category
            request = requests.get(link)

            source = request.content
            soup = BeautifulSoup(source, 'lxml')
            magnets = ['==== Made by @eliasbenb ====']
            for page_link in soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                page_link = 'https://1377x.to/' + page_link.get('href')
                page_request = requests.get(page_link)
                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')

                for link in page_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                    magnets.append('\n'+link.get('href'))
                magnets = list(dict.fromkeys(magnets))

            timestr = time.strftime(" %Y%m%d%H%M%S")
            file_name = "1377x Results " + timestr + ".txt"
            with open(file_name,'w') as w1:
                for magnet in magnets:
                    w1.write(magnet)
            exported_sucess_message()
        except:
            error_message()

    def setupUi(self, x1337MainWindow):
        x1337MainWindow.setObjectName("x1337MainWindow")
        x1337MainWindow.setFixedSize(600, 330)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        x1337MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        x1337MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(x1337MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.domainComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.domainComboBox.setGeometry(QtCore.QRect(150, 60, 300, 22))
        self.domainComboBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.domainComboBox.setObjectName("domainComboBox")
        self.domainComboBox.addItem("")
        self.domainLabel = QtWidgets.QLabel(self.centralwidget)
        self.domainLabel.setGeometry(QtCore.QRect(200, 30, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.domainLabel.setFont(font)
        self.domainLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.domainLabel.setObjectName("domainLabel")
        self.categoryComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.categoryComboBox.setGeometry(QtCore.QRect(150, 180, 300, 22))
        self.categoryComboBox.setObjectName("categoryComboBox")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryComboBox.addItem("")
        self.categoryLabel = QtWidgets.QLabel(self.centralwidget)
        self.categoryLabel.setGeometry(QtCore.QRect(200, 150, 200, 16))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.categoryLabel.setFont(font)
        self.categoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.categoryLabel.setObjectName("categoryLabel")
        self.scrapeButton = QtWidgets.QPushButton(self.centralwidget)
        self.scrapeButton.setGeometry(QtCore.QRect(262, 260, 75, 30))
        self.scrapeButton.setObjectName("scrapeButton")
        x1337MainWindow.setCentralWidget(self.centralwidget)

        self.scrapeButton.clicked.connect(self.callback)

        self.retranslateUi(x1337MainWindow)
        QtCore.QMetaObject.connectSlotsByName(x1337MainWindow)

    def retranslateUi(self, x1337MainWindow):
        _translate = QtCore.QCoreApplication.translate
        x1337MainWindow.setWindowTitle(_translate("x1337MainWindow", "MagnetMagnet - 1377x"))
        self.domainComboBox.setItemText(0, _translate("x1337MainWindow", "https://1377x.to/"))
        self.domainLabel.setText(_translate("x1337MainWindow", "Choose a 1377x domain:"))
        self.categoryComboBox.setItemText(0, _translate("x1337MainWindow", "Movies"))
        self.categoryComboBox.setItemText(1, _translate("x1337MainWindow", "TV"))
        self.categoryComboBox.setItemText(2, _translate("x1337MainWindow", "Anime"))
        self.categoryComboBox.setItemText(3, _translate("x1337MainWindow", "Music"))
        self.categoryComboBox.setItemText(4, _translate("x1337MainWindow", "XXX"))
        self.categoryLabel.setText(_translate("x1337MainWindow", "Choose a category:"))
        self.scrapeButton.setText(_translate("x1337MainWindow", "Scrape"))
