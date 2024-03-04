#### ----------- LIST  ------------------------------------

# Creating a list with integers, strings, and mixed data types
list = [1, 2, 3, 4, 5, "HELLO", "WORLD"]

# Printing the entire list
print(list)

# Accessing the first element of the list
print(list[0])

# Accessing the last two elements of the list
print(list[len(list) - 2], list[len(list) - 1])

# Slicing elements from index 2 to index 4 (exclusive)
print(list[2:5])

# Slicing elements starting from index 2 till the end
print(list[2:])

# Slicing elements from the beginning till index 4 (exclusive)
print(list[:5])

# Slicing the last two elements of the list
print(list[-2:])

# Slicing elements from the beginning till the second last element
print(list[:-2])

# Slicing every second element of the list
print(list[::2])

# Slicing every third element of the list
print(list[::3])

# Appending a new element to the end of the list
list.append("APPENDED")
print(list)

# Sorting the list in ascending order
list.sort()
print(list)

# Sorting the list in descending order
list.sort(reverse=True)
print(list)

# Reversing the order of elements in the list
list.reverse()
print(list)

# Modifying an element at index 5
list[5] = "CHANGED"
print(list)

#### ----------- TUPLE ------------------------------------

# Creating a tuple with integers, strings, and mixed data types
tuple = (1, 2, 3, 4, 5, "HELLO", "WORLD")

# Printing the entire tuple
print(tuple)

# Accessing the first element of the tuple
print(tuple[0])

# Accessing the last two elements of the tuple
print(tuple[len(tuple) - 2], tuple[len(tuple) - 1])

# Converting the tuple to a list and removing the last element
list = list(tuple)
list.pop()
print(list)

#### ----------- DICTIONARY  ------------------------------------

# Creating a dictionary with various data types as keys and values
dictionary = {
    "key1": "value1",
    123: 123,
    "key2": 1234,
    1234: "value2"
}

# Printing the entire dictionary
print(dictionary)

# Accessing the value associated with key 'key1'
print(dictionary["key1"])

# Accessing the value associated with key 123
print(dictionary[123])

# Modifying the value associated with key 'key1'
dictionary["key1"] = 4456
print(dictionary["key1"])

#### ----------- NESTED DICTIONARY  ------------------------------------

# Creating a dictionary with nested dictionaries and lists
std = {
    "name": "python",
    "version": 3.2,
    "author": "Guido van Rossum",
    "uses": {
        "libraries": ["turtle", "stat"],
        "web": ("django", "flask"),
    },
    2468: 8642
}

# Printing the entire dictionary
print(std)

# Extracting keys and nested keys from the dictionary
Keys = list(std.keys())
keyskey = list(std["uses"].keys())
print(Keys)
print(std[Keys[0]])
print(std["uses"]["libraries"])

# Creating a list containing a nested dictionary and accessing its elements
list = [{"A": "A", "B": "B"}]
print(list)
print(list[0]["A"])

#### ----------- SET  ------------------------------------

# Creating a set with integers
set = {1, 2, 3, 4, 5}
print(set)

# Removing element 5 from the set
print(set.remove(5))
print(set)

# Attempting to add a tuple to the set (uncomment this line to test)
# set.add((1, 2, 3, 4))

# Removing and returning an arbitrary element from the set
print(set.pop())

