class Demo:
    # Class Variables
    Value1=10
    Value2=20

    def __init__(self):
        self.No1=11
        self.No2=21

    # Instace Method
    def fun(self):
        print("Inside Instance Method Named as fun")
        print(self.No1)
        print(self.No2)
        print(Demo.Value1)
        print(Demo.Value2)
    
    @classmethod
    def gun(cls):
        print("Inside Class Method Named as gun")
        # print(Demo.No1)  Not Allowed
        # print(Demo.No2)  Not Allowed
        print(cls.Value1)
        print(cls.Value2)   
    
    @staticmethod
    def sun():
        print("Inside Static Method Named as sun")
        print(Demo.Value1)
        print(Demo.Value2)

Demo.sun()