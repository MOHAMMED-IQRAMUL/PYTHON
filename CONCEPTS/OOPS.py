class Class:
    var12 = "class "
    
    def __init__(self, var1, var2):
        self.var1 = var1
        self.var2 = var2
        print("Initializing...")
        
    def method1(self):
        print("Method 1")
        print(self.var1)
        print(self.var2)
        
    @staticmethod
    def staticmethod():
        print("Static method")
        
C1 = Class(1, 2)
C1.method1()  # Invoking method1
C1.var1 = 3
C1.var2 = 4
C1.method1()  # Invoking method1 after modifying var1 and var2
C1.staticmethod()  # Invoking staticmethod
print(C1.var12)  # Accessing class variable var12

class Check:
    __Privateclass = "Class"
    
    def __init__(self, D):
        print("Initializing...")
        self.__D = D
        print("Initialized...")
        
    def Accecssor(self):
        print(self.__Privateclass)
        print(self.__D)
        print(Check.__Privateclass)
        
    @classmethod
    def ClassMethod(cls):
        cls.__Privateclass = "CHANGED CLASS"
        
    @property 
    def Dpp(self):
        return self.__D + " DPP"
    
    @Dpp.setter
    def Dpp(self, D):
        self.__D = D

c = Check(100)
c.Accecssor()  # Invoking Accecssor method
c.ClassMethod()  # Invoking ClassMethod
c.Accecssor()  # Invoking Accecssor method after changing __Privateclass
print(c.Dpp)  # Accessing Dpp property
c.Dpp = "New Value"  # Setting value using Dpp property
print(c.Dpp)  # Accessing Dpp property after changing its value

class B1:
    B1 = "B1"
    
    def __init__(self, b):
        print("B1")
        self.b1 = b

class B2:
    B2 = "B2"
    
    def __init__(self, b):
        print("B2")
        self.b2 = b

class D1(B1):
    D1 = "D1"
    
    def __init__(self, d, b):
        print("D1")
        self.d1 = d
        super().__init__(b)

class D2(D1):
    D2 = "D2"
    
    def __init__(self, d, b, c):
        print("D2")
        self.d2 = d
        super().__init__(b)

class D3(D2):
    D3 = "D3"
    
    def __init__(self, d, b, c, e):
        print("D3")
        self.d3 = d
        super().__init__(b, c, e)  
    
    def Print(self):
        print("d3:", self.d3, " d2:", self.d2, " d1:", self.d1, " b1:", self.b1) 

B11 = B1(10)
B22 = B2(20)
D11 = D1(30, 40)
D22 = D2(50, 60, 80)
D33 = D3(70, 80, 90, 100)
D33.Print()
