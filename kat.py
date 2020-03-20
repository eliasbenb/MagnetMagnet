from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

kat_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def kat():
    def kat_callback():
        kat_domain = kat_domain_entry.get()
        kat_category = kat_category_entry.get()
        kat_clipboard = kat_clipboard_combobox.get()
        kat_link = kat_domain + kat_category
        try:
            kat_request = requests.get(kat_link)
        except:
            messagebox.showinfo("KAT Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        kat_source = kat_request.content
        kat_soup = BeautifulSoup(kat_source, 'lxml')
        kat_magnets = ['==== Made by @eliasbenb ====']
        for link in kat_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
            kat_magnets.append('\n'+link.get('href'))
        kat_magnets = list(dict.fromkeys(kat_magnets))
        
        kat_timestr = time.strftime(" %Y%m%d%H%M%S")
        kat_file_name = "KAT Results " + kat_timestr + ".txt"
        with open(kat_file_name,'w') as kat_w1:
            for magnet in kat_magnets:
                kat_w1.write(magnet)
        messagebox.showinfo("KAT Scraper @eliasbenb", "Magnet links successfully exported to local directory")

        if kat_clipboard == "Yes":
            kat_magnets_clipboard = str(kat_magnets)
            kat_magnets_clipboard = kat_magnets_clipboard.replace(r"', '\n", "\n")
            kat_magnets_clipboard = kat_magnets_clipboard.replace("['", "")
            kat_magnets_clipboard = kat_magnets_clipboard.replace("']", "")
            pyperclip.copy(kat_magnets_clipboard)
            messagebox.showinfo("KAT Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

    def kat_load_config():
        kat_domain_entry.delete(0,tkinter.END)
        kat_category_entry.delete(0,tkinter.END)
        with open(kat_path+"\\kat_config.env", "r") as kat_r1:
            kat_saved_config = [line.rstrip('\n') for line in kat_r1]
        kat_domain_entry.insert(0,kat_saved_config[0])
        kat_category_entry.insert(0,kat_saved_config[1])
        kat_clipboard_combobox.insert(0, kat_saved_config[2])

    def kat_save_config():
        kat_domain = kat_domain_entry.get()
        kat_category = kat_category_entry.get()
        kat_clipboard = kat_clipboard_combobox.get()
        with open(kat_path+"\\kat_config.env", "w") as kat_w2:
            kat_w2.write(kat_domain+'\n'+kat_category+'\n'+kat_clipboard)
    
    kat_app = Tk()

    kat_domain_text = StringVar()
    kat_domain_label = Label(kat_app, text="Enter KAT Domain Link:")
    kat_domain_label.place(relx=0.5, rely=0.1, anchor="center")
    kat_domain_entry = Entry(kat_app, textvariable=kat_domain_text)
    kat_domain_entry.place(relx=0.5, rely=0.2, anchor="center")

    kat_category_text = StringVar()
    kat_category_label = Label(kat_app, text="Enter Category String:")
    kat_category_label.place(relx=0.5, rely=0.35, anchor="center")
    kat_category_entry = Entry(kat_app, textvariable=kat_category_text)
    kat_category_entry.place(relx=0.5, rely=0.45, anchor="center")

    kat_clipboard_label = Label(kat_app, text="Copy the Magnets to Clipboard?")
    kat_clipboard_label.place(relx=0.5, rely=0.6, anchor="center")
    kat_clipboard_combobox = ttk.Combobox(kat_app, values=['Yes', 'No'])
    kat_clipboard_combobox.place(relx=0.5, rely=0.7, anchor="center")

    kat_ok_button = Button(kat_app, text = "OK", command = kat_callback)
    kat_ok_button.place(relx=0.5, rely=0.91, anchor="center")

    kat_load_config_button = Button(kat_app, text = "Load Config", command = kat_load_config)
    kat_load_config_button.place(relx=0.2, rely=0.5, anchor="center")

    kat_save_config_button = Button(kat_app, text = "Save Config", command = kat_save_config)
    kat_save_config_button.place(relx=0.8, rely=0.5, anchor="center")
    
    kat_app.title('KAT @eliasbenb')
    kat_app.iconbitmap(kat_path+'\\icon.ico')
    kat_app.geometry('500x225')
    
    kat_app.mainloop()