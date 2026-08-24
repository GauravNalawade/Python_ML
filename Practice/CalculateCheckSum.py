import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer = fobj.read(1000)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1000)

    fobj.close()

    return hobj.hexdigest()
    
def main():
     
     if(CalculateChecksum("Demo4.txt")==CalculateChecksum("Demo1.txt")):
         os.remove("Demo1.txt")


if __name__=="__main__":
    main()