#square patt*
n=5
for i in range(1,n):
    for j in range(1,n):
        if i==1 or i==4 or j==1 or j==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
