import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import BaggingRegressor
from sklearn.metrics import mean_squared_error,r2_score

# ------------------------------------------------------
# Step1 : Load the Data
# ------------------------------------------------------

df=pd.read_csv("california_housing.csv")

print("Shape of Dataset :",df.shape)
print("First few Records: ",df.head())

# ------------------------------------------------------
# Step2 : Separate Features ans labels
# ------------------------------------------------------

X=df.drop("target",axis=1)
Y=df["target"]

print("Shape of X:",X.shape)  
print("Shape of Y:",Y.shape)

# ------------------------------------------------------
# Step3 : Split Dataset for training and testing
# ------------------------------------------------------

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)

# ------------------------------------------------------
# Step 4.1: Create the Base model 
# ------------------------------------------------------

Base_model=DecisionTreeRegressor(random_state=42)

# ------------------------------------------------------
# Step 4.1: Create the Bagging model
# ------------------------------------------------------

model=BaggingRegressor(
    estimator=Base_model,
    n_estimators=10,
    random_state=42
)

# ------------------------------------------------------
# Step5 : Train the model
# ------------------------------------------------------

model=model.fit(X_train,Y_train)

# ------------------------------------------------------
# Step6 : Test the model
# ------------------------------------------------------

Y_pred=model.predict(X_test)

# ------------------------------------------------------
# Step7 : Evaluate the model
# ------------------------------------------------------

print("MSE:",mean_squared_error(Y_test,Y_pred))
print("R2:",r2_score(Y_test,Y_pred))

