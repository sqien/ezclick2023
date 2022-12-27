from tkinter import *
from tkinter import ttk

gui = Tk()
frm = ttk.Frame(gui, padding=10)
frm.grid()
ttk.Label(frm, text="EzClicker").grid(column=0, row=0)
ttk.Button(frm, text="Quit", command=gui.destroy).grid(column=2, row=1)
ttk.Button(frm, text="Start", command=gui.destroy).grid(column=1, row=0)
gui.mainloop()
