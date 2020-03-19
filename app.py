from tkinter import Button, Label, PhotoImage, Tk
from imagebytes import *
from kat import kat
from rarbg import rarbg
from tpb import tpb
import os, webbrowser

path = '%s\\eliasbenb' %  os.environ['APPDATA']
if not os.path.exists(path):
    os.makedirs(path)
with open(path+'\\icon.ico','wb') as m1:
    m1.write(icon_image_bytes)
with open(path+'\\website.png','wb') as m2:
    m2.write(website_image_bytes)
with open(path+'\\github.png','wb') as m3:
    m3.write(github_image_bytes)
with open(path+'\\eliasbenb.png','wb') as m4:
    m4.write(eliasbenb_image_bytes)

app = Tk()

website_photo = PhotoImage(file=path+"\\website.png")
github_photo = PhotoImage(file=path+"\\github.png")
eliasbenb_photo = PhotoImage(file=path+"\\eliasbenb.png")

def website_open():
    webbrowser.open('https://eliasbenb.github.io')
def github_open():
    webbrowser.open('https://github.com/eliasbenb/MagnetMagnet')

kat_button = Button(app, text="KAT", font=("Segoe UI", 15, "bold"), command=kat)
kat_button.place(relx=(1/3), rely=0.381, anchor="e", height=150, width=150)
rarbg_button = Button(app, text="RARBG", font=("Segoe UI", 15, "bold"), command=rarbg)
rarbg_button.place(relx=0.5, rely=0.381, anchor="center", height=150, width=150)
tpb_button = Button(app, text="TPB", font=("Segoe UI", 15, "bold"), command=tpb)
tpb_button.place(relx=(2/3), rely=0.381, anchor="w", height=150, width=150)

eliasbenb_label = Label(app, image=eliasbenb_photo)
eliasbenb_label.place(relx=0.5, rely=0.8775, anchor="center", height=32)
website_button = Button(app, image=website_photo, command=website_open)
website_button.place(relx=0.16666666, rely=0.8775, anchor="center", height=32, width=32)
website_button["border"] = "0"
github_button = Button(app, image=github_photo, command=github_open)
github_button.place(relx=0.83333333, rely=0.8775, anchor="center", height=32, width=32)
github_button["border"] = "0"

app.title('MagnetMagnet @eliasbenb')
app.iconbitmap(path+'\\icon.ico')
app.geometry('450x200')

app.mainloop()
