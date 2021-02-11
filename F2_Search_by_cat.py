# Karina Ahrens - ID 001105641
# this code display a page to search products by category
from tkinter import *
from tkinter import ttk
import sqlite3

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


class SearchByCat(Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        master.title("Search Products by Category")
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
        self.search_label = Label(self.master, text="Search by Category: ")
        self.search_label.pack()

        # Entry box Label to search products
        self.search_label = Label(self.master, text="All Products by Category: ")
        self.search_label.pack()

        # Drop down box
        self.drop = ttk.Combobox(self.master, value=["Choose Category", "Action Figure", "Doll", "Lego", "Launchers"])
        self.drop.current(0)
        self.drop.pack()

        # Entry box Button to search products
        self.search_button = Button(self.master, text="Search", command=self.searching_category)
        self.search_button.pack()

        # button to close window
        self.btn_2exit = Button(self.master, text='Close Window', fg='darkred', bg='darkgray', command=master.destroy)
        self.btn_2exit.pack()

    # function to display a dropbox with all the categories available
    def searching_category(self):
        selec = self.drop.get()
        if selec == "Choose Category":
            test = Label(self.master, text="Choose and click search")
            test.pack()
        if selec == "Action Figure":
            c.execute("SELECT * FROM products WHERE category = 'Action Figure'")
            category_data = c.fetchall()
            test = Label(self.master, text=category_data)
            test.pack()
        if selec == "Doll":
            c.execute("SELECT * FROM products WHERE category = 'Doll' ")
            category_data = c.fetchall()
            test = Label(self.master, text=category_data)
            test.pack()
        if selec == "Lego":
            c.execute("SELECT * FROM products WHERE category = 'Lego' ")
            category_data = c.fetchall()
            test = Label(self.master, text=category_data)
            test.pack()
        if selec == "Launchers":
            c.execute("SELECT * FROM products WHERE category = 'Launchers' ")
            category_data = c.fetchall()
            test = Label(self.master, text=category_data)
            test.pack()

        searched_label = Label(self.master, text=selec)
        searched_label.pack()

        con.commit()
        mainloop()
