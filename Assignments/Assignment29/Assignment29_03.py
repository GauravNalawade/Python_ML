import sys

def main():
        
        try:
            FileName=(sys.argv[1])

            fobjExisting=open(FileName,"r")
            fobjNew=open("Demo.txt","w")

            Data=fobjExisting.read()
            fobjNew.write(Data)

            fobjExisting.close()
            fobjNew.close()

            print(f"Create Demo.txt and copy contents of {FileName} into Demo.txt")

        except FileNotFoundError as fobj:
             print("Source file Does not exist:",fobj)

        except IndexError as iobj:
             print("Usage:python Assignment29_03.py <fileName>:",iobj)

if __name__=="__main__":
    main()


