def AreaOfCircle(rad):
    PI=3.14
    area=PI*rad*rad
    return area

def main():
    print("Enter Rasius of Circle")
    radius=float(input())

    Ret=AreaOfCircle(radius)
    print("Area of Circle: ",Ret)

if __name__=="__main__":
    main()