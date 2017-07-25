name = input('name:').strip()
age = input('age:').strip()

job = input('job:').strip()
print('Information of %s:\n'
      ' \nName:%s\nAge:%s\nJob:%s' % (name, name, age, job))
s1 = '{name} is {actor}'
d = {'name':'alex', 'actor':'good boy'}

result = s1.format(**d)
print(result)