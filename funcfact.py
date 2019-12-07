#func: fact
def fact(i):
    fact=1
    for i in range(1,i+1):
         fact = fact*i
    print("factorial=",fact)

a = int(input("enter any number:"))
fact(a)

    
