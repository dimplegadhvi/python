#calc
a = int(input('Enter Number 1 :'))
b = int(input('Enter Number 2 :'))

print("1.Add")
print("2.sub")
print("3.div")
print("4.mul")

n = int(input("enter your choice:"))

if (n==1):
    c=a+b
    print("ans=",c)
elif (n==2):
    c=a-b
    print("ans=",c)
elif (n==3):
    c=a/b
    print("ans=",c)
elif (n==4):
    c=a*b
    print("ans=",c)
else :
    print("invalid choice")
      
