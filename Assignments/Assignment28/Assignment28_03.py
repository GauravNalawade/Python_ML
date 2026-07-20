def main():
    print("Enter FileName that you want to read")
    FileName=input()

    try:
        fobj=open(FileName,"r")
  
        Data=fobj.read()
        print(Data)

        fobj.close()

    except FileNotFoundError as e:
        print("file is not present in current directory:",e)


if __name__=="__main__":
    main()