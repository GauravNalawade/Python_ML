import pandas as pd
import matplotlib.pyplot as plt

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler


def MarvellousClassifier(DataPath):
    border="-"*40

    # Step1: Load the dataset from csv file 
    print(border)
    print("Step1: Load the dataset from csv file")

    df=pd.read_csv(DataPath)

    print(border)
    print("Some entries from dataset:")
    print(df.head())
    print(border)

    # Step2: Clean the dataset 
    print(border)
    print("Step2:Clean the dataset")
    print(border)

    df.dropna(inplace=True)

    print("Shape of Dataset",df.shape)
    print("Total Records:",df.shape[0])
    print("Total Columns:",df.shape[1])

    print(border)

    # Step 3: Shaperate Independent and Dependent Variables
    print(border)
    print("Step 3: Shaperate Independent and Dependent Variables")
    print(border)

    X=df.drop(columns=['Class'])
    Y=df['Class'] 

    print("Shape of X:",X.shape)
    print("Shape of Y:",Y.shape) 

    print(border)
    print("Input Columns:",X.columns.tolist())
    print("Output Columns:Class")
    print(border)

    # Step 4: Split the dataset for training and testing

    print(border)
    print("Step 4: Split the dataset for training and testing")
    print(border)

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42,stratify=Y)

    print(border)
    print("Details of Training and Testing Data")
    print("Shape of X_train:",X_train.shape)
    print("Shape of X_test:",X_test.shape)
    print("Shape of Y_train:",Y_train.shape)
    print("Shape of Y_test:",Y_test.shape)

    print(border)

    # Step5:Feature Scaling
    print(border)
    print("Step5: Feature Scaling")
    print(border)

    scaler=StandardScaler()
    X_train_scaled=scaler.fit_transform(X_train)
    X_test_scaled=scaler.fit_transform(X_test)

    print("Feature Scaling done")

    print(border)


def main():
    MarvellousClassifier("WinePredictor.csv")

if __name__=="__main__":
    main()