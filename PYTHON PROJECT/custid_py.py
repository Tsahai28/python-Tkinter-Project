import sqlite3
from Tkinter import *
from tkMessageBox import *
con=sqlite3.Connection('rakesh_sql')
cur=con.cursor()
cur.execute("create table if not exists customer(id varchar2(10) primary key,first_name varchar2(50) not null,last_name varchar2(11))")
def insert():
    showinfo('response','Are you sure to insert the data')
    cur.execute("insert into customer values(?,?,?)",(e1.get(),e2.get(),e3.get()))
    con.commit()
def show():
    showinfo('response','Show full data')
    cur.execute("select * from customer where id==(?)",(e4.get(),))
    a=cur.fetchall()
    Label(root,text=a).grid(row=6,column=1)
def show_all():
    showinfo('response','Do you agree')
    cur.execute("select * from customer")
    a1=cur.fetchall()
    Label(root,text=a1).grid(row=6,column=1)

root=Tk()
Label(root,text='STARBUCK GOLD CARD:',relief='ridge',font='Oswald 20 bold italic').grid(row=0,column=1)
Label(root,text='FULL NAME:',font='times 15').grid(row=1,column=0)
e1=Entry(root)
e1.grid(row=1,column=1)
Label(root,text='MOBILE:',font='times 15').grid(row=2,column=0)
e2=Entry(root)
e2.grid(row=2,column=1)
Label(root,text='EMAIL:',font='times 15').grid(row=3,column=0)
e3=Entry(root)
e3.grid(row=3,column=1)
Label(root,text='ENTER ID TO FETCH INFO:',font='times 15').grid(row=4,column=0)
e4=Entry(root)
e4.grid(row=4,column=1)
Button(root,text='Insert',font='times 15',command=insert).grid(row=5,column=0)
Button(root,text='Show',font='times 15',command=show).grid(row=5,column=1)
Button(root,text='Show All',font='times 15',command=show_all).grid(row=5,column=2)

root.mainloop()
