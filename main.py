from PyQt5.QtWidgets import QMainWindow, QApplication
import sys, webbrowser

from home import Ui_homeMainWindow
from search import Ui_searchMainWindow
from x1377 import Ui_x1337MainWindow
from kat import Ui_katMainWindow
from nyaa import Ui_nyaaMainWindow
from rarbg import Ui_rarbgMainWindow
from tpb import Ui_tpbMainWindow

class HomeWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_homeMainWindow()
        self.ui.setupUi(self)
    def search(self):
        self.SearchWindow = SearchWindow()
        self.SearchWindow.show()
    def x1377(self):
        self.x1377Window = x1377Window()
        self.x1377Window.show()
    def kat(self):
        self.katWindow = katWindow()
        self.katWindow.show()
    def nyaa(self):
        self.nyaaWindow = nyaaWindow()
        self.nyaaWindow.show()
    def rarbg(self):
        self.rarbgWindow = rarbgWindow()
        self.rarbgWindow.show()
    def tpb(self):
        self.tpbWindow = tpbWindow()
        self.tpbWindow.show()
    def website(self):
        webbrowser.open('http://eliasbenb.github.io/')
    def github(self):
        webbrowser.open('http://github.com/eliasbenb/MagnetMagnet')

class SearchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_searchMainWindow()
        self.ui.setupUi(self)
class x1377Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_x1337MainWindow()
        self.ui.setupUi(self)
class katWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_katMainWindow()
        self.ui.setupUi(self)
class nyaaWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_nyaaMainWindow()
        self.ui.setupUi(self)
class rarbgWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_rarbgMainWindow()
        self.ui.setupUi(self)
class tpbWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_tpbMainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = HomeWindow()
    w.show()
    sys.exit(app.exec_())