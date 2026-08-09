import pandas as pd

def main():
    Data={
            "Name":["Sagar","Amit","Pooja"],
            "Age":[27,28,25],
            "City":["Pune","Kolhapur","Satar"]
         }
 
    dobj=pd.DataFrame(Data)    

    print(dobj[["Name","Age"]])

if __name__=="__main__":
    main()