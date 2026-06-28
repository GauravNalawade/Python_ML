from functools import reduce

CheckEven=lambda No:(No % 2 ==0)

Increment= lambda No:No+1

Addition=lambda No1,No2:No1+No2

def main():
    Data=[13,12,8,10,11,20]

    print("Input Data is : ",Data)

    FData=list(filter(CheckEven,Data))
    print("Data After Filter: ",FData)


    MData=list(map(Increment,FData))
    print("Data After Mapped: ",MData)

    RData=reduce(Addition,MData)
    print("Data After Reduced: ",RData)

if __name__=="__main__":
    main()