import tkinter as tk
from tkinter import ttk
from tkinter import *

gui = tk.Tk()
gui.title("EzClicker")
#gui.geometry('400x300')
gui.resizable(False, False)
#ecl = tk.Label(text="EzClicker").pack()

entry_cps = tk.IntVar()
var = IntVar()
def test():
    cps = entry_cps.get()
    print(cps)

    button = var.get()
    print(button)


text = tk.Label(text="How much cps?").grid(row=0, column=2)
entrycps = tk.Entry(textvariable=entry_cps).grid(row=1, column=2)
start = tk.Button(text="Start", width=20, command=test).grid(row=0, column=1)
wb1 = tk.Radiobutton(text="Left", variable=var, value=1).grid(row=1, column=1)
wb2 = tk.Radiobutton(text="Right", variable=var, value=2).grid(row=2, column=1)
quit = tk.Button(text="Quit", width=20, command=gui.destroy).grid(row=7, column=2, padx=5, pady=5)


gui.mainloop()
