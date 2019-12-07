  #patt*24*** 
n=4
a=2
for i in range(1,n+1):
    for j in range(1,i+1):
        if i%2==0:
            print(a,end=" ")
            a=a+2
        else:
            print("*",end=" ")
    print()
