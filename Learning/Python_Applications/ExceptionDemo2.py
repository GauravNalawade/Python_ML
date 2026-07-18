def main():
    Ans=0
    try:
        print("Enter first Number: ")
        No1=int(input())

        print("Enter Second Number: ")
        No2=int(input())    

        Ans=No1/No2

        print("Division is succesfull")
        
    except ZeroDivisionError as zobj:
        print("Exception Occurred due to second operand is zero:",zobj)


    print("Result is: ",Ans)
    
if __name__=="__main__":
    main()




