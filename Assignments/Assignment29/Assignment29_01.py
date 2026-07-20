import os

def main():
    print("Enter the FileName that you want to search:")
    FileName=input()

    if(os.path.exists(FileName)):
        print(f"{FileName} is Exist")
    else:
        print(f"{FileName} is Not Present in Current Directory")


if __name__=="__main__":
    main()