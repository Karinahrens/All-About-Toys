# David Buendia Soler - ID 001076459
from tkinter import *
import tkinter as tk
from tkinter import messagebox
from F3_basket_database import Database
from F3_BasketWindow import BasketW
import datetime

def f3main():
    #Instanciate different objects and variables
    bw = BasketW
    root = Tk()
    db = Database()
    t = Text(root)

    #Create a class for shopping basket
    class ShoppingBasket:

        def __init__(self, master, title, geometry):
            self.root = master
            self.root.title(title)
            self.root.geometry(geometry)

    w1 = ShoppingBasket(root, "Welcome to your Shopping Basket", "600x800")

    #Function to add a toy to your basket
    def add_toy():

        if toy_name.get() == "":
            messagebox.showerror("Please include all fields")
            return
        db.add(toy_name.get(), price.get(), quantity.get())

        toy_name.delete(0, END)
        price.delete(0, END)
        quantity.delete(0, END)


    #Function to add delivery details
    def add_delivery():

        #Insert in the database function inputs from text boxes
        db.delivery(customer_name.get(), full_address.get(), city.get(), postcode.get())

        #Clear text boxes
        full_address.delete(0, END)
        customer_name.delete(0, END)
        city.delete(0, END)
        postcode.delete(0, END)


    #Function to display your current basket after any additions
    def fetchBasket():
        root1 = tk.Tk()
        bw(master=root1)

    #Visa check simulator
    def add_payment():

        checkoutWindow = Toplevel()
        checkoutWindow.title("VisaCheck")
        checkoutWindow.geometry("500x500")


        full_name = Entry(checkoutWindow, width=30)
        full_name.grid(row=1, column=1)
        card = Entry(checkoutWindow, width=30)
        card.grid(row=5, column=1, padx=20, pady=(10, 0))
        sort_code = Entry(checkoutWindow, width=30)
        sort_code.grid(row=6, column=1)
        cvv = Entry(checkoutWindow, width=30)
        cvv.grid(row=7, column=1)



        full_name_label = Label(checkoutWindow, text="Full Name")
        full_name_label.grid(row=1, column=0)
        card_label = Label(checkoutWindow, text="Card Number")
        card_label.grid(row=5, column=0)
        sort_code_label = Label(checkoutWindow, text="Sort Code")
        sort_code_label.grid(row=6, column=0)
        cvv_label = Label(checkoutWindow, text="CVV")
        cvv_label.grid(row=7, column=0)
        title_checkout = Label(checkoutWindow, text="Please enter your card details", font=("Helvetica", 20))
        title_checkout.grid(row=0, column=1)


        #Displays total price
        for sum in db.getPrice():
            print(sum)



            getTotal_label = Label(checkoutWindow, text=sum, font=("Helvetica", 20))
            getTotal_label.place(x=200, y=300)

            totalPrice_label = Label(checkoutWindow, text="Total Price:  £", font=("Helvetica", 20))
            totalPrice_label.place(x=0, y=300)

        #Create button to call the function "receipt"
        place_order_btn = Button(checkoutWindow, text="Place Order", font=("Helvetica", 20), command=receipt)
        place_order_btn.place(x=200, y=400)


    #Function to delete toy of your current basket based on its id (displayed on the basket too)
    def delete():
        if toy_id.get() == "":
            messagebox.showerror("Please include all fields")
            return
        db.delete(toy_id.get())

        toy_id.delete(0, END)

    #Function to display all the information in GUI using similar widgets to basketWindow Class
    def receipt():
        receiptW = Toplevel()
        receiptW.geometry("600x600")
        receiptW.title("Receipt")
        messagebox.showinfo("VisaCheck", "Your details have been verified")

        header_label = Label(receiptW, text="Your order has been placed!", font=("Helvetica", 20))
        header_label.place(x=100, y=300)

        product_id = Label(receiptW, text='Product Id', font=('bold', 12), pady=20)
        product_id.grid(row=2, column=0, sticky=tk.W)
        product_name = Label(receiptW, text='Product Name', font=('bold', 12), pady=20)
        product_name.grid(row=2, column=1, sticky=tk.W)
        product_price = Label(receiptW, text='Product Price', font=('bold', 12), pady=20)
        product_price.grid(row=2, column=2, sticky=tk.W)
        product_quantity = Label(receiptW, text='Product Quantity', font=('bold', 12), pady=20)
        product_quantity.grid(row=2, column=3, sticky=tk.W)

        rows = db.printBasket()

        i = 2
        #Condition to display values in rows/columns
        for item in rows:
            for j in range(len(item)):
                e1 = Entry(receiptW, width=20, fg="red")
                e1.grid(row=i + 2, column=j)
                e1.insert(END, item[j])

            i = i + 1
        #Display total price
        for sum in db.getPrice():
            print(sum)


            getTotal_label = tk.Label(receiptW, text=sum, font=("Helvetica", 20))
            getTotal_label.place(x=200, y=500)

            totalPrice_label = tk.Label(receiptW, text="Total Price:  £", font=("Helvetica", 20))
            totalPrice_label.place(x=0, y=500)


        customer_name = Label(receiptW, text="Customer Name", font=('bold', 12), pady=20)
        customer_name.grid(row=10, column=0, sticky=tk.W)
        full_address = Label(receiptW, text='Full address', font=('bold', 12), pady=20)
        full_address.grid(row=10, column=1, sticky=tk.W)
        city = Label(receiptW, text='City', font=('bold', 12), pady=20)
        city.grid(row=10, column=2, sticky=tk.W)
        postcode = Label(receiptW, text='Postcode', font=('bold', 12), pady=20)
        postcode.grid(row=10, column=3, sticky=tk.W)

        detail = db.printDelivery()

        i = 10
        # Condition to display values in rows/columns
        for details in detail:
            for j in range(len(details)):
                e2 = Entry(receiptW, width=20, fg="green")
                e2.grid(row=i + 2, column=j)
                e2.insert(END, details[j])

            i = i + 1

        save_btn = Button(receiptW, text="Save receipt", font=("Helvetica", 15), command=save_receipt())
        save_btn.place(x=400, y=500)

    # Function to allow user to save receipt
    def save_receipt():

        # Display the date of the purchase
        Receipt_name = datetime.datetime.now()

        f = open(Receipt_name.strftime("%d %B %Y") + ".txt", 'w')
        f.write("Product _code Product_name Product_price Product_quantity\n")

        for download in db.printReceipt():
            f.write("{}\n".format(download))

        for sum in db.getPrice():
            f.write(("Total Price" + str(sum)))

        f.close()



    #Create text boxes
    toy_name = Entry(root, width=30)
    toy_name.place(x=100, y=75)
    price = Entry(root, width=30)
    price.place(x=100,y=120)
    quantity = Entry(root, width=30)
    quantity.place(x=100, y=155)
    customer_name = Entry(root, width=30)
    customer_name.place(x=100, y=360)
    full_address = Entry(root, width=30)
    full_address.place(x=100, y=390)
    city = Entry(root, width=30)
    city.place(x=100, y=420)
    postcode = Entry(root, width=30)
    postcode.place(x=100, y=450)
    toy_id = Entry(root, width=30)
    toy_id.place(x=140, y=240)


    #Create text box label
    delivery_details = Label(root, text="Please enter your delivery details", font=("Helvetica", 20))
    delivery_details.place(x=100, y=320)
    customer_name_label = Label(root, text="Full Name", font=("Helvetica", 13))
    customer_name_label.place(x=0, y=360)
    full_address_label = Label(root, text="Full address",font=("Helvetica", 13))
    full_address_label.place(x=0, y=390)
    city_label = Label(root, text="City",font=("Helvetica", 13))
    city_label.place(x=0, y=420)
    postcode_label = Label(root, text="Postcode",font=("Helvetica", 13))
    postcode_label.place(x=0, y=450)
    title_label = Label(root, text="Shopping basket", font=("Helvetica", 25))
    title_label.place(x=175, y=0)
    toy_name_label = Label(root, text="Toy name", font=("Helvetica", 13))
    toy_name_label.place(x=0, y=75)
    price_label = Label(root, text="Price",font=("Helvetica", 13))
    price_label.place(x=0, y=120)
    quantity_label = Label(root, text="Quantity",font=("Helvetica", 13))
    quantity_label.place(x=0, y=155)
    toy_id_label = Label(root, text="Select product ID ", font=("Helvetica", 13))
    toy_id_label.place(x=0, y=240)

    #Create buttons
    add_btn = Button(root, text="Add toy to your Basket",font=("Helvetica", 13), command=add_toy)
    add_btn.place(x=20, y=190)
    delete_btn = Button(root, text="Delete", font=("Helvetica", 13), command=delete)
    delete_btn.place(x=300, y=230)
    viewBasket_btn = Button(root, text="View your Basket", font=("Helvetica", 13), command=fetchBasket)
    viewBasket_btn.place(x=300, y=100)
    insert_delivery = Button(root, text="Add delivery details", font=("Helvetica", 15),
                             command=add_delivery)
    insert_delivery.place(x=150, y=550)

    checkout = Button(root, text="Proceed to checkout", font=("Helvetica", 20), command=add_payment)
    checkout.place(x=200, y=600)

    #Create RadioButton with the variable d
    d = StringVar()
    d.set(0)
    dcost = Radiobutton(root, text="Regular delivery 3-5 days (FREE)", value=0, variable=d)
    dcost.place(x=100, y=480)
    dcost1 = Radiobutton(root, text="Express delivery 1-2 days (5£)", value=5, variable=d)
    dcost1.place(x=100, y=510)


    #Close root loop
    root.mainloop()

