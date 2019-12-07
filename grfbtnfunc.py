#graf1 : button func
from tkinter import *
def func1():
    print("welcome")
root=Tk()
Button(root,text="click me",bg="black",fg="white",command=func1).place(x=20,y=100,height=30,width=160)

mainloop()
