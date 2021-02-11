# Karina Ahrens - ID 001105641
# this code is where customer can browse catalogue, also there is buttons
# that will open a window to search products, search by catalogue, see reviews page and to open the shopping basket
from F2_Search_prod import *
from F2_Search_by_cat import *
from F3_Basket import *
from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from F2_Descriptions import batman, spider, shrek, dart, frozen, yoda, harry
from F2_Review import batman_rev, spider_rev, shrek_rev, dart_rev, frozen_rev, yoda_rev, harry_rev


# database
# connecting database for products
connects = sqlite3.connect('e-retail_admin.db')

# cursor
c = connects.cursor()


# function to create a new window with scrollbar
def products_list():
    root = Toplevel()
    root.title('All About Toys')
    # centralization
    # reference about the centralization of the window: https://youtu.be/gjU3Lx8XMS8
    width_window = 1000
    height_window = 800
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    x0 = (width / 2) - (width_window / 2)
    y0 = (height / 2) - (height_window / 2)
    root.geometry("%dx%d+%d+%d" % (width_window, height_window, x0, y0))

    # creating a scroll bar: code from : https://www.youtube.com/watch?v=0WafQCaok6g&t=11s&ab_channel=Codemy.com
    # creating main frame
    main_frame = Frame(root)
    main_frame.pack(fill=BOTH, expand=TRUE)

    # creating canvas
    my_canvas = Canvas(main_frame)
    my_canvas.pack(side=LEFT, fill=BOTH, expand=TRUE)

    # adding scrollbar to the canvas
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)

    # configure canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))

    # creating a new frame inside canvas
    frame = Frame(my_canvas)

    # add new frame to a windows in the canvas
    my_canvas.create_window((x0, y0), window=frame, anchor="nw")

    # ---------------------------------------------------------------------------------------------------------------#
    # Welcome to products label
    welcome = Label(frame, bg='white', font=('bold', 15), text="WELCOME TO AAT - ONLINE SHOPPING STORE")
    welcome.pack(pady=20)

    # function to open search products page
    def call_search():
        root_s = Tk()
        Search(master=root_s)

    # adding button to open window to search for products
    search_products_button = Button(frame, fg='darkblue', bg='darkgray', text="SEARCH PRODUCTS", command=call_search)
    search_products_button.pack(pady=20)

    def category_search():
        root_cat = Tk()
        SearchByCat(master=root_cat)

    # button to open search by category
    search_by_category = Button(frame, fg='darkblue', bg='darkgray', text="SEARCH BY CATEGORY", command=category_search)
    search_by_category.pack(pady=10)

    # query database batman
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=1")
    record = c.fetchone()
    # print(records)
    print_batman = ''
    if record:
        print_batman = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_batman)
    query_label.pack()

    # toy image
    batman_img = ImageTk.PhotoImage(Image.open("images/batman.png"))
    batman_label = Label(frame, image=batman_img)
    batman_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=1")
    stocks = c.fetchone()

    batman_stock = ''
    stock = ''
    if stock in stocks == 0:
        batman_stock += "Product availability: Out Of Stock"
    elif stock in stocks <= 20:
        batman_stock += "Product availability: Low stock"
    else:
        batman_stock += "Product available"

    stock_label = Label(frame, text=batman_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=batman)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=batman_rev)
    btn_review.pack(pady=(0, 20))

    # query database spider man
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=2")
    record = c.fetchone()
    # print(records)

    print_spider = ''

    if record:
        print_spider = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_spider)
    query_label.pack()

    # toy image
    spider_man_img = ImageTk.PhotoImage(Image.open('images/spider.jpg'))
    spider_man_label = Label(frame, image=spider_man_img)
    spider_man_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=2")
    stocks = c.fetchone()

    spider_stock = ''

    if stock in stocks == 0:
        spider_stock += "Product availability: Out Of Stock"
    elif stock in stocks <= 20:
        spider_stock += "Product availability: Low stock"
    else:
        spider_stock += "Product available"

    stock_label = Label(frame, text=spider_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=spider)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=spider_rev)
    btn_review.pack(pady=(0, 20))

    # query database shrek
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=3")
    record = c.fetchone()
    # print(records)

    print_shrek = ''

    if record:
        print_shrek = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_shrek)
    query_label.pack()

    # toy image
    shrek_img = ImageTk.PhotoImage(Image.open('images/Shrek.jpg'))
    shrek_label = Label(frame, image=shrek_img)
    shrek_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=3")
    stocks = c.fetchone()

    shrek_stock = ''

    for stock in stocks:
        if stock == 0:
            shrek_stock = "Product availability: Out Of Stock"
        elif stock < 20:
            shrek_stock = "Product availability: Low stock"
        else:
            shrek_stock = "Product available"

    stock_label = Label(frame, text=shrek_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=shrek)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=shrek_rev)
    btn_review.pack(pady=(0, 20))

    # query database dart
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=4")
    record = c.fetchone()
    # print(records)

    print_dart = ''

    if record:
        print_dart = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_dart)
    query_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=4")
    stocks = c.fetchone()

    dart_stock = ''
    for stock in stocks:
        if stock == 0:
            dart_stock = "Product availability: Out Of Stock"
        elif stock < 20:
            dart_stock = "Product availability: Low stock"
        else:
            dart_stock = "Product available"

    stock_label = Label(frame, text=dart_stock)
    stock_label.pack()

    # toy image
    darts_img = ImageTk.PhotoImage(Image.open('images/dart.jpg'))
    darts_label = Label(frame, image=darts_img)
    darts_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=dart)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=dart_rev)
    btn_review.pack(pady=(0, 20))

    # query database frozen
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=5")
    record = c.fetchone()
    # print(records)

    print_frozen = ''

    if record:
        print_frozen = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_frozen)
    query_label.pack()

    # toy image
    frozen_img = ImageTk.PhotoImage(Image.open('images/frozen.jpg'))
    frozen_label = Label(frame, image=frozen_img)
    frozen_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=5")
    stocks = c.fetchone()

    frozen_stock = ''
    for stock in stocks:
        if stock == 0:
            frozen_stock = "Product availability: Out Of Stock"
        elif stock < 20:
            frozen_stock = "Product availability: Low stock"
        else:
            frozen_stock = "Product available"

    stock_label = Label(frame, text=frozen_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=frozen)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=frozen_rev)
    btn_review.pack(pady=(0, 20))

    # query database yoda
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=6")
    record = c.fetchone()
    # print(records)

    print_yoda = ''

    if record:
        print_yoda = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_yoda)
    query_label.pack()

    # toy image
    yoda_img = ImageTk.PhotoImage(Image.open('images/yoda.jpg'))
    yoda_label = Label(frame, image=yoda_img)
    yoda_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=6")
    stocks = c.fetchone()

    yoda_stock = ''
    for stock in stocks:
        if stock == 0:
            yoda_stock = "Product availability: Out Of Stock"
        elif stock < 20:
            yoda_stock = "Product availability: Low stock"
        else:
            yoda_stock = "Product available"

    stock_label = Label(frame, text=yoda_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkred', bg='darkgray', command=yoda)
    btn_description.pack()

    # opens review window
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=yoda_rev)
    btn_review.pack(pady=(0, 20))

    # query database harry potter
    c.execute("SELECT prod_name, prod_cost FROM product WHERE id=7")
    record = c.fetchone()
    # print(records)

    print_harry = ''

    if record:
        print_harry = 'Name: ' + str(record[0]) + "\n" + 'Price: £' + str(record[1]) + "\n"

    query_label = Label(frame, font=('bold', 15), text=print_harry)
    query_label.pack()

    # toy image
    lego_img = ImageTk.PhotoImage(Image.open('images/hplego.jpg'))
    lego_label = Label(frame, image=lego_img)
    lego_label.pack()

    # here we use the stock information to display message about stock availability
    c.execute("SELECT prod_quantity FROM product WHERE id=7")
    stocks = c.fetchone()

    harry_stock = ''
    for stock in stocks:
        if stock == 0:
            harry_stock = "Product availability: Out Of Stock"
        elif stock < 20:
            harry_stock = "Product availability: Low stock"
        else:
            harry_stock = "Product available"

    stock_label = Label(frame, text=harry_stock)
    stock_label.pack()

    # opens shopping basket
    btn_buy = Button(frame, text='BUY', fg='black', bg='yellow', command=f3main)
    btn_buy.pack()

    # opens description window
    btn_description = Button(frame, text='Product Description', fg='darkblue', bg='darkgray', command=harry)
    btn_description.pack()

    # button to open review page
    btn_review = Button(frame, text="REVIEWS", fg='black', bg='cadet blue', command=harry_rev)
    btn_review.pack(pady=(0, 20))

    # button to exit page
    btn_2exit = Button(frame, text='Close Window', fg='darkred', bg='darkgray', command=frame.destroy)
    btn_2exit.pack()

    root.mainloop()
