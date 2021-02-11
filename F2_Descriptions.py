# Karina Ahrens - ID 001105641

# this code represents the descriptions window of the toys.
from tkinter import *
import sqlite3

con = sqlite3.connect("e-retail_admin.db")
c = con.cursor()


def batman():
    batman_window = Tk()
    batman_window.title('Batman Description')
    batman_window.geometry("500x500")

    c.execute("SELECT prod_desc FROM product WHERE id=1")
    records = c.fetchone()
    # print(records)

    batman_description = Label(batman_window, text="Batman toy description:")
    batman_description.pack()
    batman_description = Label(batman_window, text=records)
    batman_description.pack()
    btn_2exit = Button(batman_window, text='Close Window', fg='darkred', bg='darkgray', command=batman_window.destroy)
    btn_2exit.pack()
    batman_window.mainloop()

    con.commit()


def spider():
    spiders_window = Tk()
    spiders_window.title('Spider Description')
    spiders_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=2 ")
    records = c.fetchone()

    spider_description = Label(spiders_window, text="Spider-Man toy description:")
    spider_description.pack()
    spider_description = Label(spiders_window, text=records)
    spider_description.pack()
    btn_2exit = Button(spiders_window, text='Close Window', fg='darkred', bg='darkgray', command=spiders_window.destroy)
    btn_2exit.pack()
    spiders_window.mainloop()

    con.commit()


def shrek():
    shrek_window = Tk()
    shrek_window.title('Shrek Description')
    shrek_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=3 ")
    records = c.fetchone()

    shrek_description = Label(shrek_window, text="Shrek Description:")
    shrek_description.pack()
    shrek_description = Label(shrek_window, text=records)
    shrek_description.pack()
    btn_2exit = Button(shrek_window, text='Close Window', fg='darkred', bg='darkgray', command=shrek_window.destroy)
    btn_2exit.pack()
    shrek_window.mainloop()

    con.commit()


def dart():
    dart_window = Tk()
    dart_window.title('Dart Launcher Description')
    dart_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=4 ")
    records = c.fetchone()

    dart_description = Label(dart_window, text="Dart Launcher Description:")
    dart_description.pack()
    dart_description = Label(dart_window, text=records)
    dart_description.pack()
    btn_2exit = Button(dart_window, text='Close Window', fg='darkred', bg='darkgray', command=dart_window.destroy)
    btn_2exit.pack()
    dart_window.mainloop()

    con.commit()


def frozen():
    frozen_window = Tk()
    frozen_window.title('Frozen Description')
    frozen_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=5 ")
    records = c.fetchone()

    frozen_description = Label(frozen_window, text="Frozen Description:")
    frozen_description.pack()
    frozen_description = Label(frozen_window, text=records)
    frozen_description.pack()
    btn_2exit = Button(frozen_window, text='Close Window', fg='darkred', bg='darkgray', command=frozen_window.destroy)
    btn_2exit.pack()
    frozen_window.mainloop()

    con.commit()


def yoda():
    yoda_window = Tk()
    yoda_window.title('Baby Yoda Description')
    yoda_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=6 ")
    records = c.fetchone()

    yoda_description = Label(yoda_window, text="Baby Yoda Description:")
    yoda_description.pack()
    yoda_description = Label(yoda_window, text=records)
    yoda_description.pack()
    btn_2exit = Button(yoda_window, text='Close Window', fg='darkred', bg='darkgray', command=yoda_window.destroy)
    btn_2exit.pack()
    yoda_window.mainloop()

    con.commit()


def harry():
    harry_window = Tk()
    harry_window.title('Harry Potter Description')
    harry_window.geometry("500x500")
    c.execute("SELECT prod_desc FROM product WHERE id=7 ")
    records = c.fetchone()

    harry_description = Label(harry_window, text="Harry Potter - Lego Description:")
    harry_description.pack()
    harry_description = Label(harry_window, text=records)
    harry_description.pack()
    btn_2exit = Button(harry_window, text='Close Window', fg='darkred', bg='darkgray', command=harry_window.destroy)
    btn_2exit.pack()
    harry_window.mainloop()

    con.commit()
