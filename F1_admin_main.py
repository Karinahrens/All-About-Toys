# Musnath Ahamed - ID 001090034
import tkinter as tk
# from tkinter import *
from F1_admin_index import Admin


root = tk.Tk()
frame = tk.Frame(root, background='peach puff')
frame.pack()


def admin_panel():
    root.destroy()
    Admin()


tk.Label(frame, text="Welcome To AllAboutToys Ltd", bg='old lace').pack()
tk.Button(frame, text="Admin Page", pady=5, padx=30, command = admin_panel, bg='snow3').pack()


root.mainloop()
