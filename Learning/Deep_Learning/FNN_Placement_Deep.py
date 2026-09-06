# ------------------------------------------------------------------------------
# Deep Learning pipeline
# ------------------------------------------------------------------------------
# 1. Read the data from CSV
# 2. Data Analysis (EDA)
# 3. Preprocessing
# 4. Train Test Split
# 5. Feature Scaling
# 6. FNN Model training
# 7. Model Evaluation
# 8. Graphical Representation
# 9. Model Preserve 
# 10.Model Loading and Preserve 
# 11.Test Unseen Data
# ------------------------------------------------------------------------------


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score,confusion_matrix


# ------------------------------------------------------------------------------
# 1.Read the data from csv
# ------------------------------------------------------------------------------


data= pd.read_csv("placement_data.csv")

print("Complete Dataset")
print(data)


# ------------------------------------------------------------------------------
# 2. Data Analysis
# ------------------------------------------------------------------------------

print("2. Data Analysis")

print("First 5 rows")
print(data.head())

print("column names :")
print(data.columns)

print("Shape of dataset :")
print(data.shape)

print("Satsticial Summary :")
print(data.describe())

# ------------------------------------------------------------------------------
# 3. Preprocessing
# ------------------------------------------------------------------------------

print("3. Preprocessing")

X=data[['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']]

Y=data['Placed']

print("Input Features: ")
print(X.head())

print("Target: ")
print(Y.head())

# ------------------------------------------------------------------------------
# 4. TRain test split
# ------------------------------------------------------------------------------

print("Train Test Split")

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.30,random_state=42)

print("Training Input Shape:",X_train.shape)
print("Testing Input Shape:",X_test.shape)
print("Training Output Shape:",Y_train.shape)
print("Testing Output Shape:",Y_test.shape)

# ------------------------------------------------------------------------------
# 5. Feature Scaling
# ------------------------------------------------------------------------------
print("5. Feature Scaling")

scalar=StandardScaler()

X_train_scaled=scalar.fit_transform(X_train)

X_test_scaled=scalar.fit_transform(X_test)

print("Scales Training Data :")
print(X_train_scaled[:5])

# ------------------------------------------------------------------------------
# 6. FNN Model Training 
# ------------------------------------------------------------------------------

print("6. FNN Model Training ")
model=MLPClassifier(
    hidden_layer_sizes=(8,4),
    activation="relu",
    solver="adam",
    max_iter=1000,
    random_state=42
)
print(model)

print("Train the model")

model.fit(X_train_scaled,Y_train)

print("Model Training completed")

# ------------------------------------------------------------------------------
# 7. Model Evaluation 
# ------------------------------------------------------------------------------

print("7. Model Evaluation ")

Y_pred=model.predict(X_test_scaled)

Accuracy=accuracy_score(Y_test,Y_pred)

print("Accuracy is :",Accuracy)

cm = confusion_matrix(Y_test,Y_pred)

print("Confusion matrix :",cm)

print("Predict the probability : ")

Y_prob=model.predict_proba(X_test_scaled)

print(Y_prob[:5])

# ------------------------------------------------------------------------------
# 9. Model Preserve
# ------------------------------------------------------------------------------
print("9. Model Preserve")

joblib.dump(model,"placement_fnn_model.pkl")

joblib.dump(scalar,"Placement_scaler.pkl") 

print("Model and Scalar gets dump successfully")

# ------------------------------------------------------------------------------
# 10. Model loading and preserve
# ------------------------------------------------------------------------------

print("10. Model loading and preserve")

loaded_model=joblib.load("placement_fnn_model.pkl")
loaded_scalar=joblib.load("Placement_scaler.pkl")

print("Model gets loaded successfully") 

# ------------------------------------------------------------------------------
# 11.Test Unseen Data
# Aptitude:70
# coding :75
# communication:80
# Academics:85
# Internship:1
# ------------------------------------------------------------------------------

print("11.Test Unseen Data")

new_student=pd.DataFrame([[70,75,80,85,1]],columns=['Aptitude', 'Coding', 'Communication', 'Academics', 'Internship']) 

new_student_scaled=loaded_scalar.transform(new_student)

new_prediction=loaded_model.predict(new_student_scaled)

new_probability=loaded_model.predict_proba(new_student_scaled)

print("New Students Data :")
print(new_student)

print("Prediction Probabilityt: ",new_probability)

if new_prediction[0]==1:
    print("Prediction :Placed")
else: 
    print("Prediction :Not Placed")


 