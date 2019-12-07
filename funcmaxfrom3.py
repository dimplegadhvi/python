#fun: max form 3
def maxfunc(a,b,c):
    if a>b and a>c:
        print(no1,'= is max')
    elif b>c and b>a:
        print(no2,'= is max')
    else:
        print(no3,'= is max')

no1 = int(input('Enter a ='))
no2 = int(input('Enter b ='))
no3 = int(input('Enter c ='))
maxfunc(no1,no2,no3)


