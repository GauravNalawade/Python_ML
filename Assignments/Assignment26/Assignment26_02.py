class Circle:
    PI=3.14

    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0

    def Accept(self,r):
        self.Radius=r
    
    def CalculateArea(self):
        self.Area=Circle.PI*self.Radius*self.Radius

    def CalculateCircumference(self):
        self.Circumference=2*Circle.PI*self.Radius

    def Display(self):
        print("Radius :",self.Radius)
        print("Area :",self.Area)
        print("Circumference :",self.Circumference)

Cobj1=Circle()
Cobj2=Circle()
Cobj3=Circle()
Cobj4=Circle()

Cobj1.Accept(10)
Cobj1.CalculateArea()
Cobj1.CalculateCircumference()
Cobj1.Display()

Cobj2.Accept(20)
Cobj2.CalculateArea()
Cobj2.CalculateCircumference()
Cobj2.Display()

Cobj3.Accept(30)
Cobj3.CalculateArea()
Cobj3.CalculateCircumference()
Cobj3.Display()

Cobj4.Accept(40)
Cobj4.CalculateArea()
Cobj4.CalculateCircumference()
Cobj4.Display()

