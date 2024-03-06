
print("1 + 2 : ",1 + 2 )
print("'String-' + 'String' : ", "String-" + "String")
print("[1,2,3] + [4,5,6] : ",[1,2,3]+[4,5,6])
print("[1,'Middle1',3] + [4,'Middle2',6] : ",[1,"Middle1",3]+[4,"Middle2",6])
print("(1,2,3) + (4,5,6) : ",(1,2,3)+(4,5,6))
print("(1,'Middle1',3) + (4,'Middle2',6) : ",(1,'Middle1',3)+(4,'Middle2',6))

class NUM :
    def __init__(self, num):
        self.num = num 
    def add(self, num2):
        return NUM(self.num + num2.num ) 
    def __add__(self, num2):
        return NUM(self.num + num2.num)
    def Show(self):
        print(self.num)
    
N1 = NUM(10)
N2 = NUM(20)
N1.Show()
N2.Show()
N3 = N1 + N2
N3.Show()
N4 = N1.add(N2)
N4.Show()
 