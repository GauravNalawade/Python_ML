import pandas as pd

Border="-"*30

#########################################
# Step 1: Load the dataset
#########################################

print(Border)
print("Step 1: Load the dataset")
print(Border)

DataPath="iris.csv"

df=pd.read_csv(DataPath)

print("Dataset loaded successfully") 
print("Initial entries from Dataset are.:")
print(df.head())

#########################################
# Step 2: Data Analysis (EDA)
#########################################

print(Border)
print("Step 2: Data Analysis (EDA)")
print(Border)

print("Shape of dataset:",df.shape)

print("Column names:",list(df.columns))

print("Missing value per column:")
print(df.isnull().sum()) 

print("Class distribution (species count)")
print(df["species"].value_counts())

print("Stastical Reports od dataset")
print(df.describe())
