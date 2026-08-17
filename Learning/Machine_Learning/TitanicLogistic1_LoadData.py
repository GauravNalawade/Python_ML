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

# ---------------------------------------------------------------------------
# Function Name: main
# Description :  Entry point function 
# Input:         
# Output:        
# Author:        Gaurav Nalawade
# Date:          16/08/2026
# ---------------------------------------------------------------------------
             
def main():
    LoadData("MarvellousTitanicDataset.csv")


if __name__=="__main__":
    main()