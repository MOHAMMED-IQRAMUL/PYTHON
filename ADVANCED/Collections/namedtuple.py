from collections import namedtuple
"""
This script demonstrates the usage of the `namedtuple` class from the `collections` module.
Classes:
    Points: A named tuple with fields 'x' and 'y'.
Usage:
    - A named tuple `Points` is created with fields 'x' and 'y'.
    - An instance of `Points` is created with values 10 and 20 for 'x' and 'y', respectively.
    - The values of the fields are accessed using both attribute-style access (`p.x`, `p.y`) 
      and index-style access (`p[0]`, `p[1]`).
Output:
    - Prints the values of 'x' and 'y' using attribute-style access.
    - Prints the values of 'x' and 'y' using index-style access.
"""

test = namedtuple('Points', 'x,y')

p = test(10, 20)
print(p.x, p.y)
print(p[0], p[1])


