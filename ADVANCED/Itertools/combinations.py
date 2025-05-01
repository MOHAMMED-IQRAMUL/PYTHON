from itertools import combinations

for a in combinations('abc', 2):
    print(a)
    
from itertools import combinations_with_replacement

for a in combinations_with_replacement('abc', 2):
    print(a)
    
    