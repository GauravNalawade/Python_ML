import os

def main():
    try:
        # fobj.remove()   ->Not Applicable
        os.remove("Demo.txt")

    except FileNotFoundError as fobj:
        print("file is not present in current directory:",fobj)

if __name__=="__main__":
    main() 

