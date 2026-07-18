def main():
    try:
        open("Demo.txt","r")
        print("File gets Opened")

    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main()