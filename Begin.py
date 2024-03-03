# This is a simple Python script demonstrating basic operations and concepts

# Printing "HELLO World" using concatenation
print("HELLO "+"World")

# Printing "HELLO World" using comma separator
print("HELLO ","World")

# Declaring variables
name = "IQRAMUL"
age = 19
cgpa = 9.3
scgpa = cgpa
scgpa -= 0.1

# Printing variables with labels
print("Name: ", name, "\nAge: ", age, "\nCGPA: ", cgpa, "\nSCGPA: ", scgpa ,"\nCGPA: ",cgpa)

# Demonstrating different ways of declaring strings
String1 = 'String1'
String2 = "String1"
String3 = '''String3'''
String4 = "'String4'"
String5 = '"String5"'
String6 = """String6--"""

# Printing strings along with their types
print("String1", String1)
print("String2", String2)
print("String3", String3)
print("String4", String4)
print("String5", String5)
print("String6", String6)
print("type(String1) : ", type(String1) )
print("type(String2) : ", type(String2) )
print("type(String3) : ", type(String3)  )
print("type(String4) : ", type(String4))
print("type(String5) : ", type(String5)  )
print("type(String6) : ", type(String6)  )

# Taking user input and printing it
Text = input("Enter Your Text: ")
print("Text : ",Text)

# Demonstrating string slicing and methods
Str = "hello World"
print(Str[0])
print(Str[0:5])
print(Str[:5])
print(Str[6:])
print(Str[6:len(Str)])
print(Str[-5: -1])
print(Str.capitalize())
print(Str.upper())
print(Str.lower())  
print(len(Str))

# Demonstrating if-elif-else statements
num = 7
if(num % 2 == 0):
    print("DIVISIBLE BY 2")
elif(num % 3 == 0):
    print("DIVISIBLE BY 3")
elif(num % 5 == 0):
    print("DIVISIBLE BY 5")
else:
    print("NOT DIVISIBLE BY 2, 3, 5")

# Demonstrating conditional expression
print(" 1 > 2 ") if 1 > 2 else print(" 1 !> 2 ")
print(" 1 < 2 ") if 1 < 2 else print(" 1 !< 2 ")
print()
print(" 1 > 2 ") if 1 > 2 else print(" 1 !> 2 F 2 > 3 ") if 2 > 3 else print(" 2 !> 3 ")
print(" 1 > 2 ") if 1 > 2 else print(" 1 !> 2 F 2 < 3 ") if 2 < 3 else print(" 2 !< 3 ")
print(" 1 < 2 ") if 1 < 2 else print(" 1 !< 2 F 2 < 3 ") if 2 < 3 else print(" 2 !< 3 ")
print(" 1 < 2 ") if 1 < 2 else print(" 1 !< 2 F 2 > 3 ") if 2 > 3 else print(" 2 !> 3 ")
