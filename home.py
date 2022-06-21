from tkinter import *
import sqlite3

root = Tk()
root.geometry('500x500')
root.title("Travel Managment")
def cust():
	root1 = Toplevel(root)
	Fullname=StringVar()
	Email=StringVar()
	var = IntVar()
	Flight = StringVar()
	c=StringVar()
	var1= IntVar()

	def database():
		name1=Fullname.get()
		email=Email.get()
		gender=var.get()
		flight=Flight.get()
		country=c.get()
		prog=var1.get()
		conn = sqlite3.connect('Form.db')
		with conn:
			cursor=conn.cursor()
		cursor.execute('CREATE TABLE IF NOT EXISTS Customer (Fullname TEXT,Email TEXT,Gender TEXT, Flight TEXT,country TEXT,payment TEXT)')
		cursor.execute('INSERT INTO Customer (FullName,Email,Gender,Flight,country,payment) VALUES(?,?,?,?,?,?)',  (name1,email,gender,flight,country,prog,))
		conn.commit()
      
             
	label_0 = Label(root1, text="Booking",width=20,font=("bold", 20))
	label_0.place(x=90,y=53)


	label_1 = Label(root1, text="FullName",width=20,font=("bold", 10))
	label_1.place(x=80,y=130)

	entry_1 = Entry(root1,textvar=Fullname)
	entry_1.place(x=240,y=130)

	label_2 = Label(root1, text="Email",width=20,font=("bold", 10))
	label_2.place(x=68,y=180)

	entry_2 = Entry(root1,textvar=Email)
	entry_2.place(x=240,y=180)

	label_3 = Label(root1, text="Gender",width=20,font=("bold", 10))
	label_3.place(x=70,y=230)

	Radiobutton(root1, text="Male",padx = 5, variable=var, value=1).place(x=235,y=230)
	Radiobutton(root1, text="Female",padx = 20, variable=var, value=2).place(x=290,y=230)

	label_4 = Label(root1, text="country",width=20,font=("bold", 10))
	label_4.place(x=70,y=280)

	list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

	droplist=OptionMenu(root1,c, *list1)
	droplist.config(width=15)
	c.set('select your country') 
	droplist.place(x=240,y=280)

	label_7 = Label(root1, text="FlightName",width=20,font=("bold", 10))
	label_7.place(x=80,y=260)

	entry_7 = Entry(root1,textvar=Flight)
	entry_7.place(x=240,y=260)

	label_4 = Label(root1, text="payment",width=20,font=("bold", 10))
	label_4.place(x=85,y=330)
	var2= IntVar()
	Checkbutton(root1, text="Credit", variable=var1).place(x=235,y=330)

	Checkbutton(root1, text="Net", variable=var2).place(x=290,y=330)

	Button(root1, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
def staff():
	root2 = Toplevel(root)
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


	label_0 = Label(root2, text="Staff Details",width=20,font=("bold", 20))
	label_0.place(x=90,y=53)

	label_1 = Label(root2, text="Name",width=20,font=("bold", 10))
	label_1.place(x=80,y=130)

	entry_1 = Entry(root2,textvar=Fullname)
	entry_1.place(x=240,y=130)

	label_2 = Label(root2, text="Age",width=20,font=("bold", 10))
	label_2.place(x=68,y=180)

	entry_2 = Entry(root2,textvar=Age)
	entry_2.place(x=240,y=180)

	label_3 = Label(root2, text="Salary",width=20,font=("bold", 10))
	label_3.place(x=70,y=230)

	Radiobutton(root2, text="50k",padx = 5, variable=var, value=1).place(x=235,y=230)
	Radiobutton(root2, text="100k",padx = 20, variable=var, value=2).place(x=290,y=230)
	Radiobutton(root2, text="20k",padx = 30, variable=var, value=3).place(x=370,y=230)

	label_4 = Label(root2, text="Designation",width=20,font=("bold", 10))
	label_4.place(x=70,y=280)

	list1 = ['Manager','CEO','Clerk','Developer','Director','Assistant-Mamager'];

	droplist=OptionMenu(root2,c, *list1)
	droplist.config(width=15)
	c.set('select')
	droplist.place(x=240,y=280)

	label_7 = Label(root2, text="Address",width=20,font=("bold", 10))
	label_7.place(x=85,y=330)

	entry_7 = Entry(root2,textvar=Addr)
	entry_7.place(x=240,y=330)

	Button(root2, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)
def Accommodation():
	root3 = Toplevel(root)
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
   
   
            
	label_0 = Label(root3, text="Accomodation",width=20,font=("bold", 20))
	label_0.place(x=90,y=53)

	label_1 = Label(root3, text="hotel-Name",width=20,font=("bold", 10))
	label_1.place(x=80,y=130)

	entry_1 = Entry(root3,textvar=Accom)
	entry_1.place(x=240,y=130)

	label_2 = Label(root3, text="Package",width=20,font=("bold", 10))
	label_2.place(x=68,y=180)

	entry_2 = Entry(root3,textvar=Package)
	entry_2.place(x=240,y=180)

	label_3 = Label(root3, text="Food",width=20,font=("bold", 10))
	label_3.place(x=70,y=230)

	Radiobutton(root3, text="Yes",padx = 5, variable=var, value=1).place(x=235,y=230)
	Radiobutton(root3, text="No",padx = 20, variable=var, value=2).place(x=290,y=230)

	label_4 = Label(root3, text="country",width=20,font=("bold", 10))
	label_4.place(x=70,y=280)

	list1 = ['Canada','India','UK','Nepal','Iceland','South Africa'];

	droplist=OptionMenu(root3,c, *list1)
	droplist.config(width=15)
	c.set('select your country') 
	droplist.place(x=240,y=280)
	
	label_4 = Label(root3, text="Rating",width=20,font=("bold", 10))
	label_4.place(x=85,y=330)
	var2= IntVar()
	Checkbutton(root3, text=">5", variable=var1).place(x=235,y=330)

	Checkbutton(root3, text="<5", variable=var2).place(x=290,y=330)

	Button(root3, text='Submit',width=20,bg='brown',fg='white',command=database).place(x=180,y=380)

Button(root, text ="Customer", relief=RAISED,command=cust).pack()
Button(root, text ="Staff", relief=RAISED,command=staff).pack()
Button(root, text ="Accomodation", relief=RAISED,command=Accommodation).pack()

root.mainloop()
