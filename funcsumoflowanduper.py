# func : sum of low and upper
def sumfun(l,w):
    sum=0 
    for i in range(l,w+1):
        print(i)
        sum=sum+i
    return sum
a = int(input("enter lower limit:"))
b = int(input("enter upper limit:"))

c=sumfun(a,b)
print("total =",c)

