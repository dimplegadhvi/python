#class:fact
class fact:
    """this is fact prog:"""
    def fact(self,a):
        fact=1
        for a in range(1,a+1):
             fact = fact*a
        print("factorial=",fact)
f=fact()
print(fact.__doc__)
x=int(input("Enter no:"))
f.fact(x)


