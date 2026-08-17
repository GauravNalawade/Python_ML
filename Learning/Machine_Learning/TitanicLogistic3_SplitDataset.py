import pandas as pd
import numpy as np
import joblib as jb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix

# Step 1: Load Data

# ---------------------------------------------------------------------------
# Function Name: Load Data
# Description :  Load the data from csv
# Input:         Name of Csv File
# Output:        Data Frame
# Author:        Gaurav Nalawade
# Date:          16/08/2026
# ---------------------------------------------------------------------------


def LoadData(fileName):
    df=pd.read_csv(fileName)

    print("Dataset Loaded Successfully")
    print(df.head())

    return df
# Step 2: Data Preprocessing

# ---------------------------------------------------------------------------
# Function Name: Preprocessing
# Description :  It performs data analysis
# Input:         Data Frame
# Output:        Updated DataFrame
# Author:        Gaurav Nalawade
# Date:          16/08/2026
# ---------------------------------------------------------------------------


def preprocessdata(df):
    df=df.drop(["Passengerid",
                "zero",
                "name"
                ],
                errors="ignore"
               )

    # Handle missing values
    df["Age"]=df["Age"].fillna(df["Age"].median())
    df["Fare"]=df["Fare"].fillna(df["Fare"].median())

    df["Embarked"]=df["Embarked"].fillna(df["Embarked"].mode()[0])

    # Convert Categorical to numeric Data

    df=pd.get_dummies(
        df,
        columns=["Embarked"],
        drop_first=True,
        dtype=int 
    )    
    
    print(df.head())

    print("Data Preprocessig Completed")

    return df


# Step 3: Split Data

# ---------------------------------------------------------------------------
# Function Name: SplitData
# Description :  It performs Splitting acitvity
# Input:         Data Frame
# Output:        4 Subset for training and testing 
# Author:        Gaurav Nalawade
# Date:          16/08/2026
# ---------------------------------------------------------------------------

def SplitData(df):
    X=df.drop("Survived",axis=1)
    Y=df["Survived"]

    X_train,X_test,Y_train,Y_test=train_test_split(
        X,
        Y,
        test_size=0.2,
        random_state=42
    )
    print("Dataset Splitting Completed Successfully")
    return X_train,X_test,Y_train,Y_test


# ---------------------------------------------------------------------------
# Function Name: main
# Description :  Entry point function 
# Input:         None
# Output:        None
# Author:        Gaurav Nalawade
# Date:          16/08/2026
# ---------------------------------------------------------------------------

             
def main():
    # Step1 :
    df=LoadData("MarvellousTitanicDataset.csv")

    # Step 2:
    df=preprocessdata(df)

    # Step 3: 
    X_train,X_test,Y_train,Y_test=SplitData(df)




if __name__=="__main__":
    main()