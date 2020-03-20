from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

searcher_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def searcher():
    def searcher_callback():
        searcher_domain = searcher_domain_combobox.get()
        searcher_search = searcher_search_entry.get()

        if searcher_domain == 'Kick Ass Torrents':
            searcher_domain = 'https://kat.rip/'
            searcher_search = searcher_search.replace(' ', '%20')
            searcher_link = searcher_domain + 'usearch/' + searcher_search
        elif searcher_domain == 'RARBG':
            searcher_domain = 'https://rarbgmirror.com/'
            searcher_search = searcher_search.replace(' ', '+')
            searcher_link = searcher_domain + 'torrents.php?search=' + searcher_search
        elif searcher_domain == 'The Pirate Bay':
            searcher_domain = 'https://tpb.party/'
            searcher_search = searcher_search.replace(' ', '%20')
            searcher_link = searcher_domain + 'search/' + searcher_search + '/1/99/0'

        try:
            searcher_request = requests.get(searcher_link)
        except:
            messagebox.showinfo("Something is wrong with the website. It might be down, try again later.")

        searcher_source = searcher_request.content
        searcher_soup = BeautifulSoup(searcher_source, 'lxml')
        searcher_magnets = ['==== Made by @eliasbenb ====']
        for link in searcher_soup.findAll('a', attrs={'href': re.compile("^magnet")}):
            searcher_magnets.append('\n'+link.get('href'))
        searcher_magnets = list(dict.fromkeys(searcher_magnets))
        
        searcher_timestr = time.strftime(" %Y%m%d%H%M%S")
        searcher_file_name = "searcher Results " + searcher_timestr + ".txt"
        with open(searcher_file_name,'w') as searcher_w1:
            for magnet in searcher_magnets:
                searcher_w1.write(magnet)
        messagebox.showinfo("Searcher Scraper @eliasbenb", "Magnet links successfully exported to local directory")

    searcher_app = Tk()

    searcher_search_text = StringVar()
    searcher_search_label = Label(searcher_app, text="Enter a search: ")
    searcher_search_label.place(relx=0.5, rely=0.1, anchor="center")
    searcher_search_entry = Entry(searcher_app, textvariable=searcher_search_text)
    searcher_search_entry.place(relx=0.5, rely=0.2, anchor="center")    

    searcher_domain_label = Label(searcher_app, text="Choose a domain: ")
    searcher_domain_label.place(relx=0.5, rely=0.35, anchor="center")
    searcher_domain_combobox = ttk.Combobox(searcher_app, values=['Kick Ass Torrents', 'RARBG', 'The Pirate Bay'])
    searcher_domain_combobox.place(relx=0.5, rely=0.45, anchor="center")

    searcher_ok_button = Button(searcher_app, text = "OK", command = searcher_callback)
    searcher_ok_button.place(relx=0.5, rely=0.91, anchor="center")
    
    searcher_app.title('Searcher @eliasbenb')
    searcher_app.iconbitmap(searcher_path+'\\icon.ico')
    searcher_app.geometry('500x225')
    
    searcher_app.mainloop()