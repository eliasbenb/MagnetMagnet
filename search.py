from tkinter import Button, Checkbutton, Entry, IntVar, Label, messagebox, StringVar, Tk, ttk
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

path = '%s\\eliasbenb' %  os.environ['APPDATA']

def search():
    def callback():
        def magnet_copy(event):
            choice = magnet_combobox.current()
            magnet_choice = magnets[choice-1]
            pyperclip.copy(magnet_choice)
            messagebox.showinfo("Search Scraper @eliasbenb", "The selected magnet link was successfully copied to the clipboard")
        query = query_entry.get()
        def kat():
            kat_link = 'http://kat.rip/usearch/' + query
            try:
                request = requests.get(kat_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            titles_all = soup.findAll('a', class_="cellMainLink")
            for title in titles_all:
                if title not in magnet_combobox['values']:
                    magnet_combobox['values'] += (title.text,)
            links = soup.findAll('a', title="Torrent magnet link")
            for m in links:
                magnets.append(m['href'])
        
        def rarbg():
            rarbg_link = 'https://torrentapi.org/pubapi_v2.php?mode=search&search_string=' + query + '&token=lnjzy73ucv&format=json_extended&app_id=lol'
            try:
                request = requests.get(rarbg_link, headers={'User-Agent': 'Mozilla/5.0'})
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")
            source = request.text
            soup = str(BeautifulSoup(source, 'lxml'))
            soup = soup.replace('<html><body><p>{"torrent_results":[', '')
            soup = soup.split(',')
            titles = str([i for i in soup if i.startswith('{"title":')])
            titles = titles.replace('{"title":"', '')
            titles = titles.replace('"', '')
            titles = titles.split("', '")
            titles[0] = titles[0].replace("['", "")
            for title in titles:
                magnet_combobox['values'] += (title,)
            links = str([i for i in soup if i.startswith('"download":')])
            links = links.replace('"download":"', '')
            links = links.replace('"', '')
            links = links.split("', '")
            for link in links:
                magnets.append(link)
        
        def tpb():
            tpb_link = 'https://tpb.party/search/' + query + '/1/99/0/'
            try:
                request = requests.get(tpb_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            titles_all = soup.findAll('div', class_="detName")
            for title in titles_all:
                if title not in magnet_combobox['values']:
                    magnet_combobox['values'] += (title.text,)
            links = soup.findAll('a', title="Download this torrent using magnet")
            for m in links:
                magnets.append(m['href'])
        def x1377():
            x1377_link = 'https://www.1377x.to/search/' + query + '/1/'
            try:
                request = requests.get(x1377_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")
            source = request.text
            soup = BeautifulSoup(source, 'lxml')
            for page_link in soup.findAll('a', attrs={'href': re.compile("^/torrent/")}):
                page_link = 'https://www.1377x.to/' + page_link.get('href')
                try:
                    page_request = requests.get(page_link)
                except:
                    messagebox.showinfo("Search Scraper @eliasbenb", "Something went wrong!")

                page_source = page_request.content
                page_soup = BeautifulSoup(page_source, 'lxml')
                link = page_soup.find('a', attrs={'href': re.compile("^magnet")})
                magnets.append(link.get('href'))
                title = page_soup.find('h1')
                magnet_combobox['values'] += (title.text,)

        if ('selected' in kat_domain_checkbutton.state()) and ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            rarbg()
            tpb()
            x1377()            

        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            rarbg()
            tpb()
        
        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            rarbg()
            x1377()

        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            tpb()
            x1377()

        elif ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            rarbg()
            tpb()
            x1377()

        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in rarbg_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            rarbg()

        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            tpb()
        
        elif ('selected' in kat_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()
            x1377()
    
        elif ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in tpb_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            rarbg()
            tpb()

        elif ('selected' in rarbg_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            rarbg()
            x1377()

        elif ('selected' in tpb_domain_checkbutton.state()) and ('selected' in x1377_domain_checkbutton.state()):
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            tpb()
            x1377()

        elif 'selected' in kat_domain_checkbutton.state():
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            kat()

        elif 'selected' in rarbg_domain_checkbutton.state():
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            rarbg()

        elif 'selected' in tpb_domain_checkbutton.state():
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            tpb()

        elif 'selected' in x1377_domain_checkbutton.state():
            magnet_combobox['values'] = ['-- SELECT A MAGNET LINK TO COPY --']
            magnets = []
            x1377()

        else:
            messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain, please kindly inform me on my GitHub.")

        magnet_combobox.bind("<<ComboboxSelected>>", magnet_copy)

    app = Tk()

    kat_domain_int = StringVar()
    kat_domain_checkbutton = ttk.Checkbutton(app, text="KAT", variable=kat_domain_int)
    kat_domain_checkbutton.place(relx=(1/5), rely=(1/20), anchor="center")
    kat_domain_checkbutton.state(['!disabled','selected'])
    rarbg_domain_int = StringVar()
    rarbg_domain_checkbutton = ttk.Checkbutton(app, text="RARBG", variable=rarbg_domain_int)
    rarbg_domain_checkbutton.place(relx=(2/5), rely=(1/20), anchor="center")
    rarbg_domain_checkbutton.state(['!disabled','selected'])
    tpb_domain_int = StringVar()
    tpb_domain_checkbutton = ttk.Checkbutton(app, text="TPB", variable=tpb_domain_int)
    tpb_domain_checkbutton.place(relx=(3/5), rely=(1/20), anchor="center")
    tpb_domain_checkbutton.state(['!disabled','selected'])
    x1377_domain_int = StringVar()
    x1377_domain_checkbutton = ttk.Checkbutton(app, text="1377x", variable=x1377_domain_int)
    x1377_domain_checkbutton.place(relx=(4/5), rely=(1/20), anchor="center")
    x1377_domain_checkbutton.state(['!disabled','selected'])

    query_string = StringVar()
    query_label = Label(app, text="Enter a Search Query:")
    query_label.place(relx=(1/2), rely=(3/20), anchor="center")
    query_entry = Entry(app, textvariable=query_string)
    query_entry.place(relx=(1/2), rely=(1/4), anchor="center", width=300)

    magnet_combobox = ttk.Combobox(app, values=['-- SELECT A MAGNET LINK TO COPY --'], state='readonly')
    magnet_combobox.place(relx=(1/2), rely=(2/5), anchor="center", width = 300)
    
    search_button = Button(app, text="Search", command=callback)
    search_button.place(relx=(1/2), rely=(9/10), anchor="center")

    app.title('Search @eliasbenb')
    app.iconbitmap(path+'\\icon.ico')
    app.geometry('400x300')
    app.resizable(False, False)
    
    app.mainloop()