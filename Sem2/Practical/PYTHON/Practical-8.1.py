'''
CREATE DATABASE school;
USE school;
CREATE TABLE students(
s_rollno INT,
s_name VARCHAR(20),
s_class INT,
s_mobile INT
);
'''


import mysql.connector as sql
import tkinter
from tkinter import *
def clear():
    r1.delete('0RDNC',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
    
def insert( ):
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    cursor=db.cursor()
    a=int(r1.get())
    b=str(r2.get())
    c=int(r3.get())
    d=int(r4.get())
    query="INSERT INTO students(s_rollno, s_name, s_class, s_mobile) VALUES(%s,%s,%s,%s)"
    val=(a,b,c,d)
    cursor.execute(query,val)
    db.commit()
    db.close()


std= Tk()
std.title("Student Data")

Label(std,text="Roll no:").grid(row=0, column=0)
Label(std,text="Name:").grid(row=1, column=0)
Label(std,text="Class:").grid(row=2, column=0)
Label(std,text="Mobile no").grid(row=3, column=0)

r1 = Entry(std,bd=5)
r1.grid(row=0,column=2)
r2 = Entry(std,bd=5)
r2.grid(row=1,column=2)
r3 = Entry(std,bd=5)
r3.grid(row=2,column=2)
r4 = Entry(std,bd=5)
r4.grid(row=3,column=2)

Button(std,text="Insert",command=insert).grid(row=5,column=1,sticky="NW")
Button(std,text="Clear",command=clear).grid(row=5,column=2,sticky="NE")

mainloop()
