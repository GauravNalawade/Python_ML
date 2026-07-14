class Numbers:
    def __init__(self,No):
        self.Value=No

    def CheckPrime(self):
        if self.Value<=1:
            return False
        for i in range(2,self.Value):
            if self.Value % i == 0:
                return False
        return True
    
    def CheckPerfect(self):
        Sum=0
        for j in range(1,self.Value):
            if self.Value % j ==0:
                Sum+=j
        if Sum==self.Value:
            return True
        else:
            return False
    
    def Factors(self):
        for f in range(1,self.Value+1):
            if self.Value % f==0:
                print(f)

    def FactorsSum(self):
        SumOfFacors=0
        for k in range(1,self.Value+1):
            if self.Value % k==0:
                SumOfFacors += k
        return SumOfFacors
    
nobj1=Numbers(3)
print("Number  :",nobj1.Value)
print("Prime   : ",nobj1.CheckPrime())
print("Perfect : ",nobj1.CheckPerfect())
print("Factors :")
nobj1.Factors()
Ret1=nobj1.FactorsSum()
print("Sum of Factors is:",Ret1)

nobj2=Numbers(6)
print("Number  :",nobj2.Value)
print("Prime   : ",nobj2.CheckPrime())
print("Perfect : ",nobj2.CheckPerfect())
print("Factors :")
nobj2.Factors()
Ret2=nobj2.FactorsSum()
print("Sum of Factors is:",Ret2)
            
nobj3=Numbers(10)
print("Number  :",nobj3.Value)
print("Prime   : ",nobj3.CheckPrime())
print("Perfect : ",nobj3.CheckPerfect())
print("Factors :")
nobj3.Factors()
Ret3=nobj3.FactorsSum()
print("Sum of Factors is:",Ret3)
    