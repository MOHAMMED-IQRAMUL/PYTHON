# Using format method with placeholders {} and positional arguments

str = "Hello {} , This is {}"
print(str.format("World", "Python"))  # Output: Hello World , This is Python
print(str.format("Python", "World"))  # Output: Hello Python , This is World
print()

# Using format method with placeholders {} and positional indices

str = "Hello {0} , This is {1}"
print(str.format("World", "Python"))  # Output: Hello World , This is Python
print(str.format("Python", "World"))  # Output: Hello Python , This is World
print()

# Using format method with placeholders {} and positional indices in reverse order

str = "Hello {1} , This is {0}"
print(str.format("World", "Python"))  # Output: Hello Python , This is World
print(str.format("Python", "World"))  # Output: Hello World , This is Python
print()

# Using format method with named placeholders {name} and {course}

str = "Hello {name} , This is {course}"
print(str)  # Output: Hello {name} , This is {course}
print(str.format(name="World", course="Python"))  # Output: Hello World , This is Python
print()

# Using f-string to format strings with variables

name = "World"
course = "Python"
str = f"Hello {name} , This is {course}"
print(str)  # Output: Hello World , This is Python
print()

# Using f-string with line break and escape characters

print(f"Hello {name} , This is {course}", end="\n\n")  # Output: Hello World , This is Python followed by two line breaks

# Using f-string with double curly braces to escape placeholders

print(f"Hello {{name}}, This is {{course}}")  # Output: Hello {name}, This is {course}

# Example function with docstring explaining parameters and return type

def Sum(a, b):
    """
    a: int
    b: int
    return: int
    """
    return a + b

# Example of calling the function and accessing its docstring

print(Sum(2, 3))  # Output: 5
print(Sum.__doc__)  # Output: """
                    # a: int
                    # b: int
                    # return: int
                    # """
