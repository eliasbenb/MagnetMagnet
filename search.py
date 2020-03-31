from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup
import os, requests, re

path = '%s\\eliasbenb' %  os.environ['APPDATA']

class Ui_searchMainWindow(object):
    def callback(self):
        query = self.queryLineEdit.text()
        def resize():
            self.tableTableWidget.resizeColumnToContents(0)
            self.tableTableWidget.resizeColumnToContents(1)
            self.tableTableWidget.setFixedWidth(self.tableTableWidget.columnWidth(0) + self.tableTableWidget.columnWidth(1))
        def x1377():
            x1377_link = 'https://www.1377x.to/search/' + query + '/1/'
            try:
                request = requests.get(x1377_link)
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            for page_link in soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                page_link = 'https://www.1377x.to/' + page_link.get('href')
                try:
                    page_request = requests.get(page_link)
                except:
                    ErrorMessage = QtWidgets.QErrorMessage()
                    ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')

                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')
                link = page_soup.find('a', attrs={'href': re.compile("^magnet")})
                magnet = link.get('href')
                title = page_soup.find('h1').text
                rowPosition = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(rowPosition)
                self.tableTableWidget.setItem(rowPosition-1, 0, QtWidgets.QTableWidgetItem(str(title)))
                self.tableTableWidget.setItem(rowPosition-1, 1, QtWidgets.QTableWidgetItem(str(magnet)))
        def kat():
            kat_link = 'http://kat.rip/usearch/' + query
            try:
                request = requests.get(kat_link)
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            titles_all = soup.findAll('a', class_="cellMainLink")
            titles = []
            rowPositionBefore = self.tableTableWidget.rowCount()
            for title in titles_all:
                title = title.text
                rowPosition = self.tableTableWidget.rowCount()
                if title not in titles:
                    titles.append(title)
                    self.tableTableWidget.insertRow(rowPosition)
                    self.tableTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(title))
                else:
                    pass
            links = soup.findAll('a', title="Torrent magnet link")
            n = rowPositionBefore
            for link in links:
                link = link['href']
                self.tableTableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(link))
                n = n + 1
        def nyaa():
            nyaa_link = 'https://nyaa.si/?q=' + query
            try:
                request = requests.get(nyaa_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            source = request.content
            soup = BeautifulSoup(source, 'lxml')
            rows = soup.findAll("td", colspan="2")
            rowPositionBefore = self.tableTableWidget.rowCount()
            for row in rows:
                if 'comment' in row.find('a')['title']:
                    title = row.findAll('a', title=True)[1].text
                    rowPosition = self.tableTableWidget.rowCount()
                    self.tableTableWidget.insertRow(rowPosition)
                    self.tableTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(title))
                else:
                    title = row.find('a')['title']
                    rowPosition = self.tableTableWidget.rowCount()
                    self.tableTableWidget.insertRow(rowPosition)
                    self.tableTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(title))
            n = rowPositionBefore
            for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                self.tableTableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(link.get('href')))
                n = n + 1
        def rarbg():
            rarbg_link = 'https://torrentapi.org/pubapi_v2.php?mode=search&search_string=' + query + '&token=lnjzy73ucv&format=json_extended&app_id=lol'
            try:
                request = requests.get(rarbg_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            source = request.text
            soup = str(BeautifulSoup(source, 'lxml'))
            soup = soup.replace('<html><body><p>{"torrent_results":[', '')
            soup = soup.split(',')
            titles = str([i for i in soup if i.startswith('{"title":')])
            titles = titles.replace('{"title":"', '')
            titles = titles.replace('"', '')
            titles = titles.split("', '")
            titles[0] = titles[0].replace("['", "")
            rowPositionBefore = self.tableTableWidget.rowCount()
            for title in titles:
                rowPosition = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(rowPosition)
                self.tableTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(title))
            links = str([i for i in soup if i.startswith('"download":')])
            links = links.replace('"download":"', '')
            links = links.replace('"', '')
            links = links.replace("['", "")
            links = links.replace("']", "")
            links = links.split("', '")
            n = rowPositionBefore
            for link in links:
                self.tableTableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(link))
                n = n + 1
        def tpb():
            tpb_link = 'https://tpb.party/search/' + query + '/1/99/0/'
            try:
                request = requests.get(tpb_link)
            except:
                ErrorMessage = QtWidgets.QErrorMessage()
                ErrorMessage.showMessage('Something went wrong! Please message me on GitHub!')
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            titles_all = soup.findAll('div', class_="detName")
            titles = []
            rowPositionBefore = self.tableTableWidget.rowCount()
            for title in titles_all:
                title = title.text
                rowPosition = self.tableTableWidget.rowCount()
                if title not in titles:
                    titles.append(title)
                    self.tableTableWidget.insertRow(rowPosition)
                    self.tableTableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(title))
                else:
                    pass
            links = soup.findAll('a', title="Download this torrent using magnet")
            n = rowPositionBefore
            for m in links:
                self.tableTableWidget.setItem(n, 1, QtWidgets.QTableWidgetItem(m['href']))
                n = n + 1

        if (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            nyaa()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            nyaa()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            nyaa()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            nyaa()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            nyaa()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            nyaa()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            rarbg()
            tpb()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            nyaa()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            nyaa()
            tpb()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            nyaa()
            rarbg()
            tpb()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.katCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            kat()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            nyaa()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            rarbg()
            resize()
        elif (self.x1377CheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            x1377()
            tpb()
            resize()
        elif (self.katCheckBox.isChecked() and self.nyaaCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            nyaa()
            resize()
        elif (self.katCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            rarbg()
            resize()
        elif (self.katCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            kat()
            tpb()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.rarbgCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            nyaa()
            rarbg()
            resize()
        elif (self.nyaaCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            nyaa()
            tpb()
            resize()
        elif (self.rarbgCheckBox.isChecked() and self.tpbCheckBox.isChecked()):
            self.tableTableWidget.setRowCount(0)
            rarbg()
            tpb()
            resize()
        elif self.x1377CheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            x1377()
            resize()
        elif self.katCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            kat()
            resize()
        elif self.nyaaCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            nyaa()
            resize()
        elif self.rarbgCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
            rarbg()
            resize()
        elif self.tpbCheckBox.isChecked():
            self.tableTableWidget.setRowCount(0)
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
        self.tableTableWidget.setColumnCount(2)
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
        item = self.tableTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("searchMainWindow", "Magnet"))
        self.searchButton.setText(_translate("searchMainWindow", "Search"))
