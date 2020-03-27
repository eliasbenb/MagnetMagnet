from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

path = '%s\\eliasbenb' %  os.environ['APPDATA']

def kat():
    def callback():
        domain = domain_entry.get()
        if not domain.endswith('/'):
            domain += '/'
        category = category_entry.get()
        clipboard = clipboard_combobox.get()
        link = domain + category
        try:
            request = requests.get(link)
        except:
            messagebox.showinfo("KAT Scraper @eliasbenb", "Something went wrong!")

        source = request.content
        soup = BeautifulSoup(source, 'lxml')
        magnets = ['==== Made by @eliasbenb ====']
        for link in soup.findAll('a', attrs={'href': re.compile("^magnet")}):
            magnets.append('\n'+link.get('href'))
        magnets = list(dict.fromkeys(magnets))
        
        timestr = time.strftime(" %Y%m%d%H%M%S")
        file_name = "KAT Results " + timestr + ".txt"
        with open(file_name,'w') as w1:
            for magnet in magnets:
                w1.write(magnet)
        messagebox.showinfo("KAT Scraper @eliasbenb", "Magnet links successfully exported to local directory")

        if clipboard == "Yes":
            magnets_clipboard = str(magnets)
            magnets_clipboard = magnets_clipboard.replace(r"', '\n", "\n")
            magnets_clipboard = magnets_clipboard.replace("['", "")
            magnets_clipboard = magnets_clipboard.replace("']", "")
            pyperclip.copy(magnets_clipboard)
            messagebox.showinfo("KAT Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

    def load_config():
        domain_entry.delete(0,tkinter.END)
        category_entry.delete(0,tkinter.END)
        with open(path+"\\kat_config.env", "r") as r1:
            saved_config = [line.rstrip('\n') for line in r1]
        domain_entry.insert(0,saved_config[0])
        category_entry.insert(0,saved_config[1])
        clipboard_combobox.insert(0, saved_config[2])

    def save_config():
        domain = domain_entry.get()
        category = category_entry.get()
        clipboard = clipboard_combobox.get()
        with open(path+"\\kat_config.env", "w") as w2:
            w2.write(domain+'\n'+category+'\n'+clipboard)
    
    app = Tk()

    domain_text = StringVar(app, value="https://kat.rip/")
    domain_label = Label(app, text="Enter KAT Domain Link:")
    domain_label.place(relx=(1/2), rely=(1/10), anchor="center")
    domain_entry = Entry(app, textvariable=domain_text)
    domain_entry.place(relx=(1/2), rely=(1/5), anchor="center", width=300)

    category_text = StringVar()
    category_label = Label(app, text="Enter Category String:")
    category_label.place(relx=(1/2), rely=(7/20), anchor="center")
    category_entry = Entry(app, textvariable=category_text)
    category_entry.place(relx=(1/2), rely=(9/20), anchor="center")

    clipboard_label = Label(app, text="Copy to Clipboard?")
    clipboard_label.place(relx=(1/2), rely=(3/5), anchor="center")
    clipboard_combobox = ttk.Combobox(app, values=['Yes', 'No'], state='readonly')
    clipboard_combobox.place(relx=(1/2), rely=(7/10), anchor="center")

    ok_button = Button(app, text="OK", command=callback)
    ok_button.place(relx=(1/2), rely=(9/10), anchor="center")

    load_config_button = Button(app, text ="Load Config", command=load_config)
    load_config_button.place(relx=(1/5), rely=(9/20), anchor="center")

    save_config_button = Button(app, text ="Save Config", command=save_config)
    save_config_button.place(relx=(4/5), rely=(9/20), anchor="center")
    
    app.title('KAT @eliasbenb')
    app.iconbitmap(path+'\\icon.ico')
    app.geometry('500x225')
    app.resizable(False, False)
    
    app.mainloop()