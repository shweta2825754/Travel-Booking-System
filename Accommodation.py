from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Travel Managment")


Accom=StringVar()
Package=StringVar()
var = IntVar()
Flight = StringVar()
c=StringVar()
var1= IntVar()


def database():
   name1=Accom.get()
   package=Package.get()
   Food=var.get()
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Accomodation (Accom TEXT,Package TEXT,Food TEXT,country TEXT,Rating TEXT)')
   cursor.execute('INSERT INTO Accomodation (Accom,Package,Food,country,Rating) VALUES(?,?,?,?,?)',  (name1,package,Food,country,prog,))
   conn.commit()
   
   
            
label_0 = Label(root, text="Accomodation",width=20,font=("bold", 20))
label_0.place(x=90,y=53)

label_1 = Label(root, text="hotel-Name",width=20,font=("bold", 10))
label_1.place(x=80,y=130)

entry_1 = Entry(root,textvar=Accom)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Package",width=20,font=("bold", 10))
label_2.place(x=68,y=180)

entry_2 = Entry(root,textvar=Package)
entry_2.place(x=240,y=180)

label_3 = Label(root, text="Food",width=20,font=("bold", 10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Yes",padx = 5, variable=var, value=1).place(x=235,y=230)
Radiobutton(root, text="No",padx = 20, variable=var, value=2).place(x=290,y=230)

label_4 = Label(root, text="country",width=20,font=("bold", 10))
label_4.place(x=70,y=280)

list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=15)
c.set('select your country') 
droplist.place(x=240,y=280)

label_4 = Label(root, text="Rating",width=20,font=("bold", 10))
label_4.place(x=85,y=330)
var2= IntVar()
Checkbutton(root, text=">5", variable=var1).place(x=235,y=330)

Checkbutton(root, text="<5", variable=var2).place(x=290,y=330)

Button(root, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

root.mainloop()
