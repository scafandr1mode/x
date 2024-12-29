c = [1,2,3,4,5]
def a(b):
    c.append(b)
    c.remove(b)
    print(c)
a('as')