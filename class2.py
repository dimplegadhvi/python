#Creating Class

class demo:
    """This is a demo class"""
    def add(self):
        a=int(input("Enter first value:"))
        b=int(input("Enter second value:"))
        c=a+b
        print("Total = ",c)

d=demo()
print(demo.__doc__)
d.add()

                    
