from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests

def RARBG():
    def RARBG_callback():
        RARBG_domain = RARBG_domain_entry.get()
        RARBG_category = RARBG_category_entry.get()
        RARBG_clipboard = RARBG_clipboard_combobox.get()
        RARBG_rssLink = RARBG_domain + 'rssdd.php?category=' + RARBG_category
        try:
            RARBG_request = requests.get(RARBG_rssLink)
            if RARBG_request.status_code == 200:
                print(RARBG_request.status_code)
        except:
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        RARBG_request = requests.get(RARBG_rssLink)
        RARBG_source = RARBG_request.content
        RARBG_soup = str(BeautifulSoup(RARBG_source, 'lxml'))

        RARBG_cleanSoup = RARBG_soup.replace('<', ' ')
        RARBG_cleanSoup = RARBG_cleanSoup.replace('>', ' ')
        RARBG_splitSoup = RARBG_cleanSoup.split(' ')

        RARBG_magnets = str([i for i in RARBG_splitSoup if i.startswith('magnet')])
        RARBG_magnets = RARBG_magnets.replace('magnet:?', '\nmagnet:?')
        RARBG_magnets = RARBG_magnets.replace("', '", "")
        RARBG_magnets = RARBG_magnets.replace("['", "")
        RARBG_magnets = RARBG_magnets.replace("']", "")
        RARBG_magnets = RARBG_magnets.replace(r"\n", "")
        RARBG_magnets = "==== Made by @eliasbenb ====" + RARBG_magnets

        if RARBG_clipboard == "Yes":
            pyperclip.copy(RARBG_magnets)
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            print("Magnets not copied to clipboard")

        timestr = time.strftime(" %Y%m%d%H%M%S")
        RARBG_filename = "RARBG Results " + timestr + ".txt"
        print(RARBG_filename)
        with open(RARBG_filename,'w') as f:
            for item in RARBG_magnets:
                f.write(item)
        
        messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    RARBG_app = Tk()

    RARBG_domain_text = StringVar()
    RARBG_domain_label = Label(RARBG_app, text="Enter RARBG Domain Link:")
    RARBG_domain_label.place(relx=.5, rely=.1, anchor="center")
    RARBG_domain_entry = Entry(RARBG_app, textvariable=RARBG_domain_text)
    RARBG_domain_entry.place(relx=.5, rely=.20, anchor="center")

    RARBG_category_text = StringVar()
    RARBG_category_label = Label(RARBG_app, text="Enter Category Number:")
    RARBG_category_label.place(relx=.5, rely=.35, anchor="center")
    RARBG_category_entry = Entry(RARBG_app, textvariable=RARBG_category_text)
    RARBG_category_entry.place(relx=.5, rely=.45, anchor="center")

    RARBG_clipboard_label = Label(RARBG_app, text="Copy the Magnets to Clipboard?")
    RARBG_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    RARBG_clipboard_combobox = ttk.Combobox(RARBG_app, values=['Yes', 'No'])
    RARBG_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    RARBG_domain_label.pack()
    RARBG_domain_entry.pack()
    RARBG_category_label.pack()
    RARBG_category_entry.pack()
    RARBG_clipboard_label.pack()
    RARBG_clipboard_combobox.pack()

    RARBG_ok_button = Button(RARBG_app, text = "OK", command = RARBG_callback)
    RARBG_ok_button.place(relx=.5, rely=.91, anchor="center")

    RARBG_app.title('RARBG @eliasbenb')
    RARBG_app.iconbitmap(r'icon.ico')
    RARBG_app.geometry('500x225')
    RARBG_app.mainloop()
