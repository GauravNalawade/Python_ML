import threading

def Small(Str1):
    print(f"Inside Small {threading.get_ident()}")
    Count=0
    for char in Str1:
        if char.islower():
            Count=Count+1
    print("Number of LowerCase Character in String:",Count)


def Capital(Str2):
    print(f"Inside Capital {threading.get_ident()}")
    Count=0
    for char in Str2:
        if char.isupper():
            Count=Count+1

    print("Number of UpperCase Character in String:",Count)

def Digit(Str3):
    print(f"Inside Digit {threading.get_ident()}")
    Count=0
    for char in Str3:
        if char.isdigit():
            Count=Count+1
    print("Number of Numeric Digits in String:",Count)

def main():
    print("Inside Main",threading.get_ident())
    print("Enter String")
    Str=input()

    tobj1=threading.Thread(target=Small,args=(Str,))
    tobj2=threading.Thread(target=Capital,args=(Str,))
    tobj3=threading.Thread(target=Digit,args=(Str,))

    tobj1.start()
    tobj2.start()
    tobj3.start()

    tobj1.join()
    tobj2.join()
    tobj3.join()

if __name__=="__main__":
    main()

