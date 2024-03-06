# Defining a list representing a 3x3 matrix
list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(list)
print()

# Printing each row of the matrix
for I in list:
    print(I)
print()

# Printing each element of the matrix
for I in list:
    for J in I:
        print(J, end=" ")
    else:
        print()
print()

# Printing each element of the matrix with a new line after each row
for I in list:
    for J in I:
        print(J, end=" ")
    print()

print()

# Taking user input to create a matrix
mat = []
for I in range(3):  
    rat = []
    for J in range(3):
       print(I+1, J+1, end=" : ")   
       rat.append(int(input()))
    else:
        mat.append(rat)

print(mat)
    
# Defining a Matrix class
class Matrix:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.mat = []
    def Matrix(self):
        for I in range(self.row):
            rat = []
            for J in range(self.col):
                print(I+1, J+1, end=" : ")
                rat.append(int(input()))
            else:
                self.mat.append(rat)
    def Show(self):
        for I in self.mat:
            for J in I:
                print(J, end=" ")
            print()
    
# Creating instances of the Matrix class
M1 = Matrix(3, 3)
M2 = Matrix(3, 3)

print("Matrix 1 : ")
M1.Matrix()
print()

print("Matrix 2 : ")
M2.Matrix()
print()

print("Matrix 1 : ")
M1.Show()
print()

print("Matrix 2 : ")
M2.Show()
print()
