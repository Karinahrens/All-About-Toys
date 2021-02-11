# Musnath Ahamed - ID 001090034
# Import required libraries
import tkinter as tk
from tkinter import messagebox
from F1_admin_database import Database
# import os
import datetime

# Instantiate database object
db = Database()


# Function to implement home page of admin panel
def Home():

    root = tk.Tk()
    frame = tk.Frame(root)
    frame.pack()

    # Function to call categories class on click of Maintain Categories button
    def call_Categories():
        root.destroy()
        root_h = tk.Tk()
        Categories(master=root_h)

    # Function to call products class on click of Maintain Products button
    def call_Products():
        root.destroy()
        root_p = tk.Tk()
        Products(master=root_p)

    # Function to call stock class on click of Perform Stock Taking button
    def call_Stock():
        root.destroy()
        root_s = tk.Tk()
        Stock(master=root_s)


    # Buttons on home page that would allow user to select the options for admin panel
    main_label = tk.Label(frame, text="Select an Option", bg='old lace').pack()
    button_1 = tk.Button(frame, text="Maintain Categories", pady=5, padx=33, command=call_Categories, bg='snow3').pack()
    button_2 = tk.Button(frame, text="Maintain Products", pady=5, padx=38, command=call_Products, bg='snow3').pack()
    button_3 = tk.Button(frame, text="Perform Stock Taking", pady=5, padx=30, command=call_Stock, bg='snow3').pack()


# Class to implement categories functionality
class Categories(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Admin Panel')
        # Width height
        master.geometry("500x500")
        # Create widgets/grid
        self.create_widgets()
        # Init selected item var
        self.selected_item = 0
        # Populate initial lists
        self.populate_list()

    # Function to create category widgets
    def create_widgets(self):
        # Category Code
        self.code_text = tk.StringVar()
        self.code_label = tk.Label(self.master, text='Category Code', font=('bold', 12), pady=20)
        self.code_label.grid(row=0, column=0, sticky=tk.W)
        self.code_entry = tk.Entry(self.master, textvariable=self.code_text, bg='dark sea green')
        self.code_entry.grid(row=0, column=1)
        # Category Name
        self.name_text = tk.StringVar()
        self.cat_label = tk.Label(self.master, text='Category Name', font=('bold', 12))
        self.cat_label.grid(row=1, column=0, sticky=tk.W)
        self.cat_entry = tk.Entry(self.master, textvariable=self.name_text, bg='dark sea green')
        self.cat_entry.grid(row=1, column=1)

        # Category list (listbox)
        self.code_list = tk.Listbox(self.master, height=8, width=50, border=0, bg='powder blue')
        self.code_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.master)
        self.scrollbar.grid(row=3, column=3)
        self.code_list.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.configure(command=self.code_list.yview)

        # Bind select
        self.code_list.bind('<<ListboxSelect>>', self.select_item)

        # Buttons for category details
        self.add_btn = tk.Button(self.master, text="Add Category", width=15, command=self.add_item, bg='cadet blue')
        self.add_btn.grid(row=2, column=0, pady=20)

        self.remove_btn = tk.Button(self.master, text="Remove Category", width=15, command=self.remove_item, bg='cadet blue')
        self.remove_btn.grid(row=2, column=1, pady=20)

        self.update_btn = tk.Button(self.master, text="Update Category", width=15, command=self.update_item, bg='cadet blue')
        self.update_btn.grid(row=2, column=2, pady=20)

        self.exit_btn = tk.Button(self.master, text="Clear Input", width=15, command=self.clear_text, bg='cadet blue')
        self.exit_btn.grid(row=2, column=3, pady=20)

        self.back = tk.Button(self.master, text="Show menu", width=15, command=self.menu, bg='cadet blue')
        self.back.grid(row=9, column=0, pady=20)

    # Call this function on clicking Add Category button. Add new item in category
    def add_item(self):
        if self.code_text.get() == '' or self.name_text.get() == '':
            messagebox.showerror("Required Fields", "Please include all fields")
            return
        # Call insert function from database file. Insert into DB
        db.insert(self.code_text.get(), self.name_text.get())
        # Clear list
        self.code_list.delete(0, tk.END)
        # Insert into list
        self.code_list.insert(tk.END, (self.code_text.get(), self.name_text.get()))
        self.clear_text()
        self.populate_list()

    # Function to populate category list
    def populate_list(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.code_list.delete(0, tk.END)
        # Loop through records
        # Call fetch function form database file
        self.code_list.insert(tk.END, 'Id, Category_Code, Category_Name')
        for row in db.fetch():
            # Insert into list
            self.code_list.insert(tk.END, row)

    # Runs when item is selected in category list
    def select_item(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.code_list.curselection()[0]
            # Get selected item
            self.selected_item = self.code_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.code_entry.delete(0, tk.END)
            self.code_entry.insert(tk.END, self.selected_item[1])
            self.cat_entry.delete(0, tk.END)
            self.cat_entry.insert(tk.END, self.selected_item[2])
        except IndexError:
            pass

    # Remove item form category list
    def remove_item(self):
        # Call remove function from database file
        db.remove(self.selected_item[0])
        self.clear_text()
        self.populate_list()

    # Update item form category list
    def update_item(self):
        # Call update function from database file
        db.update(self.selected_item[0], self.code_text.get(), self.name_text.get())
        self.populate_list()

    # Clear all text fields form category entry widgets
    def clear_text(self):
        self.code_entry.delete(0, tk.END)
        self.cat_entry.delete(0, tk.END)

    # Function to implement show menu functionality
    def menu(self):
        self.master.destroy()
        Home()


# Class to implement products functionality
class Products(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Admin Panel')
        # Width height
        master.geometry("500x500")
        # Create widgets/grid
        self.create_widgets2()
        # Init selected item var
        self.selected_item = 0    
        # Populate initial lists
        self.populate_list2()

    # Function to create product widgets
    def create_widgets2(self):
        # Product Code
        self.prod_text = tk.StringVar()
        self.prod_label = tk.Label(self.master, text='Product Code', font=('bold', 12), pady=20)
        self.prod_label.grid(row=10, column=0, sticky=tk.W)
        self.prod_entry = tk.Entry(self.master, textvariable=self.prod_text, bg='PaleGreen3')
        self.prod_entry.grid(row=10, column=1)
        # Product Name
        self.prod_name = tk.StringVar()
        self.name_label = tk.Label(self.master, text='Product Name', font=('bold', 12), pady=10)
        self.name_label.grid(row=11, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(self.master, textvariable=self.prod_name, bg='PaleGreen3')
        self.name_entry.grid(row=11, column=1)
        # Product Description
        self.prod_desc = tk.StringVar()
        self.desc_label = tk.Label(self.master, text='Product Description', font=('bold', 12), pady=10)
        self.desc_label.grid(row=12, column=0, sticky=tk.W)
        self.desc_entry = tk.Entry(self.master, textvariable=self.prod_desc, bg='PaleGreen3')
        self.desc_entry.grid(row=12, column=1)
        # Product Cost
        self.prod_cost = tk.IntVar()
        self.cost_label = tk.Label(self.master, text='Product Cost', font=('bold', 12), pady=10)
        self.cost_label.grid(row=13, column=0, sticky=tk.W)
        self.cost_entry = tk.Entry(self.master, textvariable=self.prod_cost, bg='PaleGreen3')
        self.cost_entry.grid(row=13, column=1)
        # Product Quantity
        self.prod_quantity = tk.IntVar()
        self.quantity_label = tk.Label(self.master, text='Product Quantity', font=('bold', 12))
        self.quantity_label.grid(row=14, column=0, sticky=tk.W)
        self.quantity_entry = tk.Entry(self.master, textvariable=self.prod_quantity, bg='PaleGreen3')
        self.quantity_entry.grid(row=14, column=1)

        # Product list (listbox)
        self.prod_list = tk.Listbox(self.master, height=8, width=50, border=0, bg='powder blue')
        self.prod_list.grid(row=16, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar2 = tk.Scrollbar(self.master)
        self.scrollbar2.grid(row=16, column=3)
        self.prod_list.configure(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.configure(command=self.prod_list.yview)

        # Bind select
        self.prod_list.bind('<<ListboxSelect>>', self.select_item2)

        # Buttons for product details
        self.add_btn2 = tk.Button(self.master, text="Add Product", width=15, command=self.add_item2, bg='light sea green')
        self.add_btn2.grid(row=15, column=0, pady=20)

        self.remove_btn2 = tk.Button(self.master, text="Remove Product", width=15, command=self.remove_item2, bg='light sea green')
        self.remove_btn2.grid(row=15, column=1, pady=20)

        self.update_btn2 = tk.Button(self.master, text="Update Product", width=15, command=self.update_item2, bg='light sea green')
        self.update_btn2.grid(row=15, column=2, pady=20)

        self.exit_btn2 = tk.Button(self.master, text="Clear Input", width=15, command=self.clear_text2, bg='light sea green')
        self.exit_btn2.grid(row=15, column=3, pady=20)

        self.back2 = tk.Button(self.master, text="Show menu", width=15, command=self.menu, bg='cadet blue')
        self.back2.grid(row=24, column=0, pady=20)


    # Call this function on clicking Add product button. Add new item in product
    def add_item2(self):
        if self.prod_text.get() == '' or self.prod_name.get() == '' or self.prod_desc.get() == '' or self.prod_cost.get() == '' or self.prod_quantity.get() == '':
            messagebox.showerror("Required Fields", "Please include all fields")
            return
        # Call insert2 function from database file. Insert into DB
        db.insert2(self.prod_text.get(), self.prod_name.get(), self.prod_desc.get(), self.prod_cost.get(), self.prod_quantity.get())
        # Clear list
        self.prod_list.delete(0, tk.END)
        # Insert into list
        self.prod_list.insert(tk.END, (self.prod_text.get(), self.prod_name.get(), self.prod_desc.get(), self.prod_cost.get(), self.prod_quantity.get()))
        self.clear_text2()
        self.populate_list2()

    # Function to populate product list
    def populate_list2(self):
        # Delete items before update. So when you keep pressing it doesnt keep getting (show example by calling this twice)
        self.prod_list.delete(0, tk.END)
        # Loop through records
        # Call fetch2 function from database file
        self.prod_list.insert(tk.END, 'Id, Product_Id, Name, Description, Cost, Quantity')
        for row in db.fetch2():
            # Insert into list
            self.prod_list.insert(tk.END, row)

    # Remove item from product list
    def remove_item2(self):
        # Call remove2 function from database file
        db.remove2(self.selected_item[0])
        self.clear_text2()
        self.populate_list2()

    # Update item from product list
    def update_item2(self):
        # Call update2 function from database file
        db.update2(self.selected_item[0], self.prod_text.get(), self.prod_name.get(), self.prod_desc.get(), self.prod_cost.get(), self.prod_quantity.get())
        self.populate_list2()

    # Clear all text fields from product entry widgets
    def clear_text2(self):
        self.prod_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.cost_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    # Runs when item is selected product list
    def select_item2(self, event):
        # # Create global selected item to use in other functions
        # global self.selected_item
        try:
            # Get index
            index = self.prod_list.curselection()[0]
            # Get selected item
            self.selected_item = self.prod_list.get(index)
            # print(selected_item) # Print tuple

            # Add text to entries
            self.prod_entry.delete(0, tk.END)
            self.prod_entry.insert(tk.END, self.selected_item[1])
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, self.selected_item[2])
            self.desc_entry.delete(0, tk.END)
            self.desc_entry.insert(tk.END, self.selected_item[3])
            self.cost_entry.delete(0, tk.END)
            self.cost_entry.insert(tk.END, self.selected_item[4])
            self.quantity_entry.delete(0, tk.END)
            self.quantity_entry.insert(tk.END, self.selected_item[5])

        except IndexError:
            pass

    # Function to implement show menu functionality
    def menu(self):
        self.master.destroy()
        Home()


# Class t implement stock functionality
class Stock(tk.Frame):

    def __init__(self, master):
        super().__init__(master)
        self.master = master
        master.title('Admin Panel')
        # Width height
        master.geometry("500x500")
        # Create widgets/grid
        self.create_widgets3()
        # Init selected item var
        self.selected_item = 0    
        # Populate initial lists
        self.populate_list3()

    # Function to create Low stock widgets
    def create_widgets3(self):

        # Low Stock label
        self.stock_label = tk.Label(self.master, text='Low Stock', font=('bold', 14), pady=20, fg='red')
        self.stock_label.grid(row=0, column=11, sticky=tk.W)
        # Download Low Stock Data button
        self.download2 = tk.Button(self.master, text="Download Low Stock Data", width=25, command=self.download_data2, bg='forest green')
        self.download2.grid(row=1, column=11, pady=20)

        # Low stock list (listbox)
        self.stock_list = tk.Listbox(self.master, height=8, width=50, border=0, bg='powder blue')
        self.stock_list.grid(row=2, column=11, columnspan=3, rowspan=6, pady=20, padx=20)
        # Create scrollbar
        self.scrollbar2 = tk.Scrollbar(self.master)
        self.scrollbar2.grid(row=2, column=14)
        self.stock_list.configure(yscrollcommand=self.scrollbar2.set)
        self.scrollbar2.configure(command=self.stock_list.yview)   

        self.download = tk.Button(self.master, text="Download Product Data", width=20, command=self.download_data, bg='forest green')
        self.download.grid(row=9, column=11, pady=20)   

        self.back3 = tk.Button(self.master, text="Show menu", width=15, command=self.menu, bg='cadet blue')
        self.back3.grid(row=9, column=0, pady=20)

    # Function to call when Download Low Stock Data is clicked. Download low stock data in a file
    def download_data2(self):

        filename = datetime.datetime.now() 

        # Create a file to store stock details
        f = open(filename.strftime("%d %B %Y")+"_low_stock.txt", 'w')
        f.write('Product_Code  Product_Name  Product_Description  Product_Cost  Product_Quantity \n')
        # Call fetch3 function from database file
        for row in db.fetch3():
            f.write("{}\n".format(row))
        f.close()

    # Function to populate low stock list widget
    def populate_list3(self):

        self.stock_list.delete(0, tk.END)
        # Loop through records
        # Call fetch3 function from database file
        self.stock_list.insert(tk.END, 'Id, Product_Id, Name, Description, Cost, Quantity')
        for row in db.fetch3():
            # Insert into list
            self.stock_list.insert(tk.END, row)

    # Function runs when Download Product Data is clicked. Downloads product details
    def download_data(self):

        filename = datetime.datetime.now() 

        # Create a file to store product details
        f = open(filename.strftime("%d %B %Y")+".txt", 'w')
        f.write('Product_Code  Product_Name  Product_Description  Product_Cost  Product_Quantity\n')
        # Call fetch2 function from database file
        for row in db.fetch2():
            f.write("{}\n".format(row))
        f.close()

    # Function to implement show menu functionality
    def menu(self):
        self.master.destroy()
        Home()
