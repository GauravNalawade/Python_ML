no=11                       #Global Variable
def Display():
    a=21
    print("From Display: ",no)
    print("From Display value of a is: ",a)     #Local Variable 

def Demo():
    print("From Demo: ",no)
    print("From Demo value of a is:",a)          #Error


Display()
Demo()
 