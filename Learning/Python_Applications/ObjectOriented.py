class Arithmetic:
    def Addition(No1,No2):
        Ans=No1+No2
        return Ans

    def Substraction(No1,No2):
        Ans=No1-No2
        return Ans

Aobj=Arithmetic()

print("Enter First Number:")
value1=int(input())

print("Enter First Number:")
value2=int(input())

# Ret=Addition (Aobj,Value1,Value2)

Ret=Aobj.Addition(value1,value2)     #Issue/Error
print("Addition is:",Ret)

Ret=Aobj.Substraction(value1,value2)
print("Substraction is:",Ret)
