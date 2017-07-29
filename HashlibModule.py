import hashlib
import datetime

my_information = hashlib.md5()
my_information.update('this is sunki from earth'.encode('utf-8'))
print(my_information.digest())
print(my_information.hexdigest())

import hmac
key = 'you will never know'
msg = 'what is in the box'
m = hmac.new(key, msg, hashlib.sha1())
print(m.hexdigest())