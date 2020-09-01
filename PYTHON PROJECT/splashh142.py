from Tkinter import *
root=Tk()
def fun(e):
    root.destroy()
    
    #Label(root1,text=' NAME:  TWARAN SAHAI').pack()
    #Label(root1,text=' ENROLLMENT NUMBER : 171B142').pack()
    #Label(root1,text=' BATCH: B5').pack()
    #Label(root1,text=' E-MAIL: twaran12345678@gmail.com').pack()
    #Label(root1,text=' PHONE: 9179760460').pack()
img1=PhotoImage(file='./starbuck.gif')
lb=Label(root,image=img1)
lb.bind('<Motion>',fun)
lb.pack()
root.mainloop()
