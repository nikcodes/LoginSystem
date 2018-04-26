from tkinter import *
root=Tk()
root.title('Welcome')

a=[]

def new():
    cs=1
    def signup():
        global cs
        if len(e1.get())==0 or len(e2.get())==0:
            Label(r1, text='Invalid entries').grid(row=4, columnspan=2)
            cs=0
            return
        if [e1.get(),e2.get()] in a:
            Label(r1, text='User exist').grid(row=3, columnspan=2)
            return
        a.append([e1.get(), e2.get()])
        Label(r1,text='signed up').grid(row=3,columnspan=2)

    r1=Tk()
    Label(r1,text='Name').grid(row=0)
    Label(r1,text='Password').grid(row=1)
    e1=Entry(r1)
    e2=Entry(r1)
    e1.grid(row=0,column=1)
    e2.grid(row=1,column=1)
    Button(r1,text='Signup',command=signup).grid(row=2,columnspan=2)
    r1.mainloop()

def no():
    def login():
        if [e1.get(),e2.get()] in a:
            Label(r2,text='Successfully signed in').grid(row=3,columnspan=2)
            e1.delete(0, END)
            e2.delete(0, END)
        else:
            Label(r2, text='Incorrect login').grid(row=3, columnspan=2)
            e1.delete(0,END)
            e2.delete(0,END)
    r2 = Tk()
    Label(r2, text='Name').grid(row=0)
    Label(r2, text='Password').grid(row=1)
    e1 = Entry(r2)
    e2 = Entry(r2)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(r2, text='Login', command=login).grid(row=2, columnspan=2)
    r2.mainloop()

def delete():
    def dele():
        if [e1.get(),e2.get()] in a:
            a.remove([e1.get(),e2.get()])
            Label(r2,text='Successfully deleted').grid(row=3,columnspan=2)
            e1.delete(0, END)
            e2.delete(0, END)
        else:
            Label(r2, text="user doesn't exist").grid(row=3, columnspan=2)

    r2 = Tk()
    Label(r2, text='Name').grid(row=0)
    Label(r2, text='Password').grid(row=1)
    e1 = Entry(r2)
    e2 = Entry(r2)
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    Button(r2, text='Delete', command=dele).grid(row=2, columnspan=2)
    r2.mainloop()
Button(root,text='Sign up',width=10,height=3,command=new).grid(row=0,pady=10)
Button(root,text='Login',width=10,height=3,command=no).grid(row=0,column=1,pady=10)
Button(root,text='delete user',width=21,height=3,command=delete).grid(row=1,columnspan=2)
root.mainloop()
