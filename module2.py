from module1 import sum_num
print(sum_num(1,3))
from module1 import mult
print(mult(2,4))
print(mult(10,10))
def fac():
    n = 5

    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    print(factorial)
def ch():
    if 10%2==0:
        print(True)
    else:
        print(False)
ch()
def r():
    print('Hello'+' world')
r()
def t():
    print(len('Anna'))
t()
def y():
    print('Anna'.upper())
y()
def cont(string):
    substr = 'nn'
    if substr in  string:
        print(True)
    else:
        print(False)
cont('Anna')