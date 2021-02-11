# Karina Ahrens - ID 001105641
from tkinter import *
from tkinter import ttk
import sqlite3

# search function, reference https://www.youtube.com/watch?v=fXotGRP6x4E&t=827s&ab_channel=Codemy.com,
# https://www.youtube.com/watch?v=fXotGRP6x4E&ab_channel=Codemy.com


con = sqlite3.connect("e-retail_admin.db")
c = con.cursor()
# creating table
c.execute("""CREATE TABLE IF NOT EXISTS products (
                 id integer PRIMARY KEY,
                 name text,
                 price integer,
                 category text,
                 description text,
                 stock integer )""")


class Search(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        master.title("Search Products")
        # centralization
        # reference about the centralization of the window: https://youtu.be/gjU3Lx8XMS8
        width_window = 500
        height_window = 500
        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()
        x0 = (width / 2) - (width_window / 2)
        y0 = (height / 2) - (height_window / 2)
        master.geometry("%dx%d+%d+%d" % (width_window, height_window, x0, y0))

        # Entry box Label to search products
        self.search_label = Label(self.master, text="Search products: ")
        self.search_label.pack()

        # Drop down box
        self.drop = ttk.Combobox(self.master, value=["Product Name", "Price", "Category"])
        self.drop.current(0)
        self.drop.pack()

        # Entry box to search products
        self.search_box = Entry(self.master)
        self.search_box.pack()

        # Entry box Button to search products
        self.search_button = Button(self.master, text="Search", command=self.searching)
        self.search_button.pack()

        self.btn_2exit = Button(self.master, text='Close Window', fg='darkred', bg='darkgray', command=master.destroy)
        self.btn_2exit.pack()

    def searching(self):
        selected = self.drop.get()
        sql = ""
        if selected == "Product Name":
            sql = "SELECT name, price, category, description FROM products WHERE name=? COLLATE NOCASE"

        if selected == "Price":
            sql = "SELECT name, price, category, description FROM products WHERE price=?"

        if selected == "Category":
            sql = "SELECT name, price, category, description FROM products WHERE category=? COLLATE NOCASE"

        searched = self.search_box.get()
        # sql = "SELECT * FROM products WHERE name= ? "
        name = (searched, )
        result = c.execute(sql, name)

        result = c.fetchall()

        if not result:
            result = " Product not found"

        searched_label = Label(self.master, text=result)
        searched_label.pack()

        self.master.mainloop()
