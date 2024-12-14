# s = 'Moscow is capital of Russia'
# b = 12345
# print(s.capitalize()) # Меняет регистр больших букв на маленькие , кроме первой
# print(s.casefold()) # делает всеюуквы маленькими
# print(s.center(3,'s'))#добавляет в центр символы
# print(s.count('o'[0:5:]))#считает кол-во заданного элемента вв заданном диапазоне
# print(s.encode(encoding='utf-8'))#кодирует
# s.endswith('s')
# print(s.endswith('s'))#исчет данный префикс
# print(s.expandtabs(5))#добавлят количество табов
# print(s.find('o'))#находит данный элемент
# print(s.format(*'us'))#форматирует данный элемент 
# print(s.index('o'))#выводит индекс данного элемента
# print(s.isalnum())#выводит тру если хотя бы один символ-цифра
# print(s.isalpha())#вернёт тру если хотя бы один символ-буква
# print(s.isascii())#Вернёт тру если хотя бы один символ входит в ASCII или строка пуста
# print(s.isdecimal())#Возвращает True если в строка содержит число в десятичной системе исчисления и в ней есть хотя бы один символ
# print(s.isdigit())#Выводит тру если в строке хотя бы один символ-цифра
# print(s.isidentifier())#Если есть индефикаторы языка, то выводит тру
# print(print(s.islower() ))#Выводит тру если есть хотя бюы один символ в нижнем регистре
# print(s.isnumeric())#Вернёт True, если в строке есть символы и все они принадлежат числам.
# print(s.isspace())#выводит тру если есть пробел в стролке
# print(s.istitle())#Вернёт True, если в строке есть хотя бы один символ и все слова в строке начинаются с заглавных букв.
# print(s.join('is'))#добавляет к строке данный символ
# print(s.lower())#Переводит все символы в строке в нижний регистр
# print(s.strip('a'))#Возвращает копию указанной строки, с обоих концов которой устранены указанные символы.
# s.ljust(1,'g')
# print(s)# Сдвигает влево указанную строку, дополняя её справа до указанной длины указанным символом
# d = s.maketrans('s','f','g')#Возвращает таблицу пакетной замены символов для str.translate().
# print(s.translate(d))#переводит символы указанные в таблицы
# print(s.rpartition('rep'))#Разбивает строку на части и  превращает в кортеж
# print(s.replace('R', 'g'))#заменяет указанную букву на другую
# print(s.rfind('Rus'))#Возвращает наибольший индекс, по которому обнаруживается конец указанной подстроки 
# print(s.rjust(4))#Сдвигает вправо указанную строку, дополняя её слева до указанной длины указанным символом
# print( s.rsplit(('Rus'), maxsplit=12))#Разбивает строку на части, используя разделитель, и возвращает эти части списком
# print(s.split(('Mos'), maxsplit=4))#Разбивает строку на части
# print(s.startwith('ss', start=[-1]))#Возвращает флаг, указывающий на то начинается ли строка с указанного префикса
# print(s.swapcase())#Возвращает копию строки, в которой каждая буква будет иметь противоположный регистр
# print(s.title())#Возвращает копию строки в которой каждое новое слово начинается с заглавной буквы
# print(s.upper())#Переводит все символы в верхний регистр
# print(s.zfill(123))#Изначальная строка не обрезается даже если в ней меньше символов, чем указано в параметре  длины


#`1`
# print('Mama is %s %r' %('cooking','fish'))
# print('The password is %c enter %d'%(1234,1.23))
# print('You made %i jumps'%(123))
# print('The password is %x'%(123456789101123))
# print('The %e' %(1.23))
# print('the %E'%(1.23))
# print('%F'%(1.23))
# print('%f'%(1.34))
# print('%g'%(1.23))
# print('%G'%(1.23))
# print('%%')

#2
# template= '%s %s and %s'
# template&('negr','rabotatn' , 'paxft')
# print(template)
# template = '%{bike} s,%{moto} s and %{food}s'
# template%dict(bike='kayo',moto ='terminator',food = 'benzin')
# print(template)
# x = '{0} , {p} and {f}'.format(42,p=3.13,f=[2,4])
# print(x)
# x.split('and')
# y = x.replace('and','but ubderground')
# print(y)


















# b = []
# a = ['bobr kurwa','ya perdolle','mamaaaaa']
# print(a[0][0],a[1][0],a[2][0])
# for i in a:
#     b += i
# b.remove('b')
# b.insert(0,'B')
# b.remove('y')
# b.insert(10,'Y')
# b.remove('m')
# b.insert(21,'M')
# print(*b)

#1
# print('{0:10} = {1:10}'.format('spamerrrr',123.678))
# print('{0:>10} = {1:<10}'.format('sus',123.234))
# print('{0:10} = {1:10}'.format('gold',154.345))

#2
# a ='''Уважаемый (ая), Иван Иванович!
# Приглашаем Вас на день открытых дверей.
# Дата события: 1 мая.
# С уважением, Василий.
# '''

# b= ''
# for i in a:
#     b +=i
# b = b.split()
# print(b)
# b.remove('Иван')
# b.remove('Иванович!')
# b.remove('день')
# b.remove('открытых')
# b.remove('дверей.')
# b.remove('1')
# b.remove('мая.')
# b.remove('Василий.')

# # b.insert(2,'Илья')
# b.insert(3,'Александрович')
# b.insert(7,'первомайские')
# b.insert(8,'праздники')
# b.insert(14,'3 мая')
# b.insert(16,'Александр')

# b.insert(2,'Кристина')
# b.insert(3,'Сергеевна')
# b.insert(7,'день')
# b.insert(8,'благодарения')
# b.insert(14,'4 мая')
# b.insert(16,'Илья')

# b.insert(2,'Александр')
# b.insert(3,'Евгеньевич')
# b.insert(7,'день')
# b.insert(8,'рождения')
# b.insert(14,'5 мая')
# b.insert(16,'Костя')

# b.insert(2,'Берюлёз')
# b.insert(3,'Васильевич')
# b.insert(7,'новый')
# b.insert(8,'год')
# b.insert(14,'2 мая')
# b.insert(16,'Сергей')

# print(b)