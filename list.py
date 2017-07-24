name_list = ['sunki', 'demi', 'yuki']
print(name_list[0])
name_list.append('eve')
print(name_list)
name_list.append('sunki')
print(name_list)
print(name_list.count('sunki'))  # find sunki number
name_list.reverse()  # 反序
print(name_list)
name_list.sort()  # 按照ascii码排序
print(name_list)
name_list.insert(2, 'bella')
name_list.insert(1, 'sunki')
print(name_list)
for i in range(name_list.count('sunki')):#通过count函数
    #找到sunki的个数，然后用remove函数删除sunki
    name_list.remove('sunki')
print(name_list)
name_list1 = ['sunki','emily']
print(name_list+name_list1)
print(name_list.extend(name_list1))
name_list2 = 'sunki'
c = name_list.extend(name_list2)
print(c)
print(type(c))
print('yuki' in name_list)