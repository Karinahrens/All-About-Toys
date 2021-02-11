# # David Buendia Soler - ID 001076459
import sqlite3

class Database:

    def __init__(self):

        #Connect to a database and create tables
        try:
            self.conn = sqlite3.connect("e-retail_admin.db")
            self.c = self.conn.cursor()

            self.c.execute("CREATE TABLE IF NOT EXISTS payment (id INTEGER PRIMARY KEY, toy_name text,"
                           "price integer, quantity integer)")
            self.c.execute("CREATE TABLE IF NOT EXISTS delivery (customer_name text, full_address text, city text, postcode text)")

            self.conn.commit()
        except:
            print("Failed")

#Functions for Basket

    #Add toy to the table
    def add(self, toy_name, price, quantity):
        self.c.execute('INSERT INTO payment VALUES (NULL, ?, ?, ?)', (toy_name, price, quantity))
        self.conn.commit()

    #Add delivery details to table
    def delivery(self, customer_name, full_address, city, postcode):
        self.c.execute("INSERT INTO delivery VALUES (?, ?, ?, ?)", (customer_name, full_address, city, postcode))
        self.conn.commit()

    #Calculate total price based on items chosen
    def getPrice(self):
        self.c.execute('SELECT SUM(price * quantity) FROM payment')
        sum = self.c.fetchall()
        return sum

    #Delete an item basedon its ID
    def delete(self, id):
        self.c.execute("DELETE FROM payment WHERE id = ?", (id,))
        self.conn.commit()


    #Print basket
    def printBasket(self):
        self.c.execute("SELECT id, toy_name, price, quantity FROM payment")
        toys = self.c.fetchall()
        return toys

    #Print delivery details
    def printDelivery(self):
        self.c.execute("SELECT * FROM delivery")
        delivery_details = self.c.fetchall()
        return delivery_details

    def printReceipt(self):
        self.c.execute("SELECT * FROM payment")
        download = self.c.fetchall()
        return download

    #Close connection
    def __del__(self):
        self.conn.close()





