# Musnath Ahamed - ID 001090034
# Import required libraries
import sqlite3


# Class to initialize database
class Database:

    def __init__(self):

        # Establish connection with admin database and create required tables
        try:
            self.conn = sqlite3.connect("e-retail_admin.db")
            self.curr = self.conn.cursor()
            self.curr.execute("CREATE TABLE IF NOT EXISTS category (id INTEGER PRIMARY KEY, code text, cat_name text)")
            self.curr.execute("CREATE TABLE IF NOT EXISTS product (id INTEGER PRIMARY KEY, code text, prod_name text, "
                              "prod_desc text, prod_cost int, prod_quantity int)")
            self.conn.commit()
        except:
            print("Failed")

    # Functions for admin Category
    def fetch(self):
        self.curr.execute("SELECT * FROM category")
        rows = self.curr.fetchall()
        return rows

    def insert(self, code, cat_name):
        self.curr.execute("INSERT INTO category VALUES (NULL, ?, ?)", (code, cat_name))
        self.conn.commit()

    def remove(self, id):
        self.curr.execute("DELETE FROM category WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, code, cat_name):
        self.curr.execute("UPDATE category SET code = ?, cat_name = ? WHERE id = ?", (code, cat_name, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    # Functions for admin Product
    def fetch2(self):
        self.curr.execute("SELECT * FROM product")
        rows = self.curr.fetchall()
        return rows

    def insert2(self, code, prod_name, prod_decs, prod_cost, prod_quantity):
        self.curr.execute("INSERT INTO product VALUES (NULL, ?, ?,?,?,?)",
                          (code, prod_name, prod_decs, prod_cost, prod_quantity))
        self.conn.commit()

    def remove2(self, id):
        self.curr.execute("DELETE FROM product WHERE id=?", (id,))
        self.conn.commit()

    def update2(self, id, code, prod_name, prod_decs, prod_cost, prod_quantity):
        self.curr.execute(
            "UPDATE product SET code = ?, prod_name = ?, prod_desc = ?, prod_cost = ?, prod_quantity = ? WHERE id = ?",
            (code, prod_name, prod_decs, prod_cost, prod_quantity, id))
        self.conn.commit()

    # Function for low stock
    def fetch3(self):
        self.curr.execute("SELECT * FROM product where prod_quantity < 20")
        rows = self.curr.fetchall()
        return rows
