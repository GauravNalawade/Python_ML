def main():
    print("Enter FileName")
    filename=input()

    try:
        fobj=open(filename,"r")

        # Data=fobj.read()
        # if Data=="":
        #     Count=0
        # else:
        #     Count=1

        # for i in Data:
        #     if i == "\n":
        #         Count+=1

        lines=fobj.readlines()
        Count=len(lines)

        fobj.close()
        
        print(f"Total Number of lines in {filename}:",Count)

    except FileNotFoundError as e:
        print("File Not Present in Current directoty:",e)
        return 0
    

if __name__=="__main__":
    main()