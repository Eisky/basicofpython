def money_get(cash):
    while cash>0:
        cash-=100
        yield 100
        print('come and get money again')


atm = money_get(500)
print(atm.__next__())
print(atm.__next__())
print(atm.__next__())
print('you have to wait for 2 days')
print(atm.__next__())
print(atm.__next__())
