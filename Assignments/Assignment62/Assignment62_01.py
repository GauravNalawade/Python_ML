import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix
from sklearn.preprocessing import StandardScaler

# -------------------------------------------------------------
# Step 1 : Load the Dataset
# -------------------------------------------------------------
data = pd.read_csv("Employee_Attrition.csv")
# print(data)

# -------------------------------------------------------------
# Step 2 : Display shape , columns and first five records (EDA)
# -------------------------------------------------------------

print("Shape of Dataset : ")
print(data.shape)

print("Columns in Dataset : ")
print(data.columns)

print("First Five Records : ")
print(data.head())

# -------------------------------------------------------------
# Step 3 : Check for Missing Values
# -------------------------------------------------------------

print("Missing Values")
print(data.isnull().sum())

missing_percentage = (data.isnull().sum() / len(data)) * 100
print("Percentage of Missing Values per column : ")
print(f"{missing_percentage}")

# -------------------------------------------------------------
# Step 4 : Identify numerical and categorical features
# -------------------------------------------------------------

print("Numerical and Categorical Features")
print(data.dtypes)

numerical_features = data.select_dtypes(include=["number"]).columns

categorical_features = data.select_dtypes(include=["object","category","str"]).columns

print("Numerical Features : ")
print(numerical_features)

print("Categorical Features : ")
print(categorical_features)

# -----------------------------------------------------------------------------
# Step 5 : Convert Categorical Features OverTime into numerical representation 
# -----------------------------------------------------------------------------

print("Uniques Values in Column OverTime")
print(data["OverTime"].unique())

data["OverTime"]=data["OverTime"].map({
    "Yes": 1,
    "No" : 0
})

print("First 5 records after Encoding")
print(data["OverTime"].head())

# -------------------------------------------------------------
# Step 6 : Convert the target Attrition into 0 and 1
# -------------------------------------------------------------

print("Uniques Values in Column Attrition")
print(data["Attrition"].unique())

data["Attrition"]=data["Attrition"].map({
    "Yes":1,
    "No" :0
})

print("First 5 records after Encoding") 
print(data["Attrition"].head())

# -------------------------------------------------------------
# Step 7 : Seperate independent and dependent variables 
# ------------------------------------------------------------- 

X=data.drop(columns="Attrition")

Y=data["Attrition"]

print("Shape of X : ",X.shape)

print("Shape of Y : ",Y.shape)

# -------------------------------------------------------------
# Step 8 : Split the dataset for Training and Testing  
# ------------------------------------------------------------- 

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42)

print("Shape of Training Input : ",X_train.shape)
print("Shape of Training Output : ",Y_train.shape)
print("Shape of Testing Input : ",X_test.shape)
print("Shape of Testing Output : ",Y_test.shape)

# -------------------------------------------------------------
# Step 9 : Apply Appropriate Feature Scaling   
# ------------------------------------------------------------- 

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)

X_test_scaled = scalar.transform(X_test)

print("Scaled Training Data :")
print(X_train_scaled[:5])

print("Scaled Testing Data :")
print(X_test_scaled[:5]) 

# -------------------------------------------------------------
# Step 10 : Design an MLP with at least Two Hidden layers  
# ------------------------------------------------------------- 

model = MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

# -------------------------------------------------------------
# Step 11 : Train the Network
# ------------------------------------------------------------- 

model.fit(X_train_scaled,Y_train)

# -------------------------------------------------------------
# Step 12 : Number of iterations required for training 
# ------------------------------------------------------------- 

print("Number of iterations are required for training: ",model.n_iter_)

# -------------------------------------------------------------
# Step 13 : Calculate training Accuracy
# ------------------------------------------------------------- 
Y_Pred_train = model.predict(X_train_scaled)

training_accuracy = accuracy_score(Y_train,Y_Pred_train)

print(f"Training Accuracy : {training_accuracy * 100:.2f}%")  

# -------------------------------------------------------------
# Step 14 : Calculate testing Accuracy
# ------------------------------------------------------------- 
Y_Pred_test = model.predict(X_test_scaled)

testing_accuracy = accuracy_score(Y_test,Y_Pred_test)

print(f"Testing Accuracy : {testing_accuracy * 100:.2f}%")

# -------------------------------------------------------------
# Step 15 : Confusion Matrix
# ------------------------------------------------------------- 

Confusion_Matrix = confusion_matrix(Y_test,Y_Pred_test)

print("Confusion Matrix :")
print(Confusion_Matrix)

# -------------------------------------------------------------
# Step 16 : Plot the loss Curve
# ------------------------------------------------------------- 
plt.figure(figsize=(8,5))

plt.plot(model.loss_curve_,linewidth=2)

plt.title("MLP Training Loss Curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.grid(True)
plt.show()

# -------------------------------------------------------------
# Step 17 : Create a function PredictAttrition(employee_data)
# ------------------------------------------------------------- 
def PredictAttrition(employee_data):

    new_employee_data_scaled = scalar.transform(employee_data) 
 
    Pred_new_employee_data = model.predict(new_employee_data_scaled) 

    return Pred_new_employee_data   

# -------------------------------------------------------------
# Step 18 : Test the system using at least five new employee records
# ------------------------------------------------------------- 

employee_data=pd.DataFrame([
    {
                        'Age':80, 
                        'MonthlyIncome':90000,
                        'YearsAtCompany':18, 
                        'TotalWorkingYears':40,
                        'DistanceFromHome':30, 
                        'JobSatisfaction':4, 
                        'WorkLifeBalance':3, 
                        'OverTime':1,
                        'NumCompaniesWorked':8,
                        'TrainingTimesLastYear':2
   },
   {
                        'Age':50, 
                        'MonthlyIncome':100000,
                        'YearsAtCompany':5, 
                        'TotalWorkingYears':25,
                        'DistanceFromHome':40, 
                        'JobSatisfaction':1, 
                        'WorkLifeBalance':1, 
                        'OverTime':1,
                        'NumCompaniesWorked':1,
                        'TrainingTimesLastYear':1 
    },
    {
                        'Age':60, 
                        'MonthlyIncome':200000,
                        'YearsAtCompany':12, 
                        'TotalWorkingYears':50,
                        'DistanceFromHome':60, 
                        'JobSatisfaction':2, 
                        'WorkLifeBalance':1, 
                        'OverTime':0,
                        'NumCompaniesWorked':2,
                        'TrainingTimesLastYear':8
    },
    {
                        'Age':30, 
                        'MonthlyIncome':250000,
                        'YearsAtCompany':5, 
                        'TotalWorkingYears':8,
                        'DistanceFromHome':50, 
                        'JobSatisfaction':4, 
                        'WorkLifeBalance':4, 
                        'OverTime':0,
                        'NumCompaniesWorked':2,
                        'TrainingTimesLastYear':0
    },
    {
                        'Age':70, 
                        'MonthlyIncome':100000,
                        'YearsAtCompany':8, 
                        'TotalWorkingYears':50,
                        'DistanceFromHome':20, 
                        'JobSatisfaction':4, 
                        'WorkLifeBalance':4, 
                        'OverTime':1,
                        'NumCompaniesWorked':5,
                        'TrainingTimesLastYear':0
    },

   ])

Result = PredictAttrition(employee_data)
print("Predicted Result for new_employee :")

for i, prediction in enumerate(Result, start=1):

    if prediction == 0:
        print(f"Employee {i} : Likely to Stay")
    else:
        print(f"Employee {i} : Likely to Leave")
