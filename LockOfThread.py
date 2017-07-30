import time
import threading


def addNum():
    global num  # define global variable
    lock.acquire()
    print('get number:', num)
    time.sleep(0.02)
    num -= 1  # opearte on global variable
    lock.release()

lock = threading.Lock()
num = 20
t_list = []
for i in range(20):
    t = threading.Thread(target=addNum)
    t.start()
    t_list.append(t)

for t in t_list:  # 等待所有线程执行完毕
    t.join()
