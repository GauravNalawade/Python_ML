def main():
    try:
        fobj=open("Demo.txt","a")
        print("File gets Opened")

        fobj.write(" Pune Maharshtra")

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main() 
