def WordPresent(FileName,SearchString):
    try:
        fobj=open(FileName,"r")
        Data=fobj.read()
        fobj.close()

        word=Data.split()
        
        if SearchString in word:
            print(f"Word {SearchString} found in file {FileName}")
        else:
            print(f"Word {SearchString} is Not found in file {FileName}")

    except FileNotFoundError as e:
        print("File Not Present in Current directoty:",e)
        return 0

def main():
    print("Enter FileName")
    filename=input()

    print("Enter Word that you want to search")
    searchstring=input()

    WordPresent(filename,searchstring)

if __name__=="__main__":
    main()