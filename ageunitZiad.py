from tkinter import *
from tkinter import messagebox
ageapp=Tk()#My app master
ageapp.geometry("400x400")
ageapp.title("Age Units")
age=StringVar()
age.set("00")
agelabel=Label(ageapp,width=30, heigh=2,text='Write your age',font=('Arial',30))
agelabel.pack()
age_entry=Entry(ageapp,width=2,font=('Arial',30),textvariable=age)
age_entry.pack()
def calc():
    age_value=age.get()
    age_months=int(age_value)*12
    age_weeks=age_months*4
    age_days=int(age_value)*365
    m=f"Your age in months:{age_months},\n"
    w=f"Your age in weeks:{age_weeks},\n"
    d=f"Your age in days:{age_days}"
    agelist=[m,w,d]
    messagebox.showinfo("age units",agelist)
   # messagebox.showinfo("age units",m)
   # messagebox.showinfo("age units",w)
   # messagebox.showinfo("age units",d)
button=Button(ageapp,width=10,text='Calculate Age',font=('Arial',20),bg='red',command=calc)
button.pack()
ageapp.mainloop()
