```python
print(10/3)
```
This prints the result of dividing 10 by 3, which is a floating-point division. The output is:
```
3.3333333333333335
```
---
```python
print(int(10/3))
```
Here, `int()` converts the result of 10/3 to an integer by truncating the fractional part. The output is:
```
3
```
---
```python
print(10//3)
```
This uses the floor division operator `//`, which divides and rounds down to the nearest integer. The output is:
```
3
```
---
```python
print((4-2) or (4/2))
```
This evaluates the expression `(4-2)` which is `2`. Since `2` is considered as True in Python, the `or` statement returns `2`. So, it doesn't evaluate `(4/2)`. The output is:
```
2
```
---
```python
print(type((4-2) or (4/2)))
```
This prints the type of the expression `(4-2) or (4/2)`, which is an integer. The output is:
```
<class 'int'>
```
---
```python
print((4-2) and (4/2))
```
This evaluates the expression `(4-2)` which is `2`, and also evaluates `(4/2)` which is `2.0`. Since both are considered as True in Python, the `and` statement returns the second operand. The output is:
```
2.0
```
---
```python
print(type((4-2) and (4/2)))
```
This prints the type of the expression `(4-2) and (4/2)`, which is a float. The output is:
```
<class 'float'>
```
---
```python
print(type(1+2))
print(type(1-2))
print(type(1/2))
print(type(1*2))
print(type(1 or 2))
print(type(1 and (2/2)))
```
The result of the operation determines the type:

- Addition, subtraction, multiplication, and division of integers result in a float when involving division.
- The `or` and `and` operations return one of the operands, and thus the type depends on the operands involved. If any of the operands is a float, the result will be a float.
  
The output of these lines are:
```
<class 'int'>
<class 'int'>
<class 'float'>
<class 'int'>
<class 'int'>
<class 'float'>
```