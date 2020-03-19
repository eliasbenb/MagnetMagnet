from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests, tkinter.ttk
import os

path = '%s\\eliasbenb' %  os.environ['APPDATA']

def tpb():
    def tpb_callback():
        tpb_domain = tpb_domain_entry.get()
        tpb_category = tpb_category_entry.get()
        tpb_clipboard = tpb_clipboard_combobox.get()
        tpb_link = tpb_domain + 'browse/' + tpb_category
        try:
            tpb_request = requests.get(tpb_link)
        except:
            messagebox.showinfo("TPB Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        tpb_request = requests.get(tpb_link)
        tpb_soup = str(BeautifulSoup(tpb_request.content, 'html.parser'))
        tpb_clean_soup = tpb_soup.replace('"', " ")
        tpb_split_soup = tpb_clean_soup.split(" ")
        tpb_magnets = str([i for i in tpb_split_soup if i.startswith('magnet')])
        tpb_magnets = tpb_magnets.replace('magnet:?', '\nmagnet:?')
        tpb_magnets = tpb_magnets.replace("', '", "")
        tpb_magnets = tpb_magnets.replace("['", "")
        tpb_magnets = tpb_magnets.replace("']", "")
        tpb_magnets = tpb_magnets.replace(r"\n", "")
        tpb_magnets = "==== Made by @eliasbenb ====" + tpb_magnets

        if tpb_clipboard == "Yes":
            pyperclip.copy(tpb_magnets)
            messagebox.showinfo("TPB Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

        timestr = time.strftime(" %Y%m%d%H%M%S")
        tpb_filename = "TPB Results " + timestr + ".txt"
        with open(tpb_filename,'w') as t1:
            for item in tpb_magnets:
                t1.write(item)
        
        messagebox.showinfo("TPB Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    def tpb_load_config():
        tpb_domain_entry.delete(0,tkinter.END)
        tpb_category_entry.delete(0,tkinter.END)
        with open(path+"\tpb_config.env", "r") as t2:
            tpb_saved_config = [line.rstrip('\n') for line in t2]
        tpb_domain_entry.insert(0,tpb_saved_config[0])
        tpb_category_entry.insert(0,tpb_saved_config[1])
        tpb_clipboard_combobox.insert(0, tpb_saved_config[2])

    def tpb_save_config():
        tpb_domain = tpb_domain_entry.get()
        tpb_category = tpb_category_entry.get()
        tpb_clipboard = tpb_clipboard_combobox.get()
        with open(path+"\tpb_config.env", "w") as t3:
            t3.write(tpb_domain+'\n'+tpb_category+'\n'+tpb_clipboard)

    tpb_app = Tk()

    tpb_domain_text = StringVar()
    tpb_domain_label = Label(tpb_app, text="Enter TPB Domain Link:")
    tpb_domain_label.place(relx=.5, rely=.1, anchor="center")
    tpb_domain_entry = Entry(tpb_app, textvariable=tpb_domain_text)
    tpb_domain_entry.place(relx=.5, rely=.20, anchor="center")

    tpb_category_text = StringVar()
    tpb_category_label = Label(tpb_app, text="Enter Category String:")
    tpb_category_label.place(relx=.5, rely=.35, anchor="center")
    tpb_category_entry = Entry(tpb_app, textvariable=tpb_category_text)
    tpb_category_entry.place(relx=.5, rely=.45, anchor="center")

    tpb_clipboard_label = Label(tpb_app, text="Copy the Magnets to Clipboard?")
    tpb_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    tpb_clipboard_combobox = ttk.Combobox(tpb_app, values=['Yes', 'No'])
    tpb_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    tpb_ok_button = Button(tpb_app, text = "OK", command = tpb_callback)
    tpb_ok_button.place(relx=.5, rely=.91, anchor="center")

    tpb_load_config_button = Button(tpb_app, text = "Load Config", command = tpb_load_config)
    tpb_load_config_button.place(relx=0.2, rely=0.5, anchor="center")

    tpb_save_config_button = Button(tpb_app, text = "Save Config", command = tpb_save_config)
    tpb_save_config_button.place(relx=0.8, rely=0.5, anchor="center")    

    tpb_app.title('\TPB @eliasbenb')
    tpb_app.iconbitmap(path+'icon.ico')
    tpb_app.geometry('500x225')
    
    tpb_app.mainloop()
