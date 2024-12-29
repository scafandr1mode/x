def fibes(a):
    c, b = 0, 1
    for i in range(a):
        yield c
        c, b = b, c + b

print(list(fibes(10)))