import sys

def main():

    if (len(sys.argv) ==2):
        DirectoryName=sys.argv[1]
        print("DirectoryNAme is:",DirectoryName)
    else:
        print("Invalid Number of Arguments")

if __name__=="__main__":
    main()