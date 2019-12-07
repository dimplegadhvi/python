#for sum of lower and upper
l = int(input("enter lower limit:"))
u = int(input("enter upper limit:"))
sum = 0
for i in range(l,u+1):
    print(i)
    sum=sum+i
print("total=",sum)
