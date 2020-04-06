from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, requests, re, time

path = '%s\\eliasbenb' %  os.environ['APPDATA']

class Ui_katMainWindow(object):
    def callback(self):
        def exported_sucess_message():
            successMessageBox = QtWidgets.QMessageBox()
            successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

            successMessageBox.setText("Magnet links have been successfully exported to the local directory.")
            successMessageBox.setWindowTitle("Task Completed!")
            successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            successMessageBox.setWindowIcon(icon)
                
            successMessageBox.exec_()

        def error_message():
            errorMessageBox = QtWidgets.QMessageBox()
            errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

            errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
            errorMessageBox.setWindowTitle("Error!")
            errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            errorMessageBox.setWindowIcon(icon)
                
            errorMessageBox.exec_()  

        domain = str(self.domainComboBox.currentText())
        category = str(self.categoryComboBox.currentText())

        if category == "Movies":
            category = "movies"
        if category == "TV":
            category = "tv"
        if category == "Anime":
            category = "anime"
        if category == "Music":
            category = "music"
        if category == "Books":
            category = "Books"
        if category == "XXX":
            category = "xxx"
        if category == "All":
            category = "new"
        
        link = domain + category
        try:
            request = requests.get(link)
        except:
            error_message()
        source = request.content
        soup = BeautifulSoup(source, 'lxml')

        magnets = ['==== Made by @eliasbenb ====']
        for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
            magnets.append('\n'+link.get('href'))
        magnets = list(dict.fromkeys(magnets))

        timestr = time.strftime(" %Y%m%d%H%M%S")
        file_name = "KAT Results " + timestr + ".txt"
        with open(file_name,'w') as w1:
            for magnet in magnets:
                w1.write(magnet)
        exported_sucess_message()


    def setupUi(self, katMainWindow):
        katMainWindow.setObjectName("katMainWindow")
        katMainWindow.setFixedSize(600, 330)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        katMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        katMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(katMainWindow)
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
        katMainWindow.setCentralWidget(self.centralwidget)

        self.scrapeButton.clicked.connect(self.callback)

        self.retranslateUi(katMainWindow)
        QtCore.QMetaObject.connectSlotsByName(katMainWindow)

    def retranslateUi(self, katMainWindow):
        _translate = QtCore.QCoreApplication.translate
        katMainWindow.setWindowTitle(_translate("katMainWindow", "MagnetMagnet - KAT"))
        self.domainComboBox.setItemText(0, _translate("katMainWindow", "https://kat.rip/"))
        self.domainLabel.setText(_translate("katMainWindow", "Choose a KAT domain:"))
        self.categoryComboBox.setItemText(0, _translate("katMainWindow", "All"))
        self.categoryComboBox.setItemText(1, _translate("katMainWindow", "Movies"))
        self.categoryComboBox.setItemText(2, _translate("katMainWindow", "TV"))
        self.categoryComboBox.setItemText(3, _translate("katMainWindow", "Anime"))
        self.categoryComboBox.setItemText(4, _translate("katMainWindow", "Music"))
        self.categoryComboBox.setItemText(5, _translate("katMainWindow", "Books"))
        self.categoryComboBox.setItemText(6, _translate("katMainWindow", "XXX"))
        self.categoryLabel.setText(_translate("katMainWindow", "Choose a category:"))
        self.scrapeButton.setText(_translate("katMainWindow", "Scrape"))
