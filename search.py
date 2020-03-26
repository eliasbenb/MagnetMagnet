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
        def search_kat():
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
            for m in search_kat_links:
                search_magnets.append(m['href'])
        
        def search_rarbg():
            search_rarbg_link = 'https://www.rarbgmirror.com/torrents.php?search=' + search_query
            try:
                search_rarbg_request = requests.get(search_rarbg_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            search_rarbg_source = search_rarbg_request.text
            search_rarbg_soup = BeautifulSoup(search_rarbg_source, 'lxml')
            for page_link in search_rarbg_soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                rarbg_page_link = 'https://www.rarbgmirror.com/' + page_link.get('href')
                try:
                    rarbg_page_request = requests.get(rarbg_page_link)
                except:
                    messagebox.showinfo("Search Scraper @eliasbenb", "Something went wrong!")

                rarbg_page_source = rarbg_page_request.content
                rarbg_page_soup = BeautifulSoup(rarbg_page_source, 'lxml')
                link = rarbg_page_soup.find('a', attrs={'href': re.compile("^magnet")})
                search_magnets.append(link.get('href'))
                rarbg_title = rarbg_page_soup.find('h1')
                search_magnet_combobox['values'] += (rarbg_title.text,)
        
        def search_tpb():
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
        def search_x1377():
            search_x1377_link = 'https://www.1377x.to/search/' + search_query + '/1/'
            try:
                search_x1377_request = requests.get(search_x1377_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            search_1377x_source = search_x1377_request.text
            search_1377x_soup = BeautifulSoup(search_1377x_source, 'lxml')
            for page_link in search_1377x_soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                x1377_page_link = 'https://www.1377x.to/' + page_link.get('href')
                try:
                    x1377_page_request = requests.get(x1377_page_link)
                except:
                    messagebox.showinfo("Search Scraper @eliasbenb", "Something went wrong!")

                x1377_page_source = x1377_page_request.content
                x1377_page_soup = BeautifulSoup(x1377_page_source, 'lxml')
                link = x1377_page_soup.find('a', attrs={'href': re.compile("^magnet")})
                search_magnets.append(link.get('href'))
                x1377_title = x1377_page_soup.find('h1')
                search_magnet_combobox['values'] += (x1377_title.text,)

        if ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_rarbg()
            search_tpb()
            search_x1377()            

        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_rarbg()
            search_tpb()
        
        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_rarbg()
            search_x1377()

        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_tpb()
            search_x1377()

        elif ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_rarbg()
            search_tpb()
            search_x1377()

        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_rarbg_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_rarbg()

        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_tpb()
        
        elif ('selected' in search_kat_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()
            search_x1377()
    
        elif ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_tpb_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_rarbg()
            search_tpb()

        elif ('selected' in search_rarbg_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_rarbg()
            search_x1377()

        elif ('selected' in search_tpb_domain_checkbutton.state()) and ('selected' in search_x1377_domain_checkbutton.state()):
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_tpb()
            search_x1377()

        elif 'selected' in search_kat_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_kat()

        elif 'selected' in search_rarbg_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_rarbg()

        elif 'selected' in search_tpb_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_tpb()

        elif 'selected' in search_x1377_domain_checkbutton.state():
            search_magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            search_magnets = []
            search_x1377()

        else:
            messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")

        search_magnet_combobox.bind("<<ComboboxSelected>>", magnet_copy)

    search_app = Tk()

    search_kat_domain_int = StringVar()
    search_kat_domain_checkbutton = ttk.Checkbutton(search_app, text="KAT", variable=search_kat_domain_int)
    search_kat_domain_checkbutton.place(relx=(1/5), rely=(1/20), anchor="center")
    search_kat_domain_checkbutton.state(['!disabled','selected'])
    search_rarbg_domain_int = StringVar()
    search_rarbg_domain_checkbutton = ttk.Checkbutton(search_app, text="RARBG", variable=search_rarbg_domain_int)
    search_rarbg_domain_checkbutton.place(relx=(2/5), rely=(1/20), anchor="center")
    search_rarbg_domain_checkbutton.state(['!disabled','selected'])
    search_tpb_domain_int = StringVar()
    search_tpb_domain_checkbutton = ttk.Checkbutton(search_app, text="TPB", variable=search_tpb_domain_int)
    search_tpb_domain_checkbutton.place(relx=(3/5), rely=(1/20), anchor="center")
    search_tpb_domain_checkbutton.state(['!disabled','selected'])
    search_x1377_domain_int = StringVar()
    search_x1377_domain_checkbutton = ttk.Checkbutton(search_app, text="1377x", variable=search_x1377_domain_int)
    search_x1377_domain_checkbutton.place(relx=(4/5), rely=(1/20), anchor="center")
    search_x1377_domain_checkbutton.state(['!disabled','selected'])

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