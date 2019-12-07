#find min no. from 3 no.
no1 = int(input('Enter Number 1 :'))
no2 = int(input('Enter Number 2 :'))
no3 = int(input('Enter Number 3 :'))

if no1<no2 and no1<no3:
    print('no1 is min')
elif no2<no3 and no2<no1:
    print('no2 is min')
else:
    print('no3 is min')
