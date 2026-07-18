# seek (kuthe,kuthun)
# Kuthun:0/1/2

# 0  ->start
# 1  -> Current
# 2  -> End



def main():
    try:
        fobj=open("Demo.txt","r")
        print("File gets Opened")

        Data=fobj.read(5)
        print(Data)

        fobj.seek(10,1)

        Data=fobj.read(5)

        print(Data) 


    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main() 
 