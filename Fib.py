def Fib(a, b, stop):
    if a == 0:
        print(a, b)

    c = a + b
    print(c)

    if c < stop:
        Fib(b, c, stop)


Fib(0,1,10)
