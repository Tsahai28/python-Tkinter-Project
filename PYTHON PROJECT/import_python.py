from Tkinter import *
root=Tk()
#root.geometry('650x650')
def fun(e):
    root.destroy()
    root1=Tk()
    #root1.geometry('650x650')
    Label(root1,text='NAME:  TWARAN SAHAI',font=('times 20 italic'),justify='left').grid(row=0,column=0,sticky=W)
    Label(root1,text='ENROLLMENT NUMBER: 171B142',font=('times 20 italic'),justify='left').grid(row=1,column=0,sticky=W)
    Label(root1,text='BATCH: B5',font=('times 20 italic'),justify='left').grid(row=2,column=0,sticky=W)
    Label(root1,text='E-MAIL: twaran12345678@gmail.com',font=('times 20 italic'),justify='left').grid(row=3,column=0,sticky=W)
    Label(root1,text='PHONE: 9179760460',font=('times 20 italic'),justify='left').grid(row=4,column=0,sticky=W)
img1=PhotoImage(file='Untitled.gif')
lb=Label(root,image=img1)
lb.bind('<Motion>',fun)
lb.pack()
#Button(root,text=" Start ",command=fun).pack()
root.mainloop()
