from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import src.mglobals, os, requests, re, time

path = src.mglobals.base_path

class Ui_tpbMainWindow(object):
    def callback(self):
        try:
            def exported_sucess_message():
                successMessageBox = QtWidgets.QMessageBox()
                successMessageBox.setIcon(QtWidgets.QMessageBox.Information)

                successMessageBox.setText("Magnet links have been successfully exported to the local directory.")
                successMessageBox.setWindowTitle("Task Completed!")
                successMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(src.mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                successMessageBox.setWindowIcon(icon)
                    
                successMessageBox.exec_()

            def error_message():
                errorMessageBox = QtWidgets.QMessageBox()
                errorMessageBox.setIcon(QtWidgets.QMessageBox.Information)

                errorMessageBox.setText("Something went wrong! Please inform me through GitHub!")
                errorMessageBox.setWindowTitle("Error!")
                errorMessageBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(src.mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                errorMessageBox.setWindowIcon(icon)
                    
                errorMessageBox.exec_()  

            domain = str(self.domainComboBox.currentText())
            category = str(self.categoryComboBox.currentText())

            if category == "All":
                category = "recent"
            if category == "Movies - HD":
                category = "browse/207"
            if category == "Movies - Not HD":
                category = "browse/201"
            if category == "TV - HD":
                category = "browse/208"
            if category == "TV - Not HD":
                category = "browse/205"
            if category == "Music - All":
                category = "browse/101"            
            if category == "XXX - All":
                category = "browse/500"

            link = domain + category
            request = requests.get(link)
            source = request.content
            soup = BeautifulSoup(source, 'lxml')

            magnets = ['==== Made by @eliasbenb ====']
            for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                magnets.append('\n')
                magnets.append(link.get('href'))
            
            timestr = time.strftime(" %Y%m%d%H%M%S")
            file_name = "TPB Results " + timestr + ".txt"
            with open(file_name,'w') as w1:
                for magnet in magnets:
                    w1.write(magnet)
            exported_sucess_message()
        except:
            error_message()

    def setupUi(self, tpbMainWindow):
        tpbMainWindow.setObjectName("tpbMainWindow")
        tpbMainWindow.setFixedSize(600, 330)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        tpbMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(src.mglobals.icon), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        tpbMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(tpbMainWindow)
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
        tpbMainWindow.setCentralWidget(self.centralwidget)

        self.scrapeButton.clicked.connect(self.callback)

        self.retranslateUi(tpbMainWindow)
        QtCore.QMetaObject.connectSlotsByName(tpbMainWindow)

    def retranslateUi(self, tpbMainWindow):
        _translate = QtCore.QCoreApplication.translate
        tpbMainWindow.setWindowTitle(_translate("tpbMainWindow", "MagnetMagnet - TPB"))
        self.domainComboBox.setItemText(0, _translate("tpbMainWindow", "https://tpb.party/"))
        self.domainLabel.setText(_translate("tpbMainWindow", "Choose a TPB domain:"))
        self.categoryComboBox.setItemText(0, _translate("tpbMainWindow", "All"))
        self.categoryComboBox.setItemText(1, _translate("tpbMainWindow", "Movies - HD"))
        self.categoryComboBox.setItemText(2, _translate("tpbMainWindow", "Movies - Not HD"))
        self.categoryComboBox.setItemText(3, _translate("tpbMainWindow", "TV - HD"))
        self.categoryComboBox.setItemText(4, _translate("tpbMainWindow", "TV - Not HD"))
        self.categoryComboBox.setItemText(5, _translate("tpbMainWindow", "Music - All"))
        self.categoryComboBox.setItemText(6, _translate("tpbMainWindow", "XXX - All"))
        self.categoryLabel.setText(_translate("tpbMainWindow", "Choose a category:"))
        self.scrapeButton.setText(_translate("tpbMainWindow", "Scrape"))
