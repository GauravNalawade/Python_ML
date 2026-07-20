import sys

def main():
     print("Enter Existing FileName:")
     existingFile=input()

     print("Enter Destination FileName:")
     destinationFile=input()

     try:
          fobj1=open(existingFile,"r")
          fobj2=open(destinationFile,"w")

          Data1=fobj1.read() 
          fobj2.write(Data1) 
                 
          fobj1.close()
          fobj2.close()

     except FileNotFoundError as e:
             print("file is not present in current directory:",e)

if __name__=="__main__":
    main()


