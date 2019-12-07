#class:even and odd
class check:
    """check no. is even or odd"""
    def show(self,no1):
        if no1%2==0:
            print(no1,"is even")
        else :
            print(no1,"is odd")
c=check()
print(check.__doc__)
x=int(input("Enter no:"))
c.show(x)

    
