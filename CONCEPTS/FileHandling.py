# File Handling in Python

# Creating a new file and writing content to it
f = open("Demo.txt", "w")
f.write("Hello World")
f.close()

# Opening the file in read mode and printing its content
f = open("Demo.txt", "r")
print(f.read())
f.close()

# Appending additional content to the file
f = open("Demo.txt", "a")
f.write("\nHello World")
f.close()

# Creating a new Python file and writing content to it
f = open("PIPP.py", "w")
f.write("print('Hello World')")
f.close()

# Removing the created Python file using os module
import os
os.remove("PIPP.py")

# Reading and writing content to the file using 'with' statement (automatically closes the file)
with open("Demo.txt", "r+") as f:
    # Reading the content of the file
    print(f.read())
    
    # Writing additional content to the file
    f.write("\nWrite Through Hello World")
    
    # Since the file cursor is at the end, calling read() again won't return anything
    print(f.read())
    
    # Close the file manually (although 'with' statement takes care of this)
    f.close()

# Reading and writing content to the file using 'with' statement with cursor manipulation
with open("Demo.txt", "r+") as f:
    # Reading the content of the file line by line and storing it in 'data'
    data = ""
    check = True
    while check:
        check = f.readline()
        data += check
    print(data)
    
    # Moving the cursor to the 5th position and overwriting the character
    f.seek(5)
    f.write("F1")

# Checking types of file objects and print function
print(type(open("Demo.txt", "r")))
print(type(print("")))
print(print("JIKL"))

# Assigning the return value of print function to variable x
x = print("JIKL")
print(x)
print(type(x))
