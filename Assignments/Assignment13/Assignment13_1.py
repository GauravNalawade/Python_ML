def AreaOfRectangle(len,wid):
    Area=len*wid
    return Area

def main():
    print("Enter length of Rectangle ")
    length=float(input())

    print("Enter width of Rectangle ")
    width=float(input())

    Ret=AreaOfRectangle(length,width)
    print("Area of Rectangle: ",Ret)

if __name__=="__main__":
    main()