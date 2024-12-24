from functools import reduce
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
# b = lambda[x: i for i in a c.append(i**2)]

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