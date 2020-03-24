from tkinter import Button, Checkbutton, Entry, IntVar, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

search_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def search():
    def search_search_callback():
        def magnet_copy(event):
            search_choice = search_magnet_combobox.current()
            magnet_choice = search_magnets[search_choice-1]
            pyperclip.copy(magnet_choice)
            messagebox.showinfo("Search Scraper @eliasbenb", "The selected magnet link was successfully copied to the clipboard")
        search_query = search_query_entry.get()
        if ('selected' in search_tpb_domain_checkbutton.state()) and ('selected' in search_kat_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_kat_link = 'http://kat.rip/usearch/' + search_query
            try:
                search_kat_request = requests.get(search_kat_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something went wrong!")
            search_kat_source = search_kat_request.text
            search_kat_soup = BeautifulSoup(search_kat_source, 'lxml')
            kat_search_titles_all = search_kat_soup.findAll('a', class_="cellMainLink")
            for kat_title in kat_search_titles_all:
                if kat_title not in search_magnet_combobox['values']:
                    search_magnet_combobox['values'] += (kat_title.text,)
            search_kat_links = search_kat_soup.findAll('a', title="Torrent magnet link")
            search_magnets=[]
            for m in search_kat_links:
                search_magnets.append(m['href'])

            search_tpb_link = 'https://tpb.party/search/' + search_query + '/1/99/0/'
            try:
                search_tpb_request = requests.get(search_tpb_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            search_tpb_source = search_tpb_request.text
            search_tpb_soup = BeautifulSoup(search_tpb_source, 'lxml')
            tpb_search_titles_all = search_tpb_soup.findAll('div', class_="detName")
            for tpb_title in tpb_search_titles_all:
                if tpb_title not in search_magnet_combobox['values']:
                    search_magnet_combobox['values'] += (tpb_title.text,)
            search_tpb_links = search_tpb_soup.findAll('a', title="Download this torrent using magnet")
            for m in search_tpb_links:
                search_magnets.append(m['href'])

        elif 'selected' in search_kat_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_kat_link = 'http://kat.rip/usearch/' + search_query
            try:
                search_kat_request = requests.get(search_kat_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")
            search_kat_source = search_kat_request.text
            search_kat_soup = BeautifulSoup(search_kat_source, 'lxml')
            kat_search_titles_all = search_kat_soup.findAll('a', class_="cellMainLink")
            for kat_title in kat_search_titles_all:
                if kat_title not in search_magnet_combobox['values']:
                    search_magnet_combobox['values'] += (kat_title.text,)
            search_kat_links = search_kat_soup.findAll('a', title="Torrent magnet link")
            search_magnets=[]
            for m in search_kat_links:
                search_magnets.append(m['href'])

        elif 'selected' in search_tpb_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_tpb_link = 'https://tpb.party/search/' + search_query + '/1/99/0/'
            try:
                search_tpb_request = requests.get(search_tpb_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            search_tpb_source = search_tpb_request.text
            search_tpb_soup = BeautifulSoup(search_tpb_source, 'lxml')
            tpb_search_titles_all = search_tpb_soup.findAll('div', class_="detName")
            for tpb_title in tpb_search_titles_all:
                if tpb_title not in search_magnet_combobox['values']:
                    search_magnet_combobox['values'] += (tpb_title.text,)
            search_tpb_links = search_tpb_soup.findAll('a', title="Download this torrent using magnet")
            search_magnets=[]
            for m in search_tpb_links:
                search_magnets.append(m['href'])

        else:
            messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")

        search_magnet_combobox.bind("<<ComboboxSelected>>", magnet_copy)

    search_app = Tk()

    search_kat_domain_int = StringVar()
    search_kat_domain_checkbutton = ttk.Checkbutton(search_app, text="KAT", variable=search_kat_domain_int)
    search_kat_domain_checkbutton.place(relx=(2/5), rely=(1/20), anchor="center")
    search_kat_domain_checkbutton.state(['!disabled','selected'])
    search_tpb_domain_int = StringVar()
    search_tpb_domain_checkbutton = ttk.Checkbutton(search_app, text="TPB", variable=search_tpb_domain_int)
    search_tpb_domain_checkbutton.place(relx=(3/5), rely=(1/20), anchor="center")
    search_tpb_domain_checkbutton.state(['!disabled','selected'])

    search_query_string = StringVar()
    search_query_label = Label(search_app, text="Enter a Search Query:")
    search_query_label.place(relx=(1/2), rely=(3/20), anchor="center")
    search_query_entry = Entry(search_app, textvariable=search_query_string)
    search_query_entry.place(relx=(1/2), rely=(1/4), anchor="center", width=300)

    search_magnet_combobox = ttk.Combobox(search_app, values=['-- SELECT A MAGNET LINK TO COPY --'], state='readonly')
    search_magnet_combobox.place(relx=(1/2), rely=(2/5), anchor="center", width = 300)
    
    search_search_button = Button(search_app, text="Search", command=search_search_callback)
    search_search_button.place(relx=(1/2), rely=(9/10), anchor="center")

    search_app.title('Search @eliasbenb')
    search_app.iconbitmap(search_path+'\\icon.ico')
    search_app.geometry('400x300')
    search_app.resizable(False, False)
    
    search_app.mainloop()