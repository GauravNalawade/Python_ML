def main():
    print("Enter FileName")
    filename=input()

    try:
        fobj=open(filename,"r")

        lines=fobj.readlines()
        Count=len(lines)

        fobj.close()
        
        print(f"Total Number of lines in {filename}:",Count)

    except FileNotFoundError as e:
        print("File Not Present in Current directoty:",e)
    

if __name__=="__main__":
    main()