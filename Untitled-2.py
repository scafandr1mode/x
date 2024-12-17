# lst = [i for i in range(1, 10)]
# print(lst)

# lst = [i for i in range(1,6)]
# print(lst)

# lst = [i for i in range(1,6)]
# lst.sort(reverse=True)
# print(lst)

#2
# lst = [i + 2 for i in range(0, 6)]
# print(lst)

# lst = [i / 2 for i in range(4, 10)]
# print(lst)

# lst = [i + 10 for i in range(0, 8, 2)]
# print(lst)



#3
# lst = [1, 2, 3, 4, 5]
# lst = [i **2 for i in [1,2,3,4,5]]
# print(lst)

# lst = [1, 3, 5, 7, 9]
# lst = [i *3 for i in [1, 3, 5, 7, 9]]
# print(lst)

#4
# lst = [i for i in [1, 3, 5, 7, 9] if i % 2 != 0]
# print(lst)

# lst = [-6, -3, -1, 0, 2, 4]
# lst = [i for i in [-6, -3, -1, 0, 2, 4] if i>=0]
# print(lst)

#4
# lst1 = ['1', '2']
# lst2 = ['a', 'b', 'c']
# lst = [(i, j) for i in ['1', '2'] for j in ['a', 'b', 'c']]
# print(lst)

#5
# lst = [(i, j) for i in range(0, 5) for j in range(0, 5) if j == i]
# print(lst)

# lst = [(i, j) for i in range(1, 4) for j in range(1, 4) if i % 2 == 0]
# print(lst)

#6
# lst = [[j for j in range(1, 6)] for i in range(0, 3)]
# print(lst)

# lst = [[j for j in [[1,2,3],[1,2,3],[1,2,3]]] for i in range(0, 3)]
# print(lst)

#7
# lst = ('a', 'b', 'c', 'd', 'e')
# dct = {lst: i for i in range(1, 6)}
# print(dct)

# lst1 = ('name1', 'name2', 'name3', 'name4')
# lst2 = ('john', 'kate', 'alex', 'mary')
# dct = {lst1: i for i in lst2}
# print(dct)

