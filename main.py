import tkinter as tk
from tkinter import *
#from tkinter.ttk import *
#from tkinter import ttk

gui = tk.Tk()
var = IntVar()
gui.title("EzClicker")
#gui.geometry('400x300')
gui.resizable(False, False)
#ecl = tk.Label(text="EzClicker").pack()

hwtext = tk.Label(text="How much cps?").grid(row=0, column=2)
hwentry = tk.Entry().grid(row=1, column=2)
start = tk.Button(text="Start", width=20, command=gui.destroy).grid(row=0, column=1)
wb1 = tk.Radiobutton(text="Left", variable=var, value=1).grid(row=1, column=1)
wb2 = tk.Radiobutton(text="Right", variable=var, value=2).grid(row=2, column=1)
quit = tk.Button(text="Quit", width=20, command=gui.destroy).grid(row=7, column=2, padx=5, pady=5)

gui.mainloop()
