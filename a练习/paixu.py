# -*- coding:utf-8 -*-

#    排序代码


# # python插入排序
# def insertSort(a):
#     for i in range(len(a) - 1):
#         # print a,i
#         for j in range(i + 1, len(a)):
#             if a[i] > a[j]:
#                 temp = a[i]
#                 a[i] = a[j]
#                 a[j] = temp
#     return a
#
#
# # Python的冒泡排序
# def bubbleSort(alist):
#     for passnum in range(len(alist) - 1, 0, -1):
#         # print alist,passnum
#         for i in range(passnum):
#             if alist[i] > alist[i + 1]:
#                 temp = alist[i]
#                 alist[i] = alist[i + 1]
#                 alist[i + 1] = temp
#     return alist
#
#
# # Python的选择排序
# def selectionSort(alist):
#     for i in range(len(alist) - 1, 0, -1):
#         maxone = 0
#         for j in range(1, i + 1):
#             if alist[j] > alist[maxone]:
#                 maxone = j
#         temp = alist[i]
#         alist[i] = alist[maxone]
#         alist[maxone] = temp
#     return alist
#
#
# alist = [53, 22, 93, 16, 77, 31, 44, 55, 20]
# print(bubbleSort(alist))
# alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# print(selectionSort(alist))
#



# lis=[1,3,5,9,12,4,65,45,21,79]
# print(lis)
# def bibi(lis):
#     count=len(lis)
#     for i in range(0,count):
#         for j in range(i+1,count):
#             if lis[i]>lis[j]:
#                 lis[i],lis[j] = lis[j],lis[i]
#     return lis
# print(bibi(lis))

#
# lis=[3,5,78,54,21,4,1,98,66,77,33]
# print(lis)
# def haha(lis):
#     like=len(lis)
#     for i in range(like):
#         for j in range(i+1,like):
#             if  lis[i]>lis[j]:
#                 lis[i],lis[j]=lis[j],lis[i]
#         print(lis)
# print(haha(lis))



#
# def bubbleSort(sort_list):
#     list_len = len(sort_list)
#     if list_len < 2:
#         return sort_list
#     for i in range(list_len):
#         for j in range(list_len-i-1):
#             if sort_list[j]>sort_list[j+1]:
#                 sort_list[j],sort_list[j+1] = sort_list[j+1],sort_list[j]
#         print(sort_list)
# print(bubbleSort(sort_list))
# sort_list=[3,5,78,54,21,4,1,98,66,77,33]

# def bubble(l):
#     print(l)
#     for index in range(len(l) - 1, 0, -1):
#         for two_index in range(index):
#             if l[two_index] > l[two_index + 1]:
#                 l[two_index], l[two_index + 1] = l[two_index + 1], l[two_index]
#         print(l)
#     print(l)
#
# l = [60, 40,20, 50, 30, 10]
# bubble(l)

# for i in range(1,10):
#      for j in range(i,10):
#         print("%d*%d=%2d" % (i,j,i*j),end ='')
#      print("")


#递归函数
# def digui(num):
#     print(num)
#     if num>0:
#         digui(num-1)
#     else:
#         print("------")
#     print(num)
#
# digui(3)




















