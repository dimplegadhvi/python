#class: display
class display:
    """this is display of records"""
    def show(self,a,b,c):
        print("name=",a)
        print("marks=",b)
        print("rollno=",c)
d=display()
print(display.__doc__)
x=str(input("Enter name:"))
y=int(input("Enter marks:"))
z=int(input("Enter rollno:"))
d.show(x,y,z)
        
    
