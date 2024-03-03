#---          WHILE LOOPS          ---#

# Basic while loop
i = 0 
while i < 5:
    print(i)
    i += 1  

# Another while loop with conditions
i = 0 
while i <= 5:
    i += 1
    if i == 3:
        continue  # Skip printing 3
    elif i == 5:
        break  # Exit the loop if i equals 5
    else:
        print(i)

# Input elements into a list using a while loop
print("ENTER 5 ELE")
list = [0,1,2,3,4]
i = 0 
while i < 5:
    list[i] = input("ENTER ")
    i += 1
i = 0 
while i < 5:
    print(list[i]," ")
    i += 1

#---          FOR LOOPS          ---#

# Basic for loop iterating over a list
list = [1,2,3,4,6,7,8,9]
for i in list:
    print(i)
else:
    print(" END ")

# Using the range function in a for loop
for i in range(10):
    if i == 5:
        print("FOUND")
        break
else:
    print("NOT FOUND")

# Enumerate function in a for loop
li = range(5)
print(li,"  ",type(li))

for i in range(5):
    print(i)

# Nested loops to print a pattern
str = ""
for i in range(5):
    for j in range(i+1):
        str += "*"
    print(str)
    str = ""

# Using enumerate to get both index and value from a list
list = [1,2,3,4,5]
for i,num in enumerate(list):
    print("num " , num , end = "  -  ")
    print(f"list[{i}] : {list[i]} " , end = "  -  ")
    print("i : " , i)

# Using start parameter in enumerate
print()
for i,num in enumerate(list,start=1):
    print("num " , num , end = "  -  ")
    print(f"list[{i}] : {list[i-1]} " , end = "  -  ")
    print("i : " , i)
