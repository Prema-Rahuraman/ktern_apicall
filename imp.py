from tkinter import *
import sqlite3


root = Tk()
root.geometry('550x650')
root.maxsize(550,650)
root.minsize(550,650)
root.title('ktern')

name=StringVar()
email=StringVar()
var= StringVar()
var1 =IntVar()

def database():
    Name=name.get()
    Email=email.get()
    gender=var.get()
    Mob=var1.get()
    
    conn = sqlite3.connect('D:\python\ktern.db')
    with conn:
        
       cur=conn.cursor()
       cur.execute('CREATE TABLE IF NOT EXISTS Registration_Info(Candidate_Name TEXT,Email_Id TEXT,Gender Text,Mobile INTEGER)')
       cur.execute('INSERT INTO Registration_Info(Candidate_Name,Email_Id,Gender,Mobile) VALUES (?,?,?,?)',(Name,Email,gender,Mob,))
       conn.commit()


def change(root):
    
    conn = sqlite3.connect('D:\python\ktern.db')
    with conn:
       cur=conn.cursor()
       cur. execute("SELECT Candidate_Name,Email_Id,Gender,Mobile FROM Registration_Info")
       print(cur. fetchall())
  

    
label_0 = Label(root, text="REGISTRATION INFORMATION", width=30,font=("bold",20))
label_0.place(x=55,y=53)

label_1 = Label(root, text="Name", width=20,font=("bold",10))
label_1.place(x=80,y=130)

entry_1 = Entry(root, textvar=name)
entry_1.place(x=240,y=130)

label_2 = Label(root, text="Email", width=20,font=("bold",10))
label_2.place(x=68,y=180)

entry_3 = Entry(root, textvar=email)
entry_3.place(x=240,y=180)

label_3 = Label(root, text="Gender", width=20,font=("bold",10))
label_3.place(x=70,y=230)

Radiobutton(root, text="Male",padx =5,variable=var, value='M').place(x=235,y=230)
Radiobutton(root, text="Female",padx =20,variable=var, value='F').place(x=290,y=230)

label_4 = Label(root, text="Mobile", width=20,font=("bold",10))
label_4.place(x=82,y=280)

entry_4 = Entry(root, textvar=var1)
entry_4.place(x=240,y=280)

Button(root, text="SUBMIT",width=20,bg="brown",fg="white",command=database).place(x=180,y=350)
Button(root, text="DISPLAY",width=20,bg="brown",fg="white",command=lambda : change(root)).place(x=180,y=400)

root.mainloop()
