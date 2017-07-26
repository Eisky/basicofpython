data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 9, 1, 17, 13, 6]

for j in range(1,len(data)):
    for i in range(len(data) - j):
        if data[i] > data[i + 1]:
            tmp = data[i]
            data[i] = data[i + 1]
            data[i + 1] = tmp

print(data)
