# # David Buendia Soler - ID 001076459
from F3_basket_database import Database
import tkinter as tk

#Instanciate database class
db = Database()

#Create class for BasketWindow
class BasketW(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title("Your basket")
        master.geometry("700x700")
        self.create_widgets()

    #Create labels to display in GUI
    def create_widgets(self):
        self.product_id = tk.Label(self.master, text='Product Id', font=('bold', 12), pady=20)
        self.product_id.grid(row=0, column=0, sticky=tk.W)
        self.product_name = tk.Label(self.master, text='Product Name', font=('bold', 12), pady=20)
        self.product_name.grid(row=0, column=1, sticky=tk.W)
        self.product_price = tk.Label(self.master, text='Product Price', font=('bold', 12), pady=20)
        self.product_price.grid(row=0, column=2, sticky=tk.W)
        self.product_quantity = tk.Label(self.master, text='Product Quantity', font=('bold', 12), pady=20)
        self.product_quantity.grid(row=0, column=3, sticky=tk.W)


        #Calls variable connecting to the funcion "printBasket" in the Database class
        rows = db.printBasket()

        i = 0
        #Display values in ordenated rows and columns
        for item in rows:
            for j in range(len(item)):
                e = tk.Entry(self.master, width=20, fg="red")
                e.grid(row=i+2, column=j)
                e.insert(tk.END, item[j])

            i = i+1
        #Display total price
        for sum in db.getPrice():
            print(sum)

            self.getTotal_label = tk.Label(self.master, text=sum, font=("Helvetica", 20))
            self.getTotal_label.place(x=200, y=300)

            self.totalPrice_label = tk.Label(self.master, text="Total Price:  £", font=("Helvetica", 20))
            self.totalPrice_label.place(x=0, y=300)


