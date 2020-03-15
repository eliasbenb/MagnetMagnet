from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from bs4 import BeautifulSoup
import time, os, pyperclip, requests

def TPB():
    def TPB_callback():
        TPB_domain = TPB_domain_entry.get()
        TPB_category = TPB_category_entry.get()
        TPB_clipboard = TPB_clipboard_combobox.get()
        TPB_rssLink = TPB_domain + 'rss/' + TPB_category
        try:
            TPB_request = requests.get(TPB_rssLink)
            if TPB_request.status_code == 200:
                print(TPB_request.status_code)
        except:
            messagebox.showinfo("TPB Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")

        TPB_request = requests.get(TPB_rssLink)
        TPB_source = TPB_request.content
        TPB_soup = str(BeautifulSoup(TPB_source, 'lxml'))

        TPB_cleanSoup = TPB_soup.replace('<', ' ')
        TPB_cleanSoup = TPB_cleanSoup.replace('>', ' ')
        TPB_splitSoup = TPB_cleanSoup.split(' ')

        TPB_magnets = str([i for i in TPB_splitSoup if i.startswith('magnet')])
        TPB_magnets = TPB_magnets.replace('magnet:?', '\nmagnet:?')
        TPB_magnets = TPB_magnets.replace("', '", "")
        TPB_magnets = TPB_magnets.replace("['", "")
        TPB_magnets = TPB_magnets.replace("']", "")
        TPB_magnets = TPB_magnets.replace(r"\n", "")
        TPB_magnets = "==== Made by @eliasbenb ====" + TPB_magnets

        if TPB_clipboard == "Yes":
            pyperclip.copy(TPB_magnets)
            messagebox.showinfo("TPB Scraper @eliasbenb", "Magnets links successfully copied to clipboard")
        else:
            print("Magnets not copied to clipboard")

        timestr = time.strftime(" %Y%m%d%H%M%S")
        TPB_filename = "TPB Results " + timestr + ".txt"
        print(TPB_filename)
        with open(TPB_filename,'w') as f:
            for item in TPB_magnets:
                f.write(item)
        
        messagebox.showinfo("TPB Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    TPB_app = Tk()

    TPB_domain_text = StringVar()
    TPB_domain_label = Label(TPB_app, text="Enter TPB Domain Link:")
    TPB_domain_label.place(relx=.5, rely=.1, anchor="center")
    TPB_domain_entry = Entry(TPB_app, textvariable=TPB_domain_text)
    TPB_domain_entry.place(relx=.5, rely=.20, anchor="center")

    TPB_category_text = StringVar()
    TPB_category_label = Label(TPB_app, text="Enter Category Number:")
    TPB_category_label.place(relx=.5, rely=.35, anchor="center")
    TPB_category_entry = Entry(TPB_app, textvariable=TPB_category_text)
    TPB_category_entry.place(relx=.5, rely=.45, anchor="center")

    TPB_clipboard_label = Label(TPB_app, text="Copy the Magnets to Clipboard?")
    TPB_clipboard_label.place(relx=.5, rely=.60, anchor="center")
    TPB_clipboard_combobox = ttk.Combobox(TPB_app, values=['Yes', 'No'])
    TPB_clipboard_combobox.place(relx=.5, rely=.70, anchor="center")

    TPB_domain_label.pack()
    TPB_domain_entry.pack()
    TPB_category_label.pack()
    TPB_category_entry.pack()
    TPB_clipboard_label.pack()
    TPB_clipboard_combobox.pack()

    TPB_ok_button = Button(TPB_app, text = "OK", command = TPB_callback)
    TPB_ok_button.place(relx=.5, rely=.91, anchor="center")

    TPB_app.title('TPB @eliasbenb')
    TPB_app.iconbitmap(r'icon.ico')
    TPB_app.geometry('500x225')
    TPB_app.mainloop()
