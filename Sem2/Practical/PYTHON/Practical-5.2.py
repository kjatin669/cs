import tkinter
from tkinter import *

def clear():
    n1.delete("0", END)
    n2.delete("0", END)
    n3.delete("0", END)

def add():
    a = int(Entry.get(n1))
    b = int(Entry.get(n2))
    addition = a+b
    n3.insert("0", addition)
    
def sub():
    l = int(Entry.get(n1))
    d = int(Entry.get(n2))
    subtraction = l-d
    n3.insert("0", subtraction)
    
def mul():
    e = int(Entry.get(n1))
    f = int(Entry.get(n2))
    multiplication = e*f
    n3.insert("0", multiplication)
    
def div():
    g = int(Entry.get(n1))
    h = int(Entry.get(n2))
    division = g/h
    n3.insert("0", division)

c = Tk()
c.title("Calculator")

Label(c, text="1st Number: ").grid(row=0)
Label(c, text="2nd Number: ").grid(row=1)
Label(c, text="Result: ").grid(row=2)

n1 = Entry(c, bd=2)
n2 = Entry(c, bd=2)
n3 = Entry(c, bd=2)
n1.grid(row=0, column=1)
n2.grid(row=1, column=1)
n3.grid(row=2, column=1)

Button(c, text="+", command=add).grid(row=4, column=0)
Button(c, text="-", command=sub).grid(row=4, column=1)
Button(c, text="*", command=mul).grid(row=5, column=0)
Button(c, text="/", command=div).grid(row=5, column=1)
Button(c, text="Clear", command=clear).grid(row=6, column=1)
