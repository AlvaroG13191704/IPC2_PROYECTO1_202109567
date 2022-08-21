from tkinter import *

root = Tk()

for r in range(0, 5):
    for c in range(0, 5):
        cell = Entry(root, width=10)
        cell.config(bg='#440c29')
        cell.grid(padx=5, pady=5, row=r, column=c)
        cell.insert(0,'')

root.mainloop()