# coding:utf-8

data = [55,44,11,77,66,99,88,33,22]
# data = [55,44,11,77,66,99,88,33,22]
print(data)
def maopao(data):
    for i in range(len(data)-1):                 #循环四次 data-1是指减去一次循环次数，最后一个数不用对比
        for j in range(len(data)-1-i):           #data-1   是指减去一次比较次数  只有最后一个数了，所以不用对比，-i，第一次循环i=0
            if data[j] > data[j+1]:              #j代表的是下标  ，data【j】第一次是指 0位list
                data[j], data[j+1] = data[j+1], data[j]
        print(data)
    return data
print(maopao(data))

# data = [99,55,44,11,77,66,88,33,22]
# for i in range(len(data) - 1):
#     for j in range(len(data) - 1 - i):
#         if data[j] > data[j + 1]:
#             data[j], data[j + 1] = data[j + 1], data[j]
#     print(data)

data.sort()
