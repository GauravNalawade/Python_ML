def Addition(No1,No2):
    return No1+No2


def main():
    print("Enter First Number:")
    no1=int(input())

    print("Enter Second Number:")
    no2=int(input())

    Ret=Addition(no1,no2)
    print(f"Addition of {no1} and {no2} is :",Ret)


if __name__=="__main__":
    main()