class Arithmetic:

    def __init__(self):
        self.Value1=0
        self.Value2=0

    def Accept(self,v1,v2):
        self.Value1=v1
        self.Value2=v2

    def Addition(self):
        return self.Value1+self.Value2

    def Subtraction(self):
        return self.Value1-self.Value2
    
    def Multiplication(self):
        return self.Value1*self.Value2
    
    def Division(self):
        try:
            return self.Value1/self.Value2
        except ZeroDivisionError as zobj:
            print("Exception occurred due to second operand is zero:",zobj)
    
aobj1=Arithmetic()
aobj2=Arithmetic()

aobj1.Accept(10,5)

Ret=aobj1.Addition()
print("Addition is:",Ret)
Ret2=aobj1.Subtraction()
print("Subtraction is:",Ret2)
Ret3=aobj1.Multiplication()
print("Multiplication is:",Ret3)
Ret4=aobj1.Division()
print("Division is:",Ret4)

aobj2.Accept(50,10)

Ret=aobj2.Addition()
print("Addition is:",Ret)
Ret2=aobj2.Subtraction()
print("Subtraction is:",Ret2)
Ret3=aobj2.Multiplication()
print("Multiplication is:",Ret3)
Ret4=aobj2.Division()
print("Division is:",Ret4)