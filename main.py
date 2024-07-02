import pyperclip
import pyshorteners
from tkinter import *

roote = Tk()
roote.geometry("300x300")
roote.title("URL Shortener")
roote.configure(bg = "#000000")
url = StringVar()
url_addrerss = StringVar()

def urlshortener():
    urladress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladress)
    url_addrerss.set(url_short)

def copyurl():
    url_short = url_addrerss.get()
    pyperclip.copy(url_short)

Label(roote,text=" MY URL Shortener", font = "timesnewroman").pack(pady=10)
Entry(roote , textvariable = url).pack(pady=5)
Button(roote, text= " generate short url", command= urlshortener).pack(pady=7)
Entry(roote, textvariable= url_addrerss).pack(pady=5)
Button(roote,text = "copy URL",command= copyurl).pack(pady= 7)

roote.mainloop()