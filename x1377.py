from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

x1377_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def x1377():
    def x1377_callback():
        x1377_domain = x1377_domain_entry.get()
        if not x1377_domain.endswith('/'):
            x1377_domain += '/'
        x1377_category = x1377_category_entry.get()
        x1377_clipboard = x1377_clipboard_combobox.get()
        x1377_link = x1377_domain + x1377_category
        try:
            x1377_request = requests.get(x1377_link)
        except:
            messagebox.showinfo("1377x Scraper @eliasbenb", "Something went wrong!")

        x1377_source = x1377_request.content
        x1377_soup = BeautifulSoup(x1377_source, 'lxml')
        x1377_magnets = ['==== Made by @eliasbenb ====']
        for page_link in x1377_soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
            x1377_page_link = 'https://www.1377x.to/' + page_link.get('href')
            try:
                x1377_page_request = requests.get(x1377_page_link)
            except:
                messagebox.showinfo("1377x Scraper @eliasbenb", "Something went wrong!")

            x1377_page_source = x1377_page_request.content
            x1377_page_soup = BeautifulSoup(x1377_page_source, 'lxml')
            for link in x1377_page_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
                x1377_magnets.append('\n'+link.get('href'))
            x1377_magnets = list(dict.fromkeys(x1377_magnets))

        x1377_timestr = time.strftime(" %Y%m%d%H%M%S")
        x1377_file_name = "1377x Results " + x1377_timestr + ".txt"
        with open(x1377_file_name,'w') as w1:
            for magnet in x1377_magnets:
                w1.write(magnet)
        messagebox.showinfo("1377x Scraper @eliasbenb", "Magnet links successfully exported to local directory")

        if x1377_clipboard == "Yes":
            pyperclip.copy(x1377_magnets)
            messagebox.showinfo("1377x Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

    def x1377_load_config():
        x1377_domain_entry.delete(0,tkinter.END)
        x1377_category_entry.delete(0,tkinter.END)
        with open(x1377_path+"\\1377x_config.env", "r") as r1:
            x1377_saved_config = [line.rstrip('\n') for line in r1]
        x1377_domain_entry.insert(0,x1377_saved_config[0])
        x1377_category_entry.insert(0,x1377_saved_config[1])
        x1377_clipboard_combobox.insert(0, x1377_saved_config[2])

    def x1377_save_config():
        x1377_domain = x1377_domain_entry.get()
        x1377_category = x1377_category_entry.get()
        x1377_clipboard = x1377_clipboard_combobox.get()
        with open(x1377_path+"\\1377x_config.env", "w") as w2:
            w2.write(x1377_domain+'\n'+x1377_category+'\n'+x1377_clipboard)
    
    x1377_app = Tk()

    x1377_domain_text = StringVar(x1377_app, value="https://1377x.to/")
    x1377_domain_label = Label(x1377_app, text="Enter 1377x Domain Link:")
    x1377_domain_label.place(relx=(1/2), rely=(1/10), anchor="center")
    x1377_domain_entry = Entry(x1377_app, textvariable=x1377_domain_text)
    x1377_domain_entry.place(relx=(1/2), rely=(1/5), anchor="center", width=300)

    x1377_category_text = StringVar()
    x1377_category_label = Label(x1377_app, text="Enter Category String:")
    x1377_category_label.place(relx=(1/2), rely=(7/20), anchor="center")
    x1377_category_entry = Entry(x1377_app, textvariable=x1377_category_text)
    x1377_category_entry.place(relx=(1/2), rely=(9/20), anchor="center")

    x1377_clipboard_label = Label(x1377_app, text="Copy to Clipboard?")
    x1377_clipboard_label.place(relx=(1/2), rely=(3/5), anchor="center")
    x1377_clipboard_combobox = ttk.Combobox(x1377_app, values=['Yes', 'No'], state='readonly')
    x1377_clipboard_combobox.place(relx=(1/2), rely=(7/10), anchor="center")

    x1377_ok_button = Button(x1377_app, text="OK", command=x1377_callback)
    x1377_ok_button.place(relx=(1/2), rely=(9/10), anchor="center")

    x1377_load_config_button = Button(x1377_app, text ="Load Config", command=x1377_load_config)
    x1377_load_config_button.place(relx=(1/5), rely=(9/20), anchor="center")

    x1377_save_config_button = Button(x1377_app, text ="Save Config", command=x1377_save_config)
    x1377_save_config_button.place(relx=(4/5), rely=(9/20), anchor="center")
    
    x1377_app.title('1377x @eliasbenb')
    x1377_app.iconbitmap(x1377_path+'\\icon.ico')
    x1377_app.geometry('500x225')
    x1377_app.resizable(False, False)
    
    x1377_app.mainloop()