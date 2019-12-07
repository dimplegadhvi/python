#class: display
class display():
    """this is display of records"""
    def show(self,a,b,c,d,e,f):
            print("name=",a)
            print("marks=",b)
            print("rollno=",c)
            print("name=",d)
            print("marks=",e)
            print("rollno=",f)
d=display()
print(display.__doc__)
u=str(input("Enter name:"))
v=int(input("Enter marks:"))
w=int(input("Enter rollno:"))
x=str(input("Enter name:"))
y=int(input("Enter marks:"))
z=int(input("Enter rollno:"))

d.show(x,y,z,u,v,w)
        
    

