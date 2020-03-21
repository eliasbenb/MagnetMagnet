from tkinter import Button, Entry, Label, messagebox, StringVar, Tk, ttk, Checkbutton, IntVar, BooleanVar
import os, pyperclip, requests, re, tkinter.ttk, time
from bs4 import BeautifulSoup

search_path = '%s\\eliasbenb' %  os.environ['APPDATA']

def search():
    def search_kat():
        search_app.geometry('400x300')
        search_kat_checkbutton.destroy()
        search_tpb_checkbutton.destroy()
        def search_search_callback():
            def search_ok_callback_2():
                search_choice = search_combobox.current()
                magnet_choice = search_magnets[search_choice-1]
                pyperclip.copy(magnet_choice)
                messagebox.showinfo("Search Scraper @eliasbenb", "The selected magnet link was successfully copied to the clipboard")

            search_search_button.destroy()
            search_query = search_query_entry.get()
            search_query = search_query.replace(' ', '%20')
            search_link = 'http://kat.rip/usearch/' + search_query
            try:
                search_request = requests.get(search_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")
            
            search_source = search_request.text
            search_soup = BeautifulSoup(search_source, 'lxml')

            search_combobox = ttk.Combobox(search_app, values=['-- SELECT A MAGNET LINK TO COPY --'])
            search_titles_all = search_soup.findAll('a', class_="cellMainLink")
            for title in search_titles_all:
                if title not in search_combobox['values']:
                    search_combobox['values'] += (title.text,)

            search_links = search_soup.findAll('a', title="Torrent magnet link")
            search_magnets=[]
            for m in search_links:
                search_magnets.append(m['href'])

            search_combobox.place(relx=0.5, rely=0.3, anchor="center", width = 300)

            search_ok_button_2 = Button(search_app, text = "OK", command = search_ok_callback_2)
            search_ok_button_2.place(relx=0.5, rely=0.91, anchor="center")

        search_query_text = StringVar()
        search_query_label = Label(search_app, text="Enter Query:")
        search_query_label.place(relx=0.5, rely=0.10, anchor="center")
        search_query_entry = Entry(search_app, textvariable=search_query_text)
        search_query_entry.place(relx=0.5, rely=0.20, anchor="center")

        search_search_button = Button(search_app, text = "Search", command = search_search_callback)
        search_search_button.place(relx=0.5, rely=0.91, anchor="center")
    
    def search_tpb():
        search_app.geometry('400x300')
        search_kat_checkbutton.destroy()
        search_tpb_checkbutton.destroy()
        def search_search_callback():
            def search_ok_callback_2():
                search_choice = search_combobox.current()
                magnet_choice = search_magnets[search_choice-1]
                pyperclip.copy(magnet_choice)
                messagebox.showinfo("Search Scraper @eliasbenb", "The selected magnet link was successfully copied to the clipboard")

            search_search_button.destroy()
            search_query = search_query_entry.get()
            search_query = search_query.replace(' ', '%20')
            search_link = 'https://tpb.party/search/' + search_query + '/1/99/0/'
            try:
                search_request = requests.get(search_link)
            except:
                messagebox.showinfo("Search Scraper @eliasbenb", "Something is wrong with the domain/category you inputed.\nMake sure that the domain ends with trailing '/'")
            
            search_source = search_request.text
            search_soup = BeautifulSoup(search_source, 'lxml')

            search_combobox = ttk.Combobox(search_app, values=['-- SELECT A MAGNET LINK TO COPY --'])
            search_titles_all = search_soup.findAll('div', class_="detName")
            for title in search_titles_all:
                if title not in search_combobox['values']:
                    search_combobox['values'] += (title.text,)

            search_links = search_soup.findAll('a', title="Download this torrent using magnet")
            search_magnets=[]
            for m in search_links:
                search_magnets.append(m['href'])

            search_combobox.place(relx=0.5, rely=0.3, anchor="center", width = 300)

            search_ok_button_2 = Button(search_app, text = "OK", command = search_ok_callback_2)
            search_ok_button_2.place(relx=0.5, rely=0.91, anchor="center")

        search_query_text = StringVar()
        search_query_label = Label(search_app, text="Enter Query:")
        search_query_label.place(relx=0.5, rely=0.10, anchor="center")
        search_query_entry = Entry(search_app, textvariable=search_query_text)
        search_query_entry.place(relx=0.5, rely=0.20, anchor="center")

        search_search_button = Button(search_app, text = "Search", command = search_search_callback)
        search_search_button.place(relx=0.5, rely=0.91, anchor="center")
        
    search_app = Tk()

    search_kat_var = BooleanVar()
    search_tpb_var = BooleanVar()

    search_kat_checkbutton = Checkbutton(search_app, text="KAT", variable=search_kat_var, command=search_kat)
    search_kat_checkbutton.place(relx=0.3, rely=0.5, anchor="center")
    search_tpb_checkbutton = Checkbutton(search_app, text="TPB", variable=search_tpb_var, command=search_tpb)
    search_tpb_checkbutton.place(relx=0.7, rely=0.5, anchor="center")


    search_app.title('search @eliasbenb')
    search_app.iconbitmap(search_path+'\\icon.ico')
    search_app.geometry('250x100')
    
    search_app.mainloop()