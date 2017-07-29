while True:
    num1 = input("sunki:")
    num2 = input('demi:')
    a = range(10)
    try:
        num1 = int(num1)
        num2 = int(num2)
        result = num1 + num2
        a[11]


    # 把每一项异常列出来是为了更好的处理bug
    except ValueError as e:
        print('Value Error:', e)

    except IndentationError as e:
        print('Indentation Error:', e)

    except Exception as e:
        print('unexpected error:')
        print(e)
