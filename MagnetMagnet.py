from tkinter import *
from tkinter import ttk
from bs4 import BeautifulSoup
import time
import pyperclip
import requests

def callback():
    domain = domain_entry.get()
    category = category_entry.get()
    clipboard = clipboard_combobox.get()
    rssLink = domain + 'rssdd.php?category=' + category

    request = requests.get(rssLink)
    print('#############',request.status_code,'#############')
    source = request.content
    soup = str(BeautifulSoup(source, 'lxml'))

    cleanSoup = soup.replace('<', ' ')
    cleanSoup = cleanSoup.replace('>', ' ')
    splitSoup = cleanSoup.split(' ')

    magnets = str([i for i in splitSoup if i.startswith('magnet')])
    magnets = magnets.replace('magnet:?', '\nmagnet:?')
    magnets = magnets.replace("', '", "")
    magnets = magnets.replace("['", "")
    magnets = magnets.replace("']", "")
    magnets = magnets.replace(r"\n", "")
    magnets = "==== Made by @eliasbenb ====" + magnets

    if clipboard == "Yes":
        pyperclip.copy(magnets)
    else:
        print("Magnets not copied to clipboard")

    timestr = time.strftime(" %Y%m%d%H%M%S")
    filename = "RARBG Results " + timestr + ".txt"
    print(filename)
    with open(filename,'w') as f:
        for item in magnets:
            f.write(item)


app = Tk()

domain_text = StringVar()
domain_label = Label(app, text="Enter RARBG Domain Link:")
domain_label.place(relx=.5, rely=.1, anchor="center")
domain_entry = Entry(app, textvariable=domain_text)
domain_entry.place(relx=.5, rely=.20, anchor="center")

category_text = StringVar()
category_label = Label(app, text="Enter Category Number:")
category_label.place(relx=.5, rely=.35, anchor="center")
category_entry = Entry(app, textvariable=category_text)
category_entry.place(relx=.5, rely=.45, anchor="center")

clipboard_text = StringVar()
clipboard_label = Label(app, text="Copy the Magnets to Clipboard?:")
clipboard_label.place(relx=.5, rely=.60, anchor="center")
clipboard_combobox = ttk.Combobox(app, values=['Yes', 'No'])
clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

ok_button = Button(app, text = "OK", command = callback)
ok_button.place(relx=.5, rely=.91, anchor="center")

app.title('MagnetMagnet - RARBG Scraper')
app.iconbitmap(r'icon.ico')
app.geometry('500x225')

app.mainloop()