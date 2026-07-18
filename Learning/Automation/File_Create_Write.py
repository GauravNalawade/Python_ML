def main():
    try:
        fobj=open("Demo.txt","w")
        print("File gets Opened")

        fobj.write("Jay Ganesh.....")

        fobj.close()

    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main() 
