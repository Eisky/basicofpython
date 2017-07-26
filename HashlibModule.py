import hashlib

my_information = hashlib.md5()
my_information.update('this is sunki from earth'.encode('utf-8'))
print(my_information.digest())
print(my_information.hexdigest())

import hmac

a = hmac.new('wer') #要传递的信息
a.update('Can I use  your bag') #要加密的信息
print(a.digest())
print(a.hexdigest())