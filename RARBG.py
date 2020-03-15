from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests

def rarbg():
    def rarbg_callback():
        rarbg_domain = rarbg_domain_entry.get()
        rarbg_category = rarbg_category_entry.get()
        rarbg_clipboard = rarbg_clipboard_combobox.get()
        rarbg_rssLink = rarbg_domain + 'rssdd.php?category=' + rarbg_category
        try:
            rarbg_request = requests.get(rarbg_rssLink)
            if rarbg_request.status_code == 200:
                print(rarbg_request.status_code)
        except:
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        rarbg_request = requests.get(rarbg_rssLink)
        rarbg_source = rarbg_request.content
        rarbg_soup = str(BeautifulSoup(rarbg_source, 'lxml'))

        rarbg_cleanSoup = rarbg_soup.replace('<', ' ')
        rarbg_cleanSoup = rarbg_cleanSoup.replace('>', ' ')
        rarbg_splitSoup = rarbg_cleanSoup.split(' ')

        rarbg_magnets = str([i for i in rarbg_splitSoup if i.startswith('magnet')])
        rarbg_magnets = rarbg_magnets.replace('magnet:?', '\nmagnet:?')
        rarbg_magnets = rarbg_magnets.replace("', '", "")
        rarbg_magnets = rarbg_magnets.replace("['", "")
        rarbg_magnets = rarbg_magnets.replace("']", "")
        rarbg_magnets = rarbg_magnets.replace(r"\n", "")
        rarbg_magnets = "==== Made by @eliasbenb ====" + rarbg_magnets

        if rarbg_clipboard == "Yes":
            pyperclip.copy(rarbg_magnets)
            messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            print("Magnets not copied to clipboard.")

        timestr = time.strftime(" %Y%m%d%H%M%S")
        rarbg_filename = "RARBG Results " + timestr + ".txt"
        print(rarbg_filename)
        with open(rarbg_filename,'w') as f:
            for item in rarbg_magnets:
                f.write(item)
        
        messagebox.showinfo("RARBG Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    rarbg_app = Tk()

    rarbg_domain_text = StringVar()
    rarbg_domain_label = Label(rarbg_app, text="Enter RARBG Domain Link:")
    rarbg_domain_label.place(relx=.5, rely=.1, anchor="center")
    rarbg_domain_entry = Entry(rarbg_app, textvariable=rarbg_domain_text)
    rarbg_domain_entry.place(relx=.5, rely=.20, anchor="center")

    rarbg_category_text = StringVar()
    rarbg_category_label = Label(rarbg_app, text="Enter Category Number:")
    rarbg_category_label.place(relx=.5, rely=.35, anchor="center")
    rarbg_category_entry = Entry(rarbg_app, textvariable=rarbg_category_text)
    rarbg_category_entry.place(relx=.5, rely=.45, anchor="center")

    rarbg_clipboard_label = Label(rarbg_app, text="Copy the Magnets to Clipboard?")
    rarbg_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    rarbg_clipboard_combobox = ttk.Combobox(rarbg_app, values=['Yes', 'No'])
    rarbg_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    rarbg_domain_label.pack()
    rarbg_domain_entry.pack()
    rarbg_category_label.pack()
    rarbg_category_entry.pack()
    rarbg_clipboard_label.pack()
    rarbg_clipboard_combobox.pack()

    rarbg_ok_button = Button(rarbg_app, text = "OK", command = rarbg_callback)
    rarbg_ok_button.place(relx=.5, rely=.91, anchor="center")

    rarbg_app.title('RARBG @eliasbenb')
    rarbg_app.iconbitmap(r'icon.ico')
    rarbg_app.geometry('500x225')
    rarbg_app.mainloop()
