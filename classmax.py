#class:max prog
class max:
    """Find no is max"""
    def maxx(self,a,b):
            if a>b:
                print(a,"is max")
            else:
                print(b,"is max")

m=max()
print(max.__doc__)
x=int(input("Enter no:"))
y=int(input("Enter no:"))
m.maxx(x,y)

