def Addition(No1,No2):
    Ans=No1+No2
    return Ans

def Substraction(No1,No2):
    Ans=No1-No2 
    return Ans

print("Enter First Number:")
value1=int(input())

print("Enter First Number:")
value2=int(input())

Ret=Addition(value1,value2)
print("Addition is:",Ret)

Ret=Substraction(value1,value2)
print("Substraction is:",Ret)
