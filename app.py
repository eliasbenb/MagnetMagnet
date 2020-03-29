from tkinter import Button, Label, PhotoImage, Tk
from search import search
from kat import kat
from nyaa import nyaa
from rarbg import rarbg
from tpb import tpb
from x1377 import x1377
from imagebytes import *
import os, webbrowser

path = '%s\\eliasbenb' %  os.environ['APPDATA']
if not os.path.exists(path):
    os.makedirs(path)
with open(path+'\\icon.ico','wb') as w1:
    w1.write(icon_image_bytes)
with open(path+'\\website.png','wb') as w2:
    w2.write(website_image_bytes)
with open(path+'\\github.png','wb') as w3:
    w3.write(github_image_bytes)
with open(path+'\\eliasbenb.png','wb') as w4:
    w4.write(eliasbenb_image_bytes)

app = Tk()

website_photo = PhotoImage(file=path+"\\website.png")
github_photo = PhotoImage(file=path+"\\github.png")
eliasbenb_photo = PhotoImage(file=path+"\\eliasbenb.png")

def website_open():
    webbrowser.open('https://eliasbenb.github.io')
def github_open():
    webbrowser.open('https://github.com/eliasbenb/MagnetMagnet')

search_button = Button(app, text="Search", font=("Segoe UI", 15, "bold"), command=search)
search_button.place(relx=(0.5), rely=(75/275), anchor="s", height=75, width=750)

kat_button = Button(app, text="KAT", font=("Segoe UI", 15, "bold"), command=kat)
kat_button.place(relx=(1/10), rely=(225/275), anchor="s", height=150, width=150)

nyaa_button = Button(app, text="Nyaa", font=("Segoe UI", 15, "bold"), command=nyaa)
nyaa_button.place(relx=(3/10), rely=(225/275), anchor="s", height=150, width=150)

rarbg_button = Button(app, text="RARBG", font=("Segoe UI", 15, "bold"), command=rarbg)
rarbg_button.place(relx=(5/10), rely=(225/275), anchor="s", height=150, width=150)

tpb_button = Button(app, text="TPB", font=("Segoe UI", 15, "bold"), command=tpb)
tpb_button.place(relx=(7/10), rely=(225/275), anchor="s", height=150, width=150)

x1377_button = Button(app, text="1377x", font=("Segoe UI", 15, "bold"), command=x1377)
x1377_button.place(relx=(9/10), rely=(225/275), anchor="s", height=150, width=150)

website_button = Button(app, image=website_photo, command=website_open)
website_button.place(relx=(1/6), rely=1, anchor="s", height=50, width=32)
website_button["border"] = "0"

eliasbenb_label = Label(app, image=eliasbenb_photo)
eliasbenb_label.place(relx=(1/2), rely=1, anchor="s", height=50)

github_button = Button(app, image=github_photo, command=github_open)
github_button.place(relx=(5/6), rely=1, anchor="s", height=50, width=32)
github_button["border"] = "0"

app.title('MagnetMagnet @eliasbenb')
app.iconbitmap(path+'\\icon.ico')
app.geometry('750x275')
app.resizable(False, False)

app.mainloop()