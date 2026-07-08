Power=lambda No : 2**No

def main():
    print("Enter Number:")
    value=int(input())

    Ret=Power(value)
    print(f"Power of {value} is:",Ret)

if __name__=="__main__":
    main()