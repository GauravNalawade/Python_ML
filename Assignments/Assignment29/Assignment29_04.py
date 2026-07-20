import sys

def main():
        
        try:
            FileName1=(sys.argv[1])
            FileName2=(sys.argv[2])

            fobj1=open(FileName1,"r")
            fobj2=open(FileName2,"r")

            Data1=fobj1.read()
            Data2=fobj2.read()

            if(Data1==Data2):
                 print("Both file Contains Same Data: Success")
            else:
                 print("Both file do Not Contains Same Data: Failure")
                 
            fobj1.close()
            fobj2.close()

        except FileNotFoundError as e:
             print("file is not present in current directory:",e)

        except IndexError as iobj:
             print("Usage:python Assignment29_04.py <file1> <file2>:",iobj)

if __name__=="__main__":
    main()


