from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests, tkinter.ttk
import os

path = '%s\\eliasbenb' %  os.environ['APPDATA'] 

def kat():
    def kat_callback():
        kat_domain = kat_domain_entry.get()
        kat_category = kat_category_entry.get()
        kat_clipboard = kat_clipboard_combobox.get()
        kat_rssLink = kat_domain + kat_category
        try:
            kat_request = requests.get(kat_rssLink)
        except:
            messagebox.showinfo("KAT Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        kat_soup = str(BeautifulSoup(kat_request.content, 'lxml'))

        kat_cleanSoup = kat_soup.replace('"', '')
        kat_cleanSoup = kat_cleanSoup.replace('href="magnet', 'magnet')
        kat_cleanSoup = kat_cleanSoup.replace("'magnet:?", "magnet:?")
        kat_cleanSoup = kat_cleanSoup.replace("Fannounce'", "Fannounce")
        kat_splitSoup = kat_cleanSoup.split(' ')
        
        kat_magnets = str([i for i in kat_splitSoup if i.startswith('magnet')])
        kat_magnets = kat_magnets.replace("['", "")
        kat_magnets = kat_magnets.replace("']", "")
        kat_magnets = kat_magnets.replace("', 'magnet', '", " ")
        kat_cleanSoup = kat_cleanSoup.replace("',\n'magnet", "")
        kat_magnets = kat_magnets.replace(" ", "\n")
        kat_magnets = "==== Made by @eliasbenb ====" + '\n' + kat_magnets
        print(kat_magnets)

        if kat_clipboard == "Yes":
            pyperclip.copy(kat_magnets)
            messagebox.showinfo("KAT Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

        timestr = time.strftime(" %Y%m%d%H%M%S")
        kat_filename = "KAT Results " + timestr + ".txt"
        with open(kat_filename,'w') as k1:
            for item in kat_magnets:
                k1.write(item)
        
        messagebox.showinfo("KAT Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    def kat_load_config():
        kat_domain_entry.delete(0,tkinter.END)
        kat_category_entry.delete(0,tkinter.END)
        with open(path+"kat_config.env", "r") as k2:
            kat_saved_config = [line.rstrip('\n') for line in k2]
        kat_domain_entry.insert(0,kat_saved_config[0])
        kat_category_entry.insert(0,kat_saved_config[1])
        kat_clipboard_combobox.insert(0, kat_saved_config[2])

    def kat_save_config():
        kat_domain = kat_domain_entry.get()
        kat_category = kat_category_entry.get()
        kat_clipboard = kat_clipboard_combobox.get()
        with open(path+"kat_config.env", "w") as k3:
            k3.write(kat_domain+'\n'+kat_category+'\n'+kat_clipboard)
    
    kat_app = Tk()

    kat_domain_text = StringVar()
    kat_domain_label = Label(kat_app, text="Enter KAT Domain Link:")
    kat_domain_label.place(relx=.5, rely=.1, anchor="center")
    kat_domain_entry = Entry(kat_app, textvariable=kat_domain_text)
    kat_domain_entry.place(relx=.5, rely=.20, anchor="center")

    kat_category_text = StringVar()
    kat_category_label = Label(kat_app, text="Enter Category String:")
    kat_category_label.place(relx=.5, rely=.35, anchor="center")
    kat_category_entry = Entry(kat_app, textvariable=kat_category_text)
    kat_category_entry.place(relx=.5, rely=.45, anchor="center")

    kat_clipboard_label = Label(kat_app, text="Copy the Magnets to Clipboard?")
    kat_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    kat_clipboard_combobox = ttk.Combobox(kat_app, values=['Yes', 'No'])
    kat_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    kat_ok_button = Button(kat_app, text = "OK", command = kat_callback)
    kat_ok_button.place(relx=.5, rely=.91, anchor="center")

    kat_load_config_button = Button(kat_app, text = "Load Config", command = kat_load_config)
    kat_load_config_button.place(relx=0.2, rely=0.5, anchor="center")

    kat_save_config_button = Button(kat_app, text = "Save Config", command = kat_save_config)
    kat_save_config_button.place(relx=0.8, rely=0.5, anchor="center")
    
    kat_app.title('KAT @eliasbenb')
    kat_app.iconbitmap(path+'icon.ico')
    kat_app.geometry('500x225')
    
    kat_app.mainloop()