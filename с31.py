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

