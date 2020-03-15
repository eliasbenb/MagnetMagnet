from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from imagebytes import *
from rarbg import *
from tpb import *
from kat import *
import os, tkinter.ttk

path = '%s\\eliasbenb\\' %  os.environ['APPDATA'] 
with open(path+'\icon.ico','wb') as f1:
    f1.write(icon_image_bytes)

app = Tk()
rarbg_button = Button(app, text="RARBG", font=("Segoe UI", 15, "bold"), command=rarbg)
rarbg_button.place(relx=0.166666666, rely=0.5, anchor="center", height=150, width=150)
tpb_button = Button(app, text="TPB", font=("Segoe UI", 15, "bold"), command=tpb)
tpb_button.place(relx=0.5, rely=0.5, anchor="center", height=150, width=150)
kat_button = Button(app, text="KAT", font=("Segoe UI", 15, "bold"), command=kat)
kat_button.place(relx=0.833333333, rely=0.5, anchor="center", height=150, width=150)

app.title('MagnetMagnet @eliasbenb')
app.iconbitmap(path+'icon.ico')
app.geometry('450x150')

app.mainloop()
