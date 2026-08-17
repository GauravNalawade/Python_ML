import pandas as pd
import joblib

def LoadModel(FileName):
    model=joblib.load(FileName)

    print("Model Loaded Successfully")

    print(model.feature_names_in_)

    return model

def PredictPassanger(model):
    print("Enter the information")

    Pclass=int(input("Enter Pclass (1/2/3)"))
    Sex=int(input("Enter Sex: (0- M / 1-F)"))
    Age=float(input("Enter Age"))
    sibsp=int(input("Enter sibsp:"))
    Parch=int(input("Enter Parch"))
    Fare=int(input("Enter Fare"))
    Embarked=float(input("Enter Embarked: (0/1/2)"))

    passanger=pd.DataFrame([{
        "Pclass":Pclass,
        "Sex":Sex,
        "Age":Age,
        "sibsp":sibsp,
        "Parch":Parch,
        "Fare":Fare,
        "Embarked_1.0":1 if Embarked == 1 else 0,
        "Embarked_2.0":1 if Embarked == 2 else 1
    }])

    passanger=passanger[model.features_names_in_]
    result=model.predict(passanger)
    print(result)


def main():
    model=LoadModel("MarvellousTitanic.pkl")

    PredictPassanger(model)


if __name__=="__main__":
    main()