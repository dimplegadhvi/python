#fun: ret value(max)
def maxfun(a,b):
 if a>b:
     return a
 else :
     return b

n1 = int(input("enter no.:"))
n2 = int(input("enter no.:"))

ans=maxfun(n1,n2)
print(" max =",ans)
