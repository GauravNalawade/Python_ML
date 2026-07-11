class Arithmetic:
    def Addition(self,No1,No2):
        Ans=No1+No2
        return Ans

    def Substraction(self,No1,No2):
        Ans=No1-No2
        return Ans

Aobj=Arithmetic()

print("Enter First Number:")
value1=int(input())

print("Enter First Number:")
value2=int(input())

# Ret=Addition (Aobj,Value1,Value2)
Ret=Aobj.Addition(value1,value2)     
print("Addition is:",Ret)

# Ret=Substraction (Aobj,Value1,Value2)
Ret=Aobj.Substraction(value1,value2) 
print("Substraction is:",Ret)
