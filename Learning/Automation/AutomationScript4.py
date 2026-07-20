import sys

def main():

    if (len(sys.argv) ==2):
        if (sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script is used to travel the directory")
            print("for better usage please check --u flag")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Please execute the script as")
            print("Python FileName.py DirectoryName")
            print("Directory Name should be Absolute path")
        else:
            DirectoryName=sys.argv[1]
            print("DirectoryNAme is:",DirectoryName)
    else:
        print("Invalid Number of Arguments")
        print("Please use --h or --u for more information")

if __name__=="__main__":
    main()