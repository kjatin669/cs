import mysql.connector as sql
import tkinter
from tkinter import *

def clear():
    r1.delete('0',END)
    r2.delete('0',END)
    r3.delete('0',END)
    r4.delete('0',END)
    r5.delete('0',END)
    r6.delete('0',END)
    r7.delete('0',END)
    
def load( ):
    db=sql.connect(host="localhost", port=3306, user="root", passwd="itsofficialdp", db="school")
    print("Connected")
    cursor=db.cursor()
    Mobile=[int(r1.get())]
    query="SELECT * FROM students WHERE s_mobile=%s"
    cursor.execute(query, Mobile)
    rows=cursor.fetchone()
    print(rows)
    Name=rows[1]
    Rollno=rows[0]
    Class=rows[2]
    clear()
    r1.insert('0', Mobile)
    r2.insert('0',Name)
    r3.insert('0',Rollno)
    r4.insert('0',Class)
    cursor.close()
    
def update():
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("connected")
    cursor=db.cursor()
    Mobile=int(r1.get())
    a=str(r5.get())
    b=int(r6.get())
    c=str(r7.get())
    query="UPDATE students SET s_name=%s, s_rollno=%s, s_class=%s WHERE s_mobile=%s"
    val=[a,b,c,Mobile]
    cursor.execute(query,val)
    db.commit()
    print("Updated")
    cursor.close()

def delete():
    db=sql.connect(host="localhost",port=3306,user="root",passwd="itsofficialdp",db="school")
    print("Connected")
    cursor=db.cursor()
    Mobile=[int(r1.get())]
    query="DELETE FROM students WHERE s_mobile=%s"
    cursor.execute(query,Mobile)
    db.commit()
    print("Deleted Successfully")
    cursor.close()

    
std=Tk()

std.title("Student Data")
Label(std,text="Mobile no").grid(row=0, column=0)
Label(std,text="Update list").grid(row=0, column=2)
Label(std,text="Name:").grid(row=2, column=0)
Label(std,text="Roll no:").grid(row=3, column=0)
Label(std,text="Class:").grid(row=4, column=0)

r1 = Entry(std,bd=5)
r1.grid(row=0,column=1)
r2= Entry(std,bd=5)
r2.grid(row=2,column=1)
r3= Entry(std,bd=5)
r3.grid(row=3,column=1)
r4= Entry(std,bd=5)
r4.grid(row=4,column=1)
r5= Entry(std,bd=5)
r5.grid(row=2,column=2)
r6= Entry(std,bd=5)
r6.grid(row=3,column=2)
r7= Entry(std,bd=5)
r7.grid(row=4,column=2)

    
Button(std,text="Clear",command=clear).grid(row=5,column=1,sticky="NE")
Button(std,text="Load",command=load).grid(row=1,column=0,sticky="NW")
Button(std,text="Update",command=update).grid(row=1,column=2,sticky="NW")
Button(std,text="Delete",command=delete).grid(row=1,column=2,sticky="NE")

mainloop()

