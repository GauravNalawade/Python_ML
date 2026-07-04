def DisplayPattern(No):
    for i in range(No,0,-1):
        for j in range(i):
            print("*",end=" ")
        print()
                    
def main():
        print("Enter Number:")
        no=int(input())

        DisplayPattern(no)
        
if __name__=="__main__":
        main()
                        
                

