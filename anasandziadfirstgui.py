from tkinter import *
window=Tk() #my master window
window.title("First app")# my window title
window.geometry("400x200")
text1=StringVar()
def printname():
    text1.get()
    text1.set("Welcome to Anas & Zeiad First App ")
    print("Welcome to Anas & Zeiad First App ")





button1=Button(window,bg='red',width=20,text='Print',command=printname)
#button1.grid(row=1,column=2)
button1.pack()
label1=Label(window,bg='gray',width=50,textvariable=text1,font=(20))
label1.pack()
