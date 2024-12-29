
# import module1 #Импортируем весь файл 
# print(module1.f) #Работаем только с переменной F в файле
# # 5

# module1.f = 6 # Присвоение нового значения к переменной F
# print(module1.f)
# # # 6


# from module1 import c
# from module1 import *

# def printer(a):
#     print(a)
# print(c(d = 1,kj=4))


# Изменение объекта в модулях
# from smalls import x,y
# Присвоение нового значения к переменных x,y
# x = 42
# Меняем только значение первого элемента в списке
# y[0]=41
# print(x,y)
# 42 [41,3]


# Работа с модулями и функциями
# Первый способ с помощью from
# from m import func
# func(40)
# # Второй способ с помощью import
# import m
# m.func(22)

# Переименовать функцию 
# from m import func as mfunc 
# mfunc(40)

# Перезагрузка модулей после каких-то изменений
import m
# Подключение модуля обязательно
from importlib import reload;
reload(m) 