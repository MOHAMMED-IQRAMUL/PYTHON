# Generators and Function Caching

# Importing time module for measuring execution time
import time as t
from functools import lru_cache

# Defining a generator function
def myGenerator():
    for i in range(5):
        yield i
        
# Measuring the execution time of generator function
i1 = t.time()
gen = myGenerator()
for i in gen:
    print(i)
O1 = t.time() - i1

# Measuring the execution time of a regular loop
i2 = t.time()   
for i in range(5):
    print(i)    
O2 = t.time() - i2

# Measuring the execution time of a while loop
i3 = t.time()
p = 0 
while p < 5:
    print(p)
    p += 1
O3 = t.time() - i3

# Comparing execution times of generator, loop, and while loop
print("O1 ", O1)
print("O2 ", O2)
print("O3 ", O3)

# Defining a function with caching using lru_cache decorator
@lru_cache(maxsize=None)
def myFunc(n):
    return n**5

# Measuring the execution time of the cached function
ti1 = t.time()
print("myFunc(5): ", myFunc(50), end=" -- ")
print(t.time() - ti1)

ti1 = t.time()
print("myFunc(6): ", myFunc(60), end=" -- ")
print(t.time() - ti1)

ti1 = t.time()
print("myFunc(7): ", myFunc(70), end=" -- ")
print(t.time() - ti1)

# Repeating the same function calls to observe the caching effect
ti1 = t.time()
print("myFunc(5): ", myFunc(50), end=" -- ")
print(t.time() - ti1)

ti1 = t.time()
print("myFunc(6): ", myFunc(60), end=" -- ")
print(t.time() - ti1)

ti1 = t.time()
print("myFunc(7): ", myFunc(70), end=" -- ")
print(t.time() - ti1)
