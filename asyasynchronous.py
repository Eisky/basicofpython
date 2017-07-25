import time


def consumer(name):
    print('%s is ready to eat baozi' % name)
    while True:
        baozi = yield
        print('baozi[%s] comes, and ate by[%s]' % (baozi, name))



def producer(name):
    c = consumer('A')
    d = consumer('B')
    c.__next__()
    d.__next__()
    print('I am going to make baozi!')
    for i in range(5):
        time.sleep(1)
        print('________')
        c.send(i)
        d.send(i)

producer('sunki')