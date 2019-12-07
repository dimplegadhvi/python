#modfile : all functions

def add(a,b):
    c=a+b
    print("total =",c)
def sub(a,b):
    c=a-b
    print("sub =",c)
def mul(a,b):
    c=a*b
    print("mul =",c)
def div(a,b):
    c=a/b
    print("div =",c)

    
def max3(a,b,c):
    if a>b and a>c:
        print('a is max')
    elif b>c and b>a:
        print('b is max')
    else:
        print('c is max')
        
def max2(a,b):
    if a>b:
        print("a is max")
    else:
        print("b is max")

def rect(a,b):
    ans=a*b
    print("area of rectangle =",ans)
def squ(a):
    ans=a*a
    print("area of square=",ans)


def table(a):
    for i in range(1,11):
        print(a,"*",i,"=",a*i)


def lusum(a,b):
    sum=0 
    for i in range(a,b+1):
        print(i)
        sum=sum+i
    print("total is =",sum)

def fact(a):
    fact=1
    for a in range(1,a+1):
         fact = fact*a
    print("factorial=",fact)

def show(no1):
    if no1%2==0:
        print(no1,"is even")
    else :
        print(no1,"is odd")




        

