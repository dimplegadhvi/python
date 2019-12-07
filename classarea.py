#class: area of rect
class area:
    """this is area of rect"""
    def rect(self,a,b):
        ans=a*b
        print("area of rectangle =",ans)
a=area()
print(area.__doc__)
x=int(input("enter length:"))
y=int(input("enter width:"))
a.rect(x,y)
