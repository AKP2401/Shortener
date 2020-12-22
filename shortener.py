from tkinter import Button, Label
from tkinter import font
import pyshorteners
import tkinter
import pyperclip
url = ''
link = ''
shortener = pyshorteners.Shortener()
window = tkinter.Tk()
window.title("URL Shortener")
l1 = Label(window, text="Enter the url : ",font=("Arial Bold",10))
window.geometry('400x200')
l1.grid(column=0,row=5)
txt = tkinter.Entry(window,width=35)
txt.grid(column=1,row=5)
l3 = Label(window,text='',font=('Arial',10))
l3.grid(column=1,row=6)
def clicked1():
    url = txt.get()
    global link
    link=shortener.tinyurl.short(url)
    l3.configure(text=link)
bt = Button(window,text="Generate",command=clicked1)
bt.grid(column=2   ,row=5)
l2 = Label(window,text="Shortened URL : ",font=("Arial Bold",10))
l2.grid(column=0,row=6)
def clicked2():
    pyperclip.copy(link)
bt2 = Button(window,text='Copy',command=clicked2)
bt2.grid(column=2,row=6)
window.mainloop()
