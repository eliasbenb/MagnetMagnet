from tkinter import Tk, messagebox, StringVar, Label, Entry, Button, ttk
from imagebytes import *
from rarbg import *
from tpb import *

with open('icon.ico','wb') as f:
    f.write(icon_image_bytes)

app = Tk()
RARBG_button = Button(app, text="RARBG", font=("Segoe UI", 15, "bold"), command=rarbg)
RARBG_button.place(relx=0.75, rely=0.5, anchor="center", height=200, width=200)
TPB_button = Button(app, text="TPB", font=("Segoe UI", 15, "bold"), command=tpb)
TPB_button.place(relx=0.25, rely=0.5, anchor="center", height=200, width=200)

def on_closing():
    os.remove('icon.ico')
    app.destroy()
app.protocol("WM_DELETE_WINDOW", on_closing)

app.title('MagnetMagnet @eliasbenb')
app.iconbitmap(r'icon.ico')
app.geometry('400x200')
app.mainloop()
