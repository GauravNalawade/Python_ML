import pandas as pd
import matplotlib as plt
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score,confusion_matrix


# -------------------------------------------------------------
# Step 1 : Load the Dataset
# -------------------------------------------------------------

DataPath = 'Loan_Default.csv'

data = pd.read_csv(DataPath)

# -------------------------------------------------------------
# Step 2 : Exploratory Data Analysis
# -------------------------------------------------------------

print("Shape of dataset : ")
print(data.shape)

print("Columns in dataset : ")
print(list(data.columns))

print("Unique Values in Target column (Default) : ")
print(data["Default"].unique())

print("Target Class Distribution (Default) : ")
print(data["Default"].value_counts())

print("First 5 Records : ")
print(data.head())

print("Missing Values Per Column : ")
print(data.isnull().sum())

print("Percentage of Missing values per column : ")
print(f"{(data.isnull().sum()) / len(data) * 100 }")

print("Class Distribution (Default) : ")
print(data["Default"].value_counts()) 