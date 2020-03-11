from bs4 import BeautifulSoup
from tkinter import *
import tkinter
import time
import pyperclip
import requests


def callback():
    URL1 = entry_1.get()
    category = entry_2.get()
    rssLink = URL1 + 'rssdd.php?category=' + category


    request = requests.get(rssLink)
    print('#############',request.status_code,'#############')
    source = request.content
    soup = str(BeautifulSoup(source, 'lxml'))
    cleanSoup = soup.replace('<', '')
    cleanSoup = cleanSoup.replace('>', '')
    cleanSoup = cleanSoup.replace('link/', '')
    cleanSoup = cleanSoup.replace('\n', ' ')
    splitSoup = cleanSoup.split(' ')
    magnets = [i for i in splitSoup if i.startswith('magnet')]
    magnets = str(magnets).replace('magnet:?', '\nmagnet:?')
    magnets =  str(magnets).replace("', '", "")
    magnets =  str(magnets).replace("['", "")
    magnets =  str(magnets).replace("']", "")


    r = Tk()
    pyperclip.copy(magnets)


    timestr = time.strftime("(%b-%d-%Y)")
    filename = "RARBG Results " + timestr + ".txt"
    print(filename)
    with open(filename,'w') as f:
        for item in magnets:
            f.write(item)


my_window = Tk()
my_window.title("MagnetMagnet RARBG Scraper")
label_1 = Label(my_window, text = "Enter a RARBG mirror domain (make sure the link ends with '/')")
label_2 = Label(my_window, text = "Enter a category number from RARBG (Movies = 'movies'. Movies/x264/1080 = '44')")
entry_1 = Entry(my_window)
entry_2 = Entry(my_window)
button_1 = Button(my_window, text = "OK", command = callback)


label_1.grid(row = 0, column = 0)
entry_1.grid(row = 0, column = 1)
label_2.grid(row = 1, column = 0)
entry_2.grid(row = 1, column = 1)
button_1.grid(row = 2, column = 0)


my_window.mainloop()
