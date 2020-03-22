from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

tpb_path = '%s\\eliasbenb' %  os.environ['APPDATA']

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

        tpb_source = tpb_request.content
        tpb_soup = BeautifulSoup(tpb_source, 'lxml')
        tpb_magnets = ['==== Made by @eliasbenb ====']
        for link in tpb_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
            tpb_magnets.append('\n')
            tpb_magnets.append(link.get('href'))
        
        tpb_timestr = time.strftime(" %Y%m%d%H%M%S")
        tpb_file_name = "TPB Results " + tpb_timestr + ".txt"
        with open(tpb_file_name,'w') as tpb_w1:
            for magnet in tpb_magnets:
                tpb_w1.write(magnet)
        messagebox.showinfo("TPB Scraper @eliasbenb", "Magnet links successfully exported to local directory")

        if tpb_clipboard == "Yes":
            pyperclip.copy(tpb_magnets)
            messagebox.showinfo("TPB Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            pass

    def tpb_load_config():
        tpb_domain_entry.delete(0,tkinter.END)
        tpb_category_entry.delete(0,tkinter.END)
        with open(tpb_path+"\\tpb_config.env", "r") as tpb_r1:
            tpb_saved_config = [line.rstrip('\n') for line in tpb_r1]
        tpb_domain_entry.insert(0,tpb_saved_config[0])
        tpb_category_entry.insert(0,tpb_saved_config[1])
        tpb_clipboard_combobox.insert(0, tpb_saved_config[2])

    def tpb_save_config():
        tpb_domain = tpb_domain_entry.get()
        tpb_category = tpb_category_entry.get()
        tpb_clipboard = tpb_clipboard_combobox.get()
        with open(tpb_path+"\\tpb_config.env", "w") as tpb_w2:
            tpb_w2.write(tpb_domain+'\n'+tpb_category+'\n'+tpb_clipboard)
    
    tpb_app = Tk()

    tpb_domain_text = StringVar()
    tpb_domain_label = Label(tpb_app, text="Enter TPB Domain Link:")
    tpb_domain_label.place(relx=0.5, rely=0.1, anchor="center")
    tpb_domain_entry = Entry(tpb_app, textvariable=tpb_domain_text)
    tpb_domain_entry.place(relx=0.5, rely=0.2, anchor="center")

    tpb_category_text = StringVar()
    tpb_category_label = Label(tpb_app, text="Enter Category String:")
    tpb_category_label.place(relx=0.5, rely=0.35, anchor="center")
    tpb_category_entry = Entry(tpb_app, textvariable=tpb_category_text)
    tpb_category_entry.place(relx=0.5, rely=0.45, anchor="center")

    tpb_clipboard_label = Label(tpb_app, text="Copy the Magnets to Clipboard?")
    tpb_clipboard_label.place(relx=0.5, rely=0.6, anchor="center")
    tpb_clipboard_combobox = ttk.Combobox(tpb_app, values=['Yes', 'No'])
    tpb_clipboard_combobox.place(relx=0.5, rely=0.7, anchor="center")

    tpb_ok_button = Button(tpb_app, text = "OK", command = tpb_callback)
    tpb_ok_button.place(relx=0.5, rely=0.91, anchor="center")

    tpb_load_config_button = Button(tpb_app, text = "Load Config", command = tpb_load_config)
    tpb_load_config_button.place(relx=0.2, rely=0.5, anchor="center")

    tpb_save_config_button = Button(tpb_app, text = "Save Config", command = tpb_save_config)
    tpb_save_config_button.place(relx=0.8, rely=0.5, anchor="center")
    
    tpb_app.title('TPB @eliasbenb')
    tpb_app.iconbitmap(tpb_path+'\\icon.ico')
    tpb_app.geometry('500x225')
    
    tpb_app.mainloop()
