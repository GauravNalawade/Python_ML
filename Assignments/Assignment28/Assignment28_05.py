def CountFrequency(FileName,SearchString):
    try:
        fobj=open(FileName,"r")
        Data=fobj.read()
        fobj.close()

        Count=Data.count(SearchString)
        return Count

    except FileNotFoundError as e:
        print("File Not Present in Current directoty:",e)
        return 0

def main():
    print("Enter FileName")
    filename=input()

    print("Enter String that you want to search")
    searchstring=input()

    Ret=CountFrequency(filename,searchstring)
    print(f"How many times {searchstring} appears in {filename}:",Ret)
    

if __name__=="__main__":
    main()