def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets Opened")

        print("File Offset is:",fobj.tell())  # 0
        Data=fobj.read(10)
        
        print(Data)
        print("File Offset is:",fobj.tell()) # 10
 
        Data=fobj.read(10)
        
        print(Data)
        print("File Offset is:",fobj.tell())
        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main() 
