#bankbal
bal = 0
while 1:
    print('1.Deposit')
    print('2.Wdr')
    print('3.check Bal')
    print('0.exit')
    no = int(input('Enter Choice'))
    if no==1:
        amnt = float(input('Enter Amount'))
        bal += amnt
    elif no==2:
        amnt = float(input('Enter Amount'))
        bal -= amnt
    elif no==3:
        print('Bal Is ',bal)
    else:
        exit(1)
    
