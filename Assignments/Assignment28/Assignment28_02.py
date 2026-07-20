def main():
    print("Enter FileName")
    filename=input()

    try:
        fobj=open(filename,"r")

        Data=fobj.read()

        Words=Data.split()
        Count=len(Words)

        fobj.close()
        
        print(f"Total Number of words in {filename}:",Count)

    except FileNotFoundError as e:
        print("File Not Present in Current directoty:",e)
        return 0
    

if __name__=="__main__":
    main()