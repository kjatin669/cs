import mysql.connector as sql
import tkinter
from tkinter import *
from tkinter import messagebox

n = 0

def clear():
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
    
def first( ):
    global n
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    print("First Row Printed")
    cursor=db.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    n = 0
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
    r1.insert('0',data[n][0])
    r2.insert('0',data[n][1])
    r3.insert('0',data[n][2])
    r4.insert('0',data[n][3])
    db.close()
    
def Next( ):
    global n
    rno = int(r3.get())
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    print("Next Row Printed")
    cursor=db.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    n = n+1
    try:
        r1.delete('0',END)
        r2.delete('0',END)
        r3.delete('0',END)
        r4.delete('0',END)
        r1.insert('0',data[n][0])
        r2.insert('0',data[n][1])
        r3.insert('0',data[n][2])
        r4.insert('0',data[n][3])
    except:
        messagebox.showerror('ERROR','last data, No further data')
    db.close()
    
def previous( ):
    global n
    rno = int(r3.get())
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    cursor=db.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    data=cursor.fetchall()
    print (data)
    n = n-1
    if n>0:
        r1.delete('0',END)
        r2.delete('0',END)
        r3.delete('0',END)
        r4.delete('0',END)
        r1.insert('0',data[n][0])
        r2.insert('0',data[n][1])
        r3.insert('0',data[n][2])
        r4.insert('0',data[n][3])
    else:
        messagebox.showerror('ERROR','First data, No previous data')
    db.close()

def last( ):
    global n
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    print("Last Row Printed")
    cursor=db.cursor()
    query="SELECT * FROM students"
    cursor.execute(query)
    data=cursor.fetchall()
    print(data)
    n = len(data)-1
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
    r1.insert('0',data[n][0])
    r2.insert('0',data[n][1])
    r3.insert('0',data[n][2])
    r4.insert('0',data[n][3])
    db.close()


std=Tk()
std.title("Student Data")

Label(std,text="Mobile no").grid(row=0, column=0)
Label(std,text="Name:").grid(row=1, column=0)
Label(std,text="Roll no:").grid(row=2, column=0)
Label(std,text="Class:").grid(row=3, column=0)

r1 = Entry(std,bd=5)
r1.grid(row=0,column=1)
r2= Entry(std,bd=5)
r2.grid(row=1,column=1)
r3= Entry(std,bd=5)
r3.grid(row=2,column=1)
r4= Entry(std,bd=5)
r4.grid(row=3,column=1)

Button(std,text="Clear",command=clear).grid(row=6,column=1,sticky="NW")
Button(std,text="First",command=first).grid(row=5,column=1,sticky="NW")
Button(std,text="Next",command=Next).grid(row=5,column=1,sticky="NE")
Button(std,text="Previous",command=previous).grid(row=5,column=2,sticky="NW")
Button(std,text="Last",command=last).grid(row=5,column=3,sticky="NW")

mainloop()
