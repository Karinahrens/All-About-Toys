# Karina Ahrens  001105641
# this code shows all integration between F1, F2 and F3
from F2_Search_prod import *
from F3_Basket import *
from F2_Search_by_cat import *
from tkinter import *
from F2_Toys import products_list
from F1_admin_index import Admin

# Opening Homepage
root = Tk()
root.title('All About Toys')
# centralization
# reference about the centralization of the window: https://youtu.be/gjU3Lx8XMS8
width_window = 500
height_window = 500
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
x0 = (width / 2) - (width_window / 2)
y0 = (height / 2) - (height_window / 2)
root.geometry("%dx%d+%d+%d" % (width_window, height_window, x0, y0))


# homepage class
class Home:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.welcome_label = Label(master, text="Welcome to ALL ABOUT TOYS", font=('bold', 15))
        self.welcome_label.pack()

        # adding button for member area
        self.staff_button = Button(master, fg='white', bg='cadet blue', font=('bold', 10),
                                   text="MEMBER AREA", command=self.admin_panel)
        self.staff_button.pack(pady=20)

        # our products list
        self.our_product = Button(master, fg='white', bg='cadet blue', font=('bold', 10),
                                  text='OUR PRODUCTS', command=self.products_list)
        self.our_product.pack(pady=20)

        # adding button to open window to search for products
        self.search_products_button = Button(master, fg='white', bg='cadet blue', font=('bold', 10),
                                             text="SEARCH PRODUCTS", command=self.call_search)
        self.search_products_button.pack(pady=20)

        # button to open search by category
        self.search_by_category = Button(master, fg='white', bg='cadet blue', font=('bold', 10),
                                         text="SEARCH BY CATEGORY", command=self.category_search)
        self.search_by_category.pack(pady=20)

        # button to open basket
        self.button_to_buy = Button(master, text='SHOPPING BASKET', fg='white', bg='cadet blue',
                                    font=('bold', 10), command=self.call_basket)
        self.button_to_buy.pack(pady=20)

        # button to exit window
        self.btn_2exit = Button(master, text='Close Window', fg='darkred', bg='darkgray', command=master.destroy)
        self.btn_2exit.pack()

    # static method is used because this functions are independent
    @staticmethod
    def admin_panel():
        root.destroy()
        Admin()

    @staticmethod
    def products_list():
        products_list()

    @staticmethod
    def category_search():
        root_cat = Tk()
        SearchByCat(master=root_cat)

    @staticmethod
    def call_search():
        root_s = Tk()
        Search(master=root_s)

    @staticmethod
    def call_basket():
        f3main()


h = Home(root)
root.mainloop()
