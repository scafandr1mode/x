from functools import reduce
import datetime
import time
#1
# a = [1,2,3,4,5]
# a.append(6)
# a.remove(3)
# print(a)

#2
# person = {"name":'Alice',"age":30}
# person["city"]='NewYork'
# print(person)


#3
# my_set = {1, 2, 3, 4, 5}
# my_set.add(6)
# print(my_set)

# if 6 in my_set:
#     print('YEs')
# else:
#     print('No')

#4
# my_tuple = (1,2,3)
# my_tuple[0] =4
# print(my_tuple)

#5
# def a(b,c):
#     print(b+c)
# a(1,3)

#6
# def a(b):
#     print(len(b))
# a('DFGSCHVJ')

#7
# def a(b):
#     b = sum(b)/len(b)
#     print(b)
# a([1,2,3,4,5])

#8
# c = []
# def a(b):

#     for i in b:
#         c.append(len(i))
#     print(c)
# a(['asd','asdf','dfsg'])

#9
# a = [1,2,3,4,5]
# c = []
# b = lambda x: x**2,a
# print(b)

#10 
# numbers = [1, 2, 3, 4, 5, 6]
# c = []
# a = filter(lambda x: x%2==0, numbers)
# print(*a)

#11
# numbers = [1, 2, 3, 4, 5]
# a = reduce(lambda x,y: x+y,numbers)
# print(a)

#12
# numbers = [1, 2, 3, 4, 5, 6]
# a =reduce(lambda x,y: x+y ,map(lambda g: g**2,filter(lambda x: x%2==0,numbers )))
# print(a)

#13
# a = [i for i in range(1,10+1)]
# print(a)

#14
# numbers = [1, 2, 3, 4, 5, 6]
# a = [i for i in numbers if i%2==0]
# print(a)

#15
# a = {i: i ** 2 for i in range(1, 5)}
# print(a)

#16
# a = ['h','e','l','l','o']
# b = [ord('h'),ord('e'),ord('l'),ord('l'),ord('o')]
# c = {i: v for i,v in zip(a,b) }
# print(c)

#17
# res = datetime.date.today()
# print(res)


#18
# dt = datetime.date.today()
# res = dt.strftime('%Y-%m-%d')
# print(res)


#19
# a = datetime.datetime.strptime('2024/01/01', '%Y/%m/%d')
# b = datetime.datetime.strptime('2024/01/15', '%Y/%m/%d')

# res = b - a
# print(res)

#20
# dt = datetime.date.today()
# b = dt + datetime.timedelta(days=7)

# print(b)

#21
# a =[1,2,3,4,5]
# b = []
# for i in a:
#     if i%2==0:
#         b.append(i)
# print(b)

#22
# a = {'asd':12,'tr':32}
# a['df']=34
# print(a)

#23
# a = {1,2,3,4}
# b = {5,6,7,8}
# print(a-b)
# print(a+b)

#24
# a = (1,2,3)
# a[0] = 3
# print(a)
#error

#25
# def a(b):
#     print(sum(b)/len(b))
# a([1,2,3,4,5])

#26
# a = int(input())
# b = int(input())
# def j():
#     try:
#         print(a/b)
#     except:
#         ZeroDivisionError
#         print('df')
# j()

#27
#не смог

#28
# a =  [i**2 for i in range(1, 10) ]
# print(a)

#29
# a = [1,2,3,4,5]
# b = {i: i**2 for i in a }
# print(b)

#30
# a = [(5,6),(4,5),(2,1)]

# b = sorted(a, key=lambda x: x[1])
# print(b)
