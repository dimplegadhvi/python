#class: lowerlimit to upperlimit
class show():
    """this is sum of lower-limit and upper-limit"""
    def sumfun(self,l,w):
        sum=0 
        for i in range(l,w+1):
            print(i)
            sum=sum+i
        print("total=",sum)
s=show()
print(show.__doc__)
x=int(input("Enter lower limit:"))
y=int(input("Enter upper limit:"))
s.sumfun(x,y)

