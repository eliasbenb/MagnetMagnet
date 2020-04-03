from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, pyperclip, re, requests

path = '%s\\eliasbenb' %  os.environ['APPDATA']

class Ui_searchMainWindow(object):
    def copy(self):
        choice_row = self.tableTableWidget.currentRow()
        choice_magnet = self.magnets[choice_row]
        pyperclip.copy(choice_magnet)
    def callback(self):
        query = self.queryLineEdit.text()
        def resize():
            self.tableTableWidget.resizeColumnToContents(0)
            self.tableTableWidget.resizeColumnToContents(1)
            self.tableTableWidget.setFixedWidth(self.tableTableWidget.columnWidth(0) + self.tableTableWidget.columnWidth(1))
        def x1377():
            main_link = "https://www.1377x.to/search/" + query + '/1/'
            try:
                main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            main_source = main_request.text
            main_soup = BeautifulSoup(main_source, 'lxml')
            for page_link in main_soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                page_link = "https://www.1377x.to/" + page_link.get('href')
                try:
                    page_request = requests.get(page_link)
                except:
                    ErrorMessage = QtWidgets.QErrorMessage()
                    ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')
                self.magnets.append(page_soup.find('a', attrs={'href': re.compile("^magnet")}).get('href'))
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(page_soup.find('h1').text))

        def kat():
            main_link = "https://kat.rip/usearch/" + query
            try:
                main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            main_source = main_request.text
            main_soup = BeautifulSoup(main_source, 'lxml')
            for page_link in main_soup.findAll('a', class_="cellMainLink"):
                page_link = "https://kat.rip/" + page_link.get('href')
                try:
                    page_request = requests.get(page_link)
                except:
                    ErrorMessage = QtWidgets.QErrorMessage()
                    ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')
                self.magnets.append(page_soup.find('a', attrs={'href': re.compile("^magnet")}).get('href'))
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(page_soup.find('h1').text))

        def nyaa():
            main_link = 'https://nyaa.si/?q=' + query
            try:
                main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')
            rows = main_soup.findAll("td", colspan="2")
            for row in rows:
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                if 'comment' in row.find('a')['title']:
                    self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(row.findAll('a', title=True)[1].text))
                else:
                    self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(row.find('a')['title']))
            for magnet in main_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                self.magnets.append(magnet.get('href'))

        def rarbg():
            main_link = 'https://torrentapi.org/pubapi_v2.php?mode=search&search_string=' + query + '&token=lnjzy73ucv&format=json_extended&app_id=lol'
            try:
                main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml').text
            magnets_soup = main_soup.split('"')
            titles_soup = main_soup.split(",")
            for magnet in magnets_soup:
                if magnet.startswith("magnet:?"):
                    self.magnets.append(magnet)
                else:
                    pass
            for title in titles_soup:
                if title.startswith('{"title":') or title.startswith('{"torrent_results":[{"title":'):
                    row_position = self.tableTableWidget.rowCount()
                    self.tableTableWidget.insertRow(row_position)
                    title = title.replace('"', '')
                    title = title.replace("{torrent_results:[{title:", '')
                    title = title.replace('{title:', '')
                    self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(title))
                else:
                    pass

        def tpb():
            main_link = 'https://tpb.party/search/' + query + '/1/99/0/'
            try:
                main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')
            for magnet in main_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                self.magnets.append(magnet.get('href'))
            for title in main_soup.findAll('div', class_="detName"):
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                title = title.text.replace("\n", "")
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(title))

        if (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            nyaa()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            nyaa()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            nyaa()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            nyaa()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            nyaa()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            rarbg()
            tpb()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            nyaa()
            tpb()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            nyaa()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            kat()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            nyaa()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            tpb()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            nyaa()
            resize()
        elif (self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            tpb()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            nyaa()
            rarbg()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            nyaa()
            tpb()
            resize()
        elif (self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            rarbg()
            tpb()
            resize()
        elif self.x1377CheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            x1377()
            resize()
        elif self.katCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            kat()
            resize()
        elif self.nyaaCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            nyaa()
            resize()
        elif self.rarbgCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            rarbg()
            resize()
        elif self.tpbCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            self.magnets = []
            tpb()
            resize()

    def setupUi(self, searchMainWindow):
        searchMainWindow.setObjectName("searchMainWindow")
        searchMainWindow.setWindowModality(QtCore.Qt.NonModal)
        searchMainWindow.setEnabled(True)
        searchMainWindow.setFixedSize(1500, 400)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        searchMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(searchMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.x1377CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.x1377CheckBox.setGeometry(QtCore.QRect(40, 100, 70, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.x1377CheckBox.setFont(font)
        self.x1377CheckBox.setObjectName("x1377CheckBox")
        self.katCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.katCheckBox.setGeometry(QtCore.QRect(40, 140, 70, 17))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.katCheckBox.setFont(font)
        self.katCheckBox.setObjectName("katCheckBox")
        self.nyaaCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.nyaaCheckBox.setGeometry(QtCore.QRect(40, 180, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.nyaaCheckBox.setFont(font)
        self.nyaaCheckBox.setObjectName("nyaaCheckBox")
        self.rarbgCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rarbgCheckBox.setGeometry(QtCore.QRect(40, 220, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.rarbgCheckBox.setFont(font)
        self.rarbgCheckBox.setObjectName("rarbgCheckBox")
        self.tpbCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.tpbCheckBox.setGeometry(QtCore.QRect(40, 260, 70, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tpbCheckBox.setFont(font)
        self.tpbCheckBox.setObjectName("tpbCheckBox")
        self.tableTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableTableWidget.setGeometry(QtCore.QRect(279, 40, 1190, 321))
        self.tableTableWidget.setObjectName("tableTableWidget")
        self.tableTableWidget.setColumnCount(1)
        self.tableTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTableWidget.setHorizontalHeaderItem(1, item)
        self.searchButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchButton.setGeometry(QtCore.QRect(40, 340, 75, 23))
        self.searchButton.setObjectName("searchButton")
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setGeometry(QtCore.QRect(40, 40, 201, 20))
        self.queryLineEdit.setText("")
        self.queryLineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.queryLineEdit.setObjectName("queryLineEdit")
        searchMainWindow.setCentralWidget(self.centralwidget)

        self.searchButton.clicked.connect(self.callback)
        self.tableTableWidget.itemClicked.connect(self.copy)

        self.retranslateUi(searchMainWindow)
        QtCore.QMetaObject.connectSlotsByName(searchMainWindow)

    def retranslateUi(self, searchMainWindow):
        _translate = QtCore.QCoreApplication.translate
        searchMainWindow.setWindowTitle(_translate("searchMainWindow", "MagnetMagnet - Search"))
        self.x1377CheckBox.setText(_translate("searchMainWindow", "1377x"))
        self.katCheckBox.setText(_translate("searchMainWindow", "KAT"))
        self.nyaaCheckBox.setText(_translate("searchMainWindow", "Nyaa"))
        self.rarbgCheckBox.setText(_translate("searchMainWindow", "RARBG"))
        self.tpbCheckBox.setText(_translate("searchMainWindow", "TPB"))
        item = self.tableTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("searchMainWindow", "Title"))
        self.searchButton.setText(_translate("searchMainWindow", "Search"))
