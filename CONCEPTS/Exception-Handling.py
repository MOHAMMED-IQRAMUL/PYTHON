# Exception Handling in Python

try:
    # Prompt the user to enter two numbers
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    
    # Attempt to perform division and display the result using an f-string
    print(f"{a} / {b} = {int(a) / int(b)}")
    
except ZeroDivisionError:
    # Handle the ZeroDivisionError if the user attempts to divide by zero
    print("Cannot divide by zero!")
    
except ValueError:
    # Handle the ValueError if the user enters invalid inputs (non-numeric values)
    print("Please enter valid numbers!")
    
except Exception as e:
    # Handle any other unexpected exceptions and display the error message
    print("An error occurred:", e)
    
finally:
    # The finally block is executed regardless of whether an exception occurs or not
    print("Try block ends")

# Display a message indicating the end of the program
print("Program end")

# Prompt the user to enter something and raise a SyntaxWarning if the input is not empty
if True == bool(input("Enter something: ")):
    raise SyntaxWarning("HELLO")
