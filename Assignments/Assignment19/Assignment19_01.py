Power=lambda no : no**2

def main():
    print("Enter Number:")
    no=int(input())

    Ret=Power(no)
    print(f"Power of {no} is:",Ret)

if __name__=="__main__":
    main()