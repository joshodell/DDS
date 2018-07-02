import tkinter as tk
from tkinter import *


def hello_world():
    username_entry.delete(0, END)
    username_entry.insert(0, 'Hello world!')
    return()


root = Tk()

root.resizable(False, False)

username = tk.Label(root, text="Username:")
password = tk.Label(root, text="Password")
username_entry = tk.Entry(root)
password_entry = tk.Entry(root)
b1 = tk.Button(root, text="Run", width=15, command=hello_world)
b2 = tk.Button(root, text="quit", width=15, command = root.destroy)

username.grid(column=0, row=0, padx=5, pady=5)
username_entry.grid(column=1, row=0, padx=5, pady=5)
password.grid(column=0, row=1, padx=5, pady=5)
password_entry.grid(column=1, row=1, padx=5, pady=5)
b1.grid(column=0, row=2, padx=5, pady=5)
b2.grid(column=1, row=2, padx=5, pady=5)


root.mainloop()