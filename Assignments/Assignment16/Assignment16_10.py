def DisplayLen(Name):
    return len(Name)

def main():
    print("Enter String:")
    name=input()

    Ret=DisplayLen(name)
    print("Length:",Ret)

if __name__=="__main__":
    main() 