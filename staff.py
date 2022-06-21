from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Travel Managment")


Fullname=StringVar()
Age=StringVar()
var = IntVar()
Addr = StringVar()
c=StringVar()
var1= IntVar()


def database():
   name1=Fullname.get()
   age=Age.get()
   salary=var.get()
   A=Addr.get()
   desig=c.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS staff (Fullname TEXT,age TEXT,Salary TEXT,Designation TEXT,address TEXT)')
   cursor.execute('INSERT INTO staff (FullName,age,Salary,Designation,address) VALUES(?,?,?,?,?)',(name1,age,salary,desig,A,))
   conn.commit()


label_0 = Label(root, text="Staff Details",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Fullname)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Age",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Age)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Salary",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="50k",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="100k",padx = 20, variable=var, value=2).place(x=290,y=230)
Radiobutton(root, text="20k",padx = 30, variable=var, value=3).place(x=370,y=230)

label_4 = Label(root, text="Designation",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Manager','CEO','Clerk','Developer','Director','Assistant-Mamager'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select')
droplist.place(x=240,y=280)

label_7 = Label(root, text="Address",width=20,font=("bold", 10))
label_7.place(x=85,y=330)

entry_7 = Entry(root,textvar=Addr)
entry_7.place(x=240,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()

