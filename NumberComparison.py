lucky_num = 19
input_num = 0

while lucky_num != input_num:
    input_num = int(input('please input your number:'))

    if input_num < lucky_num:
        print('Think Bigger')
    elif input_num > lucky_num:
        print('Think smaller')
print('Good Luck')
