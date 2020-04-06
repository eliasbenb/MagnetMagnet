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
            self.tableTableWidget.resizeColumnToContents(2)
        def x1377():
            main_link = "https://www.1377x.to/search/" + query + '/1/'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')
            
            page_links_soup = main_soup.findAll('a', attrs={'href': re.compile("^/torrent/")})
            for page_link in page_links_soup:
                page_link = "https://1377x.to" + page_link.get('href')
                page_request = requests.get(page_link, headers={'User-Agent': 'Mozilla/5.0'})
                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')

                title = page_soup.find('h1').text
                seeders = page_soup.find('span', class_="seeds").text
                leechers = page_soup.find('span', class_="leeches").text
                magnet = page_soup.find('a', attrs={'href': re.compile("^magnet:?")}).get('href')

                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(title))
                self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders))
                self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers))
                self.magnets.append(magnet)

        def kat():
            main_link = "https://kat.rip/usearch/" + query
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            titles_soup = main_soup.findAll('a', class_="cellMainLink")
            seeders_soup = main_soup.findAll('td', class_="green center")
            leechers_soup = main_soup.findAll('td', class_="red lasttd center")
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet:?"), 'title': "Torrent magnet link"})

            titles = []
            seeders = []
            leechers = []
            for title in titles_soup:
                titles.append(title.text)
            for seeder in seeders_soup:
                seeders.append(seeder.text)
            for leecher in leechers_soup:
                leechers.append(leecher.text)
            count1 = 0
            for magnet in magnets_soup:
                self.magnets.append(magnet.get('href'))
                count1 = count1 + 1
            
            count2 = 0
            while count2 < count1:
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
                self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
                self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
                count2 = count2 + 1

        def nyaa():
            main_link = 'https://nyaa.si/?q=' + query
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            titles_soup = main_soup.findAll('a', title=True, class_=False, attrs={'href': re.compile("^/view/")})
            seeders_soup = main_soup.findAll('td', class_="text-center")
            leechers_soup = main_soup.findAll('td', class_="text-center")
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet:?")})

            titles = []
            seeders = []
            leechers = []
            for title in titles_soup:
                titles.append(title.text)
            for seeder in seeders_soup:
                seeders.append(seeder.text)
            for leecher in leechers_soup:
                leechers.append(leecher.text)
            count1 = 0
            for magnet in magnets_soup:
                self.magnets.append(magnet.get('href'))
                count1 = count1 + 1

            seeder1 = seeders[3]
            seeders.pop(0)
            seeders.pop(1)
            seeders.pop(2)
            seeders.pop(3)
            seeders = seeders[6-1::6]
            seeders.insert(0,seeder1)

            leecher1 = leechers[4]
            leechers.pop(0)
            leechers.pop(1)
            leechers.pop(2)
            leechers.pop(3)
            leechers.pop(4)
            leechers = leechers[6-1::6]
            leechers.insert(0,leecher1)

            count2 = 0
            while count2 < count1:
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
                self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
                self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
                count2 = count2 + 1

        def rarbg():
            main_link = 'https://torrentapi.org/pubapi_v2.php?mode=search&search_string=' + query + '&token=lnjzy73ucv&format=json_extended&app_id=lol'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml').text

            titles_soup = main_soup.split(",")
            seeders_soup = main_soup.split(',"')
            leechers_soup = main_soup.split(',"')
            magnets_soup = main_soup.split('"')

            titles = []
            seeders = []
            leechers = []
            for title in titles_soup:
                if title.startswith('{"title":') or title.startswith('{"torrent_results":[{"title":'):
                    title = title.replace('"', '')
                    title = title.replace("{torrent_results:[{title:", '')
                    title = title.replace('{title:', '')
                    titles.append(title)
            for seeder in seeders_soup:
                if seeder.startswith('seeders":'):
                    seeder = seeder.replace('seeders":', '')
                    seeders.append(seeder)
            for leecher in leechers_soup:
                if leecher.startswith('leechers":'):
                    leecher = leecher.replace('leechers":', '')
                    leechers.append(leecher)
            count1 = 0
            for magnet in magnets_soup:
                if magnet.startswith("magnet:?"):
                    self.magnets.append(magnet.startswith("magnet:?"))
                    count1 = count1 + 1

            count2 = 0
            while count2 < count1:
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
                self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
                self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
                count2 = count2 + 1

        def tpb():
            main_link = 'https://tpb.party/search/' + query + '/1/99/0/'
            main_request = requests.get(main_link, headers={'User-Agent': 'Mozilla/5.0'})
            main_source = main_request.content
            main_soup = BeautifulSoup(main_source, 'lxml')

            titles_soup = main_soup.findAll('div', class_="detName")
            seeders_soup = main_soup.findAll('td', attrs={'align': "right"})
            seeders_soup = seeders_soup[0::2]
            leechers_soup = main_soup.findAll('td', attrs={'align': "right"})
            leechers_soup = leechers_soup[1::2]
            magnets_soup = main_soup.findAll('a', attrs={'href': re.compile("^magnet")})

            titles = []
            seeders = []
            leechers = []
            for title in titles_soup:
                title = title.text.replace("\n", "")
                titles.append(title)
            for seeder in seeders_soup:
                seeders.append(seeder.text)
            for leecher in leechers_soup:
                leechers.append(leecher.text)
            count1 = 0
            for magnet in magnets_soup:
                self.magnets.append(magnet.get('href'))
                count1 = count1 + 1

            print(len(titles))
            print(len(seeders))
            print(len(leechers))
            print(len(self.magnets))

            count2 = 0
            while count2 < count1:
                row_position = self.tableTableWidget.rowCount()
                self.tableTableWidget.insertRow(row_position)
                self.tableTableWidget.setItem(row_position, 0, QtWidgets.QTableWidgetItem(titles[count2]))
                self.tableTableWidget.setItem(row_position, 1, QtWidgets.QTableWidgetItem(seeders[count2]))
                self.tableTableWidget.setItem(row_position, 2, QtWidgets.QTableWidgetItem(leechers[count2]))
                count2 = count2 + 1

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
        searchMainWindow.setFixedSize(1500, 400)
        font = QtGui.QFont()
        font.setFamily("Bahnschrift Light")
        font.setPointSize(11)
        searchMainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(path+r"/images/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        searchMainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(searchMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.queryLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.queryLineEdit.setGeometry(QtCore.QRect(30, 20, 200, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.queryLineEdit.setFont(font)
        self.queryLineEdit.setObjectName("queryLineEdit")
        self.x1377CheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.x1377CheckBox.setGeometry(QtCore.QRect(30, 70, 90, 20))
        self.x1377CheckBox.setObjectName("x1377CheckBox")
        self.tableTableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableTableWidget.setGeometry(QtCore.QRect(260, 20, 1210, 360))
        self.tableTableWidget.setObjectName("tableTableWidget")
        self.tableTableWidget.setColumnCount(3)
        self.tableTableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableTableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableTableWidget.setHorizontalHeaderItem(2, item)
        self.katCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.katCheckBox.setGeometry(QtCore.QRect(30, 110, 90, 20))
        self.katCheckBox.setObjectName("katCheckBox")
        self.nyaaCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.nyaaCheckBox.setGeometry(QtCore.QRect(30, 150, 90, 20))
        self.nyaaCheckBox.setObjectName("nyaaCheckBox")
        self.rarbgCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.rarbgCheckBox.setGeometry(QtCore.QRect(30, 190, 90, 20))
        self.rarbgCheckBox.setObjectName("rarbgCheckBox")
        self.tpbCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.tpbCheckBox.setGeometry(QtCore.QRect(30, 230, 90, 20))
        self.tpbCheckBox.setObjectName("tpbCheckBox")
        self.searchPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.searchPushButton.setGeometry(QtCore.QRect(30, 350, 90, 30))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.searchPushButton.setFont(font)
        self.searchPushButton.setObjectName("searchPushButton")
        searchMainWindow.setCentralWidget(self.centralwidget)

        self.searchPushButton.clicked.connect(self.callback)
        self.tableTableWidget.itemClicked.connect(self.copy)

        self.retranslateUi(searchMainWindow)
        QtCore.QMetaObject.connectSlotsByName(searchMainWindow)

    def retranslateUi(self, searchMainWindow):
        _translate = QtCore.QCoreApplication.translate
        searchMainWindow.setWindowTitle(_translate("searchMainWindow", "MagnetMagnet - Search"))
        self.x1377CheckBox.setText(_translate("searchMainWindow", "1377x"))
        item = self.tableTableWidget.horizontalHeaderItem(0)
        item.setText(_translate("searchMainWindow", "Titles"))
        item = self.tableTableWidget.horizontalHeaderItem(1)
        item.setText(_translate("searchMainWindow", "Seeders"))
        item = self.tableTableWidget.horizontalHeaderItem(2)
        item.setText(_translate("searchMainWindow", "Leechers"))
        self.katCheckBox.setText(_translate("searchMainWindow", "KAT"))
        self.nyaaCheckBox.setText(_translate("searchMainWindow", "Nyaa"))
        self.rarbgCheckBox.setText(_translate("searchMainWindow", "RARBG"))
        self.tpbCheckBox.setText(_translate("searchMainWindow", "TPB"))
        self.searchPushButton.setText(_translate("searchMainWindow", "Search"))