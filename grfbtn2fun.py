#graf1 : button func
from tkinter import *
def func1():
    print("welcome")
def func2():
    print("hello smart allu sir")

root=Tk()
Button(root,text="btn1",bg="olive",fg="white",command=func1).place(x=20,y=100,height=30,width=160)
Button(root,text="btn2",bg="white",fg="black",command=func2).place(x=20,y=150,height=30,width=160)

mainloop()
