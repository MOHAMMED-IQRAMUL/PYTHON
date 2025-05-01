from collections import Counter
"""
This script demonstrates the usage of the `collections.Counter` class to count the occurrences 
of elements in a string and a list.
Modules:
    - collections: Provides specialized container datatypes, including `Counter`.
Functionality:
    1. Counts the frequency of each character in a given string using `Counter`.
    2. Counts the frequency of each element in a given list using `Counter`.
Variables:
    - string (str): A string containing characters whose occurrences are counted.
    - counter (Counter): A Counter object that stores the frequency of each character in the string.
    - list (list): A list of integers whose occurrences are counted.
    - counter2 (Counter): A Counter object that stores the frequency of each element in the list.
Output:
    - Prints the frequency of each character in the string.
    - Prints the frequency of each element in the list.
"""

string = "aaaabbbdicbniopbconcocnoncdoiwinc"
counter = Counter(string)
print(counter)

list = [1,2,3,4,5,6,7,8,9,8,7,6,4,2,1,2,4,6,8,9,0,1,2,3,4,5,6,7,8,9]
counter2 = Counter(list)
print(counter2)