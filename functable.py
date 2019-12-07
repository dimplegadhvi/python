#fun: table print
def tablefun(no1):
    for i in range(1,11):
        print(no1,"*",i,"=",no1*i)
a = int(input("enter any no."))

tablefun(a)
