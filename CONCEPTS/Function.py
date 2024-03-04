# Function to calculate the sum of two numbers
def Sum(a, b):
    return a + b

# Example of calling the Sum function
print(Sum(2, 3))

# Function to print "Hello"
def Print():
    print("Hello")

# Example of calling the Print function
Print()

# Various print statements demonstrating different usage
print("Hello", "World")
print("Hello", "World", sep="-")
print("Hello", end=" ")
print("World")

# Function with default parameter values
def Sum(a, b=20, c=10):
    return a + b + c

# Examples of calling the Sum function with different parameters
print(Sum(30))
print(Sum(30, 20))
print(Sum(30, 20, 10))
print(Sum(c=10, a=30))
print(Sum(b=20, a=30))
print(Sum(c=10, b=20, a=30))

# Recursive function to calculate factorial
def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# Example of calling the fact function
print(fact(5))

# Function with variable-length arguments (*args)
def args(*tup):
    print(tup)
    print(type(tup))
    for i in tup:
        print(i, end=" ")
    else:
        print()

# Examples of calling the args function with different arguments
args(1,2,3,4,5,6,7,8,9,10)
args("HELLO","WORLD","PYTHON")
tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
args(*tuple)
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
args(*list)
dict = {"a": 10, "b": 20, "c": 30, "d": 40}
args(*dict)
args(tuple, list, dict)

# Function with variable-length keyword arguments (**kwargs)
def kwargs(**kwargs):
    print(kwargs)
    print(type(kwargs))
    for i in kwargs:
        print(i, kwargs[i],end=" ")
    else:
        print()

# Examples of calling the kwargs function with different keyword arguments
kwargs(a=10, b=20, c=30, d=40)
dict = {"a": 10, "b": 20, "c": 30, "d": 40}
kwargs(**dict)

# Lambda function to calculate the sum of two numbers
Sum = lambda a, b: a + b
print(Sum(2, 3))

# Function to apply a function to a value
def Fn(fx, vl):
    return fx(vl)

# Example of calling the Fn function with a lambda function
print(Fn(lambda a: a*2, 2))

# Decorator function to add a border around another function's output
def decorator1(fx):
    print("******************")
    fx()
    print("******************")

# Decorator function with a nested wrapper function
def decorator2(fx):
    def wrap():
        print("******************")
        fx()
        print("******************")
    return wrap

# Function decorated with decorator1
@decorator1
def Show1():
    print("Hello")

# Function decorated with decorator2
@decorator2
def Show2():
    print("Hello")

# Example of calling Show2, which is decorated with decorator2
Show2()

# Decorator function with a nested wrapper function
def decorator3(fx):
    def wrap():
        print("******************")
        fx()
        print("******************")
    return wrap   

# Function without decorator syntax, manually decorated
def Show3():
    print("Hello")

# Example of calling Show3, which is manually decorated with decorator3
decorator3(Show3)()

