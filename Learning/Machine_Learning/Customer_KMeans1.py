import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


def main():
    # Step 1: Load Dataset
    df=pd.read_csv("Mall_Customers.csv")

    print("Data Loaded Successfulyy")
    print(df.head())

    print("Missing values :")
    print(df.isnull().sum()) 
    


if __name__=="__main__":
    main()