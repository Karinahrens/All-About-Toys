# Karina Ahrens - ID 001105641
# this code opens a window where customer can write a review and display all reviews available
from tkinter import *
import sqlite3

con = sqlite3.connect("e-retail_admin.db")
c = con.cursor()


# function to display all info about batman reviews
def batman_rev():
    batman_window = Tk()
    batman_window.title('Batman Reviews')
    batman_window.geometry("800x800")
    # creating table
    '''
    c.execute("""CREATE TABLE IF NOT EXISTS batman_rev (
                          name text,
                          mail text,
                          review text
                          )""")
    '''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM batman_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(batman_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        data = "INSERT INTO batman_rev (name, mail, review) VALUES (?, ?,?)"
        values = (name.get(), mail.get(), review.get())

        # test not working
        test = c.fetchall()
        c.execute(data, values)
        if test == 0:
            "Missing information"
        else:
            pass

        con.commit()
        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()

    # write a review
    write_review = Label(batman_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(batman_window, text="Name: ")
    name_label.pack()
    name = Entry(batman_window)
    name.pack(ipadx=30)
    mail_label = Label(batman_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(batman_window)
    mail.pack(ipadx=30)
    review_label = Label(batman_window, text="Your Review: ")
    review_label.pack()
    review = Entry(batman_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(batman_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(batman_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    batman_window.mainloop()


# function to display all info about spider reviews
def spider_rev():
    spider_window = Tk()
    spider_window.title('Spider-Man Reviews')
    spider_window.geometry("800x500")
    '''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS spider_rev (
                          name text,
                          mail text,
                          review text
                          )""")
    '''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM spider_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(spider_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO spider_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()
        con.close()

    # write a review
    write_review = Label(spider_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(spider_window, text="Name: ")
    name_label.pack()
    name = Entry(spider_window)
    name.pack(ipadx=30)
    mail_label = Label(spider_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(spider_window)
    mail.pack(ipadx=30)
    review_label = Label(spider_window, text="Your Review: ")
    review_label.pack()
    review = Entry(spider_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(spider_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(spider_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    spider_window.mainloop()


# function to display all info about shrek reviews
def shrek_rev():
    shrek_window = Tk()
    shrek_window.title('Shrek Reviews')
    shrek_window.geometry("800x500")
    '''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS shrek_rev (
                          name text,
                          mail text,
                          review text
                          )""")'''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM shrek_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(shrek_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO shrek_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        con.commit()
        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()

    # write a review
    write_review = Label(shrek_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(shrek_window, text="Name: ")
    name_label.pack()
    name = Entry(shrek_window)
    name.pack(ipadx=30)
    mail_label = Label(shrek_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(shrek_window)
    mail.pack(ipadx=30)
    review_label = Label(shrek_window, text="Your Review: ")
    review_label.pack()
    review = Entry(shrek_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(shrek_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(shrek_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    shrek_window.mainloop()


# function to display all info about dart launcher reviews
def dart_rev():
    dart_window = Tk()
    dart_window.title('Dart Launcher Reviews')
    dart_window.geometry("800x500")
    '''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS dart_rev (
                          name text,
                          mail text,
                          review text
                          )""") '''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM dart_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(dart_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO dart_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        con.commit()
        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()

    # write a review
    write_review = Label(dart_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(dart_window, text="Name: ")
    name_label.pack()
    name = Entry(dart_window)
    name.pack(ipadx=30)
    mail_label = Label(dart_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(dart_window)
    mail.pack(ipadx=30)
    review_label = Label(dart_window, text="Your Review: ")
    review_label.pack()
    review = Entry(dart_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(dart_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(dart_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    dart_window.mainloop()


# function to display all info about frozen reviews
def frozen_rev():
    frozen_window = Tk()
    frozen_window.title('Frozen Reviews')
    frozen_window.geometry("800x500")
    ''''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS frozen_rev (
                          name text,
                          mail text,
                          review text
                          )""")'''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM frozen_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(frozen_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO frozen_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        con.commit()
        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()

    # write a review
    write_review = Label(frozen_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(frozen_window, text="Name: ")
    name_label.pack()
    name = Entry(frozen_window)
    name.pack(ipadx=30)
    mail_label = Label(frozen_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(frozen_window)
    mail.pack(ipadx=30)
    review_label = Label(frozen_window, text="Your Review: ")
    review_label.pack()
    review = Entry(frozen_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(frozen_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(frozen_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    frozen_window.mainloop()


# function to display all info about yoda reviews
def yoda_rev():
    yoda_window = Tk()
    yoda_window.title('Baby Yoda Reviews')
    yoda_window.geometry("800x500")
    '''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS yoda_rev (
                          name text,
                          mail text,
                          review text
                          )""")'''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM yoda_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(yoda_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO yoda_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()

    # write a review
    write_review = Label(yoda_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(yoda_window, text="Name: ")
    name_label.pack()
    name = Entry(yoda_window)
    name.pack(ipadx=30)
    mail_label = Label(yoda_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(yoda_window)
    mail.pack(ipadx=30)
    review_label = Label(yoda_window, text="Your Review: ")
    review_label.pack()
    review = Entry(yoda_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(yoda_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(yoda_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    yoda_window.mainloop()


# function to display all info about harry potter reviews
def harry_rev():
    harry_window = Tk()
    harry_window.title('Harry Potter Lego Reviews')
    harry_window.geometry("800x500")
    '''
    # creating table
    c.execute("""CREATE TABLE IF NOT EXISTS harry_rev (
                          name text,
                          mail text,
                          review text
                          )""")'''

    # function to display reviews and customer clicks on " see all reviews"
    def all_reviews():
        c.execute("SELECT name, review  FROM harry_rev")
        records = c.fetchall()
        # print(records)
        print_reviews = ''

        for record in records:
            print_reviews += str(record) + "\n"

        all_reviews_label = Label(harry_window, text=print_reviews)
        all_reviews_label.pack()

        con.commit()

    # function that will submit new review to the database
    def submit():
        c.execute("INSERT INTO harry_rev VALUES (:name,:mail, :review)",
                  {
                      'name': name.get(),
                      'mail': mail.get(),
                      'review': review.get()
                  })

        con.commit()
        # clear box
        name.delete(0, END)
        mail.delete(0, END)
        review.delete(0, END)

        con.commit()
        con.close()

    # write a review
    write_review = Label(harry_window, text="WRITE A REVIEW")
    write_review.pack()

    # creating text boxes, reference: https://www.youtube.com/watch?v=AK1J8xF4fuk&t=1486s&ab_channel=Codemy.com
    name_label = Label(harry_window, text="Name: ")
    name_label.pack()
    name = Entry(harry_window)
    name.pack(ipadx=30)
    mail_label = Label(harry_window, text="E-mail: ")
    mail_label.pack()
    mail = Entry(harry_window)
    mail.pack(ipadx=30)
    review_label = Label(harry_window, text="Your Review: ")
    review_label.pack()
    review = Entry(harry_window)
    review.pack(ipadx=50, ipady=100)

    # send review button
    send_btn = Button(harry_window, text="SEND YOUR REVIEW", command=submit)
    send_btn.pack()

    # see all reviews
    all_reviews = Button(harry_window, text="See all reviews", command=all_reviews)
    all_reviews.pack()

    harry_window.mainloop()
