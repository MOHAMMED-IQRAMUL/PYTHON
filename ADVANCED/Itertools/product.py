from  itertools import product
a = ['a', 'b', 'c']
b = [1, 2, 3]
c = [True, False]

for a in product(a, b, c):
    print(a)