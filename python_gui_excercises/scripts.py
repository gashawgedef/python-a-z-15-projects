from tkinter import *

gashity = Tk()
gashity.title("My gashity portyfolio")

name = Label(gashity,text="Bitcoin",bg="black",fg="white")
name.grid(row=0,column=0,sticky=N+S+E+W)
gashity.mainloop()