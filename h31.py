import datetime
import calendar
#1
# res = datetime.date(2025, 12, 31)
# print(res)
# print(res.year)
# print(res.day)
# print(res.month)

#2
# res = datetime.date.today()
# print(res)
# print(res.month)
# print(res.year)

#3
# res = datetime.date(2025, 12, 31)
# print(res.weekday())
# if res in [0,1,2,3,4]:
#     print('yes')
# else:
#     print('no')
# res = datetime.date(2026-11-2)
# print(res.weekday())
# print(res.isoweekday())

#4
# start_time = datetime.datetime.strptime('13/10/2018 22:15:45', '%d/%m/%Y %H:%M:%S')
# end_time = datetime.datetime.strptime('15/11/2018 09:47:16', '%d/%m/%Y %H:%M:%S')
# res = end_time - start_time
# print(res)

# start_time = datetime.datetime.strptime('01-12-2025 16:07:5', '%d/%m/%Y %H:%M:%S')
# end_time = datetime.datetime.strptime('31:12:2025 10:32:45', '%d/%m/%Y %H:%M:%S')
# res = end_time - start_time
# print(res)

#5
# res = calendar.isleap(2020)
# print(res)
# res = calendar.isleap(1910)
# print(res)
# res = calendar.isleap(2024)
# print(res)

#6
# res = datetime.datetime.now()
# print(res.hour)
# print(res.minute)
# print(res.second)

# res = datetime.datetime.now()
# print(res)

#7
# dt = datetime.datetime(2025, 12, 31, 12, 59, 59)
# res = dt.strftime('%Y-%m-%d')
# print(res)
# res = datetime.datetime.now()
# print(res.hour)
# print(res.minute)
# print(res.second)
# print(res.year)
# print(res.month)
# print(res.day)
# print(res.weekday())

#8
# res = time.time()
# print(res)

#9
# dt = time.time()
# res = time.ctime(dt)

# print(res)

#10
# now = time.time()
# res = time.localtime(now)

# print(res.tm_mday)
# print(res.tm_hour)
# dt = 1602314100.0
# res = time.localtime(dt)
# print(res)

#11
# now = time.time()
# res = time.gmtime(now)

# print(res.tm_hour,res.tm_min)

#12
# dt = time.strptime('24/07/2015 16:01','%d/%m/%Y %H:%M')
# now = time.time()
# dt_epoch = time.mktime(dt)
# res = now - dt_epoch
# print(res)
# dt1 = time.strptime('12/02/23 10:12:54','%a %b %d %H:%M:%S %Y')
# dt2 = time.strptime('31/12/24 19:38:21','%a %b %d %H:%M:%S %Y')
# dt_epoch = time.mktime(dt2)
# dt_epochs = time.mktime(dt1)
# res = dt_epoch - dt_epochs
# res = res/180
# print(res)


#13
# time.sleep(5)
# print('Ilia')
# lst = ['a', 'b', 'c', 'd']
# for i in lst:
#     print(i)
#     time.sleep(3)

#14
# a = []
# for i in range(10+1):
#     a.append(i**2)
# print(a)

#13
# a = []
# for i in range(2,10+1):
#     a.append(i**2)
# print(a)

#14
# a = ['sa','fd','st']
# b = []
# for i in a:
#     b.append(i.upper())
# print(b)

#15
# a = ['sa','fd','st']
# b = []
# for i in a:
#     b.append(len(i))
# print(b)

#16
# a = []
# for i in range(10+1):
#     a.append(i**2)
# print(a)

#17
# a = []
# for i in range(1,5+1):
#     a.append('(')
#     a.append(i)
#     a.append(i**2)
#     a.append(')')

# print(a)

#18
# a = [1,2,3,-1]
# b = []
# for i in a:
#     if i >0:
#         b.append(i)
# print(b)

#19
# b = []
# for i in range(5):
#     a = input()
#     if len(a) > 3:
#         b.append(a)
# print(b)

#20
# a = [1,2,3,4,5,6,7,1,2]
# c = []
# for i in a:
#     if i in c:
#         continue
#     c.append(i)
# print(c)

#21
# a =[1,2,3,4,5]
# b = []
# for i in a:
#     if i %2!=0:
#         b.append(i)
# print(b)

#22
# a =[1,2,3,4,5,-1,-2,-4,0]
# b = []
# for i in a:
#     if i >0:
#         b.append(i)
# print(b)

#23
# b = []
# for i in range(5):
#     a = input()
#     if len(a)>=5:
#         b.append(a)
# print(b)

#24
# a = [1,2,3,4,5]
# b =[]
# for i in a:
#     if i %2==0:
#         b.append(i**2)
# print(b)

#25
# a = [1,2,3,4,5]
# b = []
# for i in a:
#     if i >0:
#         b.append(i**3)
# print(b)

#26
# b = []
# for i in range(5):
#     a = input()
#     if a.startswith('p')==True and len(a) >5:
#         b.append(i)
# print(b)

#27
# a=[3,6,9,12,15,18]
# b = []
# for i in a:
#     if i %2!=0:
#         b.append(i)
# print(i)

#28
# a = [1,2,3,4,5]
# b = [6,7,8,9]
# v = []

# for i in a:
#     for j in b:
#         v.append(i)
#         v.append(j)

# print(v)

#29
# a = 'dfagsjshdkl'
# b='dfdgash'
# v = []

# for i in a:
#     for j in b:
#         v.append(i)
#         v.append(j)

# print(v)

#30
# a = [1,2,3,4,5]
# b = [1,2,3,4,5]
# v = []

# for i in a:
#     for j in b:
#         if i+j >5:
#             v.append(i)
#             v.append(j)

# print(v)

#31
# a = 'dfagsjshdkl'
# b='dfdgashyoui'
# v = []
# c = ['a','e','i','o','u','y']
# for i in a:
#     for j in b:
#         if i.lower() in c and j.lower() in c:
#             v.append(i)
#             v.append(j)

# print(v)

#32
# a = [1,2,3,4,5]
# b = [1,4,9,16,25]
# c = dict(zip(a,b))
# print(c)

#33
# a = [1,2,3,4,5]
# b = ['a','b','c','d','e']
# c = dict(zip(a,b))
# print(c)

#34
# a =  []
# for i in range(3):
#     a.append([0,0,0])
# print(a)

#35
a = []
for i in range(1,20+1):
    for j in range(1,5+1):
        i = i+'\n'
        a.append(i)
print(a)