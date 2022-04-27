import tkinter
from tkinter import *

def calculate():
    a=int(Entry.get(r1))
    b=int(Entry.get(r2))
    d=int(Entry.get(r3))
    e=a*4+b*4+d*9
    r4.insert('0',e)

def clear():
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
 
c=Tk()
c.title("Calorie Center")

Label(c,text="Protein(grams)").grid(row=0, column=0)
Label(c, text="Carbohydrates(grams)").grid(row=1, column=0)
Label(c,text="Fats(grams)").grid(row=2, column=0)
Label(c,text="Total Energy").grid(row=3, column=0)

r1 = Entry(c, bd=5)
r1.grid(row=0, column=1)
r2= Entry(c, bd=5)
r2.grid(row=1, column=1)
r3= Entry(c, bd=5)
r3.grid(row=2, column=1)
r4 = Entry(c, bd=5)
r4.grid(row=3, column=1)

Button(c,text="Calculate",command=calculate).grid(row=5,column=1,sticky="NW")
Button(c,text="Clear",command=clear).grid(row=5,column=1,sticky="NE")

mainloop( )
