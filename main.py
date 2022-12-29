import tkinter as tk

gui = tk.Tk()
gui.geometry('400x300')
gui.resizable(False, False)
ecl = tk.Label(text="EzClicker").pack()

start = tk.Button(text="Start", width=20, command=gui.destroy).pack()
quit = tk.Button(text="Quit", width=20, command=gui.destroy).pack()

gui.mainloop()
