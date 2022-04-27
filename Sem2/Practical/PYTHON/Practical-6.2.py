import tkinter
from tkinter import *

def calculate():
    sum=0
    if(var1.get()==1):
        sum+=250
    if(var2.get()==1):
        sum+=300
    if(var3.get()==1):
        sum+=1000
    if(var4.get()==1):
        sum+=10
    r1.delete('0',END)
    r1.insert('0',sum)
    discount=0
    if(var.get()==1):
        discount=0
    if(var.get()==2):
        discount=sum * 0.05
    if(var.get()==3):
        discount=sum * 0.1
    r2.delete('0',END)
    r2.insert('0',discount)
    fa=sum-discount
    r3.insert('0',fa)
    
def clear():
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    
rad = Tk()
rad.title("Jay's Sandwich")

canvas_width = 500
canvas_height = 500
w = Canvas(rad,
           width=canvas_width,
           height=canvas_height,
           bg='green',
           highlightbackground='red',
           highlightthickness='5',
           cursor='trek')

Label(rad,text="Operations").grid(row=0, column=0)
Label(rad,text="Discount").grid(row=0, column=3)
Label(rad,text="Total cost:::").grid(row=7, column=0)
Label(rad,text="Discount:::").grid(row=8, column=0)
Label(rad,text="Net Payable Amount:::").grid(row=9, column=0)

r1 = Entry(rad,bd=5)
r1.grid(row=7,column=1)
r2= Entry(rad,bd=5)
r2.grid(row=8,column=1)
r3= Entry(rad,bd=5)
r3.grid(row=9,column=1)

Button(rad,text="Calculate",command=calculate).grid(row=5,column=1,sticky="NW")
Button(rad,text="Clear",command=clear).grid(row=5,column=1,sticky="NE")

var1=IntVar()
Checkbutton(rad,text="Grilled Cheese = 250",variable=var1).grid(row=1,sticky='W')

var2=IntVar()
Checkbutton(rad,text="BLT Sandwich = 300",variable=var2).grid(row=2,sticky='W')

var3=IntVar()
Checkbutton(rad,text="McNuggets = 1000",variable=var3).grid(row=3,sticky='W')

var4=IntVar()
Checkbutton(rad,text="Takeaway = 10",variable=var4).grid(row=4,sticky='W')

var=IntVar()
Radiobutton(rad,text="None",padx=2,variable=var,value=1).grid(row=1,column=3)
Radiobutton(rad,text="5%",padx=2,variable=var,value=2).grid(row=2,column=3)
Radiobutton(rad,text="10%",padx=2,variable=var,value=3).grid(row=3,column=3)

mainloop( )
