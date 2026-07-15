import threading

ElemenstSum=0
ElementsProd=0

def SumOfElements(Elements):
    global ElemenstSum
    Sum=0
    for i in Elements:
        Sum+=i
    ElemenstSum=Sum

def ProductOfElements(Elements):
    global ElementsProd
    Product=1
    for i in Elements:
        Product*=i
    ElementsProd=Product

def main():
    Data=[]
    print("Enter the size of list:")
    size=int(input())

    for i in range(size):
        no=int(input())
        Data.append(no)

    tobj1=threading.Thread(target=SumOfElements,args=(Data,))

    tobj2=threading.Thread(target=ProductOfElements,args=(Data,))
      
    tobj1.start()
    tobj2.start()

    tobj1.join()
    tobj2.join()

    print("Sum of Elements in list are:",ElemenstSum)

    print("Product of Elements in list are:",ElementsProd)

if __name__=="__main__":
    main()


