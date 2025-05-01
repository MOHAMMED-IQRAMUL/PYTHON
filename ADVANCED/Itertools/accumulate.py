from itertools import accumulate
from operator import add, mul


for a in accumulate([1, 2, 3, 4]):
    print(a, end=' ')
print()
    
for a in accumulate([1, 2, 3, 4], add):
    print(a, end=' ')
print()

for a in accumulate([1, 2, 3, 4], add, initial=10):
    print(a, end=' ')
print()
    
for a in accumulate([1, 2, 3, 4], mul):
    print(a, end=' ')
print()