def First10EvenNum():
    Result=[]
    for i in range(1,21):
        if i % 2 == 0:
            Result.append(i)
    return Result

def main():
    Ret=First10EvenNum()
    for i in Ret:
        print(i,end=" ")

if __name__=="__main__":
    main()
