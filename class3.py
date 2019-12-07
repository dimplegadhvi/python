#Creating object

class demo:
    """This is a demo class"""
    def add(self,a,b):

        c=a+b
        print("Total = ",c)

d=demo()
print(demo.__doc__)
x=int(input("Enter first value:"))
y=int(input("Enter Second value:"))
d.add(x,y)
