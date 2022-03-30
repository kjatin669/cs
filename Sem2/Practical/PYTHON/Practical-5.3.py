import tkinter
from tkinter import *

def clear():
    p.delete("0", END)
    r.delete("0", END)
    t.delete("0", END)
    s.delete("0", END)
    f.delete("0", END)

def SI():
    a = float(Entry.get(p))
    b = float(Entry.get(r))
    c = float(Entry.get(t))
    simpleInterest = (a*b*c)/100
    s.insert("0", simpleInterest)
    final=simpleInterest + a
    f.insert("0", final)

rad = Tk()
rad.title("Basic Simple Interest Calculator")

Label(rad, text="Principle: ").grid(row=0, column=0)
Label(rad, text="Rate: ").grid(row=1, column=0)
Label(rad, text="Time: ").grid(row=2, column=0)
Label(rad, text="Simple Interest: ").grid(row=6, column=0)
Label(rad, text="Final Amount: ").grid(row=7, column=0)

p=Entry(rad, bd=5)
p.grid(row=0, column=1)
r=Entry(rad, bd=5)
r.grid(row=1, column=1)
t=Entry(rad, bd=5)
t.grid(row=2, column=1)
s=Entry(rad, bd=5)
s.grid(row=6, column=1)
f=Entry(rad, bd=5)
f.grid(row=7, column=1)


Button(rad, text="Calculate", command=SI). grid(row=3, column=1, stick="NW")
Button(rad, text="Clear", command=clear). grid(row=3, column=1, stick="NE")

mainloop()
