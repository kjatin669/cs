from tkinter import *
rad=Tk()
def render():
    rad.title('Font, Size & Color ')
    t = Text(rad, height=5 , bd=5)
    t.grid(row = 0, column=1)
    Font = (var1.get(),var2.get())
    t.config(font=Font , fg= var3.get())
    
Label(rad,text="Enter Text").grid(row=0, column=0)
Label(rad,text="Font").grid(row=1, column=0)
Label(rad,text="Size").grid(row=1, column=1)
Label(rad,text="Color").grid(row=1, column=2)

var1=StringVar()
Radiobutton(rad,text="Arial",padx=2,variable=var1,value="Arial").grid(row=2,column=0)
Radiobutton(rad,text="Times New Roman",padx=2,variable=var1,value="Times New Roman").grid(row=3,column=0)           
Radiobutton(rad,text="Calibri",padx=2,variable=var1,value="Calibri").grid(row=4,column=0)


var2=IntVar()
Radiobutton(rad,text="8",padx=2,variable=var2,value=8).grid(row=2,column=1)
Radiobutton(rad,text="10",padx=2,variable=var2,value=10).grid(row=3,column=1)
Radiobutton(rad,text="12",padx=2,variable=var2,value=12).grid(row=4,column=1)

var3=StringVar()
Radiobutton(rad,text="Red",padx=2,variable=var3,value="Red").grid(row=2,column=2)
Radiobutton(rad,text="Blue",padx=2,variable=var3,value="Blue").grid(row=3,column=2)
Radiobutton(rad,text="Yellow",padx=2,variable=var3,value="Yellow").grid(row=4,column=2)

Button(rad,text="Render",command=render).grid(row=5,column=1,sticky="NW")
