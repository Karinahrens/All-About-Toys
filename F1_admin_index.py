# Musnath Ahamed - ID 001090034
# Import required libraries
from tkinter import *
# import tkinter as tk
import tkinter.messagebox as tkMessageBox
import sqlite3
from F1_admin_homepage import Home


# Define admin function to call in main page
def Admin():
    # Admin provides login and registration functionality for admin

    root = Tk()
    root.title("Admin Login")
    
    # Set window size
    width = 640
    height = 480
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry("%dx%d+%d+%d" % (width, height, x, y))
    root.resizable(0, 0)

    # Function to create and connect to database for admin
    def Database():

        global conn, cursor
        conn = sqlite3.connect("e-retail_admin.db")
        cursor = conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS `admin_member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                       "username TEXT, password TEXT, firstname TEXT, lastname TEXT)")

    # Initialize input variables for admin login and registration
    USERNAME = StringVar()
    PASSWORD = StringVar()
    FIRSTNAME = StringVar()
    LASTNAME = StringVar()

    # Function to provide login functionality
    def LoginForm():

        global LoginFrame, lbl_result1
        LoginFrame = Frame(root)
        LoginFrame.pack(side=TOP, pady=80)
        lbl_username = Label(LoginFrame, text="Username:", font=('arial', 25), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(LoginFrame, text="Password:", font=('arial', 25), bd=18)
        lbl_password.grid(row=2)
        lbl_result1 = Label(LoginFrame, text="", font=('arial', 18))
        lbl_result1.grid(row=3, columnspan=2)
        username = Entry(LoginFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(LoginFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        btn_login = Button(LoginFrame, text="Login", font=('arial', 18), width=35, command=Login, bg='Indian red')
        btn_login.grid(row=4, columnspan=2, pady=20)
        lbl_register = Label(LoginFrame, text="Register", fg="Blue", font=('arial', 12))
        lbl_register.grid(row=0, sticky=W)
        lbl_register.bind('<Button-1>', ToggleToRegister)
    
    # Function to provide registration functionality
    def RegisterForm():
        
        global RegisterFrame, lbl_result2
        RegisterFrame = Frame(root)
        RegisterFrame.pack(side=TOP, pady=40)
        lbl_username = Label(RegisterFrame, text="Username:", font=('arial', 18), bd=18)
        lbl_username.grid(row=1)
        lbl_password = Label(RegisterFrame, text="Password:", font=('arial', 18), bd=18)
        lbl_password.grid(row=2)
        lbl_firstname = Label(RegisterFrame, text="First Name:", font=('arial', 18), bd=18)
        lbl_firstname.grid(row=3)
        lbl_lastname = Label(RegisterFrame, text="Last Name:", font=('arial', 18), bd=18)
        lbl_lastname.grid(row=4)
        lbl_result2 = Label(RegisterFrame, text="", font=('arial', 18))
        lbl_result2.grid(row=5, columnspan=2)
        username = Entry(RegisterFrame, font=('arial', 20), textvariable=USERNAME, width=15)
        username.grid(row=1, column=1)
        password = Entry(RegisterFrame, font=('arial', 20), textvariable=PASSWORD, width=15, show="*")
        password.grid(row=2, column=1)
        firstname = Entry(RegisterFrame, font=('arial', 20), textvariable=FIRSTNAME, width=15)
        firstname.grid(row=3, column=1)
        lastname = Entry(RegisterFrame, font=('arial', 20), textvariable=LASTNAME, width=15)
        lastname.grid(row=4, column=1)
        btn_login = Button(RegisterFrame, text="Register", font=('arial', 18), width=35, command=Register, bg='Indian '
                                                                                                              'red')
        btn_login.grid(row=6, columnspan=2, pady=20)
        lbl_login = Label(RegisterFrame, text="Login", fg="Blue", font=('arial', 12))
        lbl_login.grid(row=0, sticky=W)
        lbl_login.bind('<Button-1>', ToggleToLogin)
    
    # Function to implement exit functionality on top bar in window
    def Exit():
        result = tkMessageBox.askquestion('System', 'Are you sure you want to exit?', icon="warning")
        if result == 'yes':
            root.destroy()
            exit()

    # ========================================MENU BAR WIDGETS==================================
    menubar = Menu(root)
    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="Exit", command=Exit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)

    # Function to toggle to login frame after clicking Login button
    def ToggleToLogin(event=None):
        RegisterFrame.destroy()
        LoginForm()
    
    # Function to toggle to register frame after clicking Register button
    def ToggleToRegister(event=None):
        LoginFrame.destroy()
        RegisterForm()
    
    # Function to store registration details in admin database
    def Register():

        Database()
        if USERNAME.get == "" or PASSWORD.get() == "" or FIRSTNAME.get() == "" or LASTNAME.get == "":
            lbl_result2.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `admin_member` WHERE `username` = ?", (USERNAME.get(),))
            if cursor.fetchone() is not None:
                lbl_result2.config(text="Username is already taken", fg="red")
            else:
                cursor.execute("INSERT INTO `admin_member` (username, password, firstname, lastname) VALUES(?, ?, ?, ?)", (str(USERNAME.get()), str(PASSWORD.get()), str(FIRSTNAME.get()), str(LASTNAME.get())))
                conn.commit()
                USERNAME.set("")
                PASSWORD.set("")
                FIRSTNAME.set("")
                LASTNAME.set("")
                lbl_result2.config(text="Successfully Created!", fg="black")
            cursor.close()
            conn.close()

    # Function to store login details in admin database
    def Login():

        Database()
        if USERNAME.get() == "" or PASSWORD.get() == "":
            lbl_result1.config(text="Please complete the required field!", fg="orange")
        else:
            cursor.execute("SELECT * FROM `admin_member` WHERE `username` = ? and `password` = ?", (USERNAME.get(), PASSWORD.get()))
            if cursor.fetchone() is not None:
                lbl_result1.config(text="You Successfully Login", fg="blue")
                # Open admin home page on successful login
                root.destroy()
                Home()
            else:
                lbl_result1.config(text="Invalid Username or password", fg="red")

    # Call LoginForm function as soon as this Admin function is called 
    LoginForm()

    # ========================================INITIALIZATION===================================
    if __name__ == '__main__':
        root.mainloop()
