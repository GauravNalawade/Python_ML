import sys
import os
import hashlib

def CalculateChecksum(FileName):
    fobj=open(FileName,"rb")

    hobj=hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer)>0):
        hobj.update(Buffer)
        Buffer=fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

def FindDuplicate(DirectoryName): 
     Ret=False
     Ret=os.path.exists(DirectoryName) 
     if(Ret==False):
         print("Path is Invalid")
         return

     Ret=os.path.isdir(DirectoryName)
     if(Ret==False):
         print("It is not a directory")
         return
 
     Duplicate={}
      
     for FolderName,SubFolder,FileNaem in os.walk(DirectoryName):
         for fname in FileNaem:
            fname=os.path.join(FolderName,fname)

            CheckSum=CalculateChecksum(fname)
            # print(f"{fname}:{CheckSum}")

            if CheckSum in Duplicate:
                Duplicate[CheckSum].append(fname)
            else:
                Duplicate[CheckSum]=[fname]

     return Duplicate


def DeleteDuplicate(DirectoryName):
    Mydict=FindDuplicate(DirectoryName)

    Result=list(filter(lambda x:len(x)>1,Mydict.values()))

    Count=0
    TotalDeleted=0

    for value in Result:
        for subvalue in value:
           Count=Count+1
           if(Count>1):
            TotalDeleted=TotalDeleted+1
            print("Duplicate Found:",subvalue) 
        Count=0
    print("Total deleted file:",TotalDeleted)

def main():
    
     DeleteDuplicate("Test")

if __name__=="__main__":
    main()