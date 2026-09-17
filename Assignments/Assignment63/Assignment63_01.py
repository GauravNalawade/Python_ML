import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import confusion_matrix,accuracy_score,classification_report,precision_score,recall_score,f1_score

# -------------------------------------------------------------
# Step 1 : Load the Dataset
# -------------------------------------------------------------

Datapath = "Loan_Default.csv"

data = pd.read_csv(Datapath)

print(data)

# -------------------------------------------------------------
# Step 2 : Exploratory Data Analysis (EDA)
# -------------------------------------------------------------

print("Shape of Dataset : ")
print(data.shape)

print("Columns name : ")
print(list(data.columns))

print("First 5 Records : ")
print(data.head())

print("Statistical Report of Dataset : ")
print(data.describe())

print("Missing Values Per Column : ")
print(data.isnull().sum())

missing_percentage = (data.isnull().sum() / len(data)) * 100
print("Percentage of Missing Values per column : ")
print(f"{missing_percentage}")

print("Unique values (Class) : ")
print(data["Default"].unique()) 

# Target class is inbalanced class 0 have 879 records and class 1 have 321 records 
print("Class Distribution (Default): ")
print(data["Default"].value_counts())

# -------------------------------------------------------------
# Step  : Identify numerical and categorical features
# -------------------------------------------------------------

print("Numerical and categorical features : ")
print(data.dtypes)

numerical_features = data.select_dtypes(include=["number"]).columns

categorical_features = data.select_dtypes(include=["object","category","str"]).columns

print("Numerical features : ")
print(numerical_features)

print("Categorical features : ")
print(categorical_features)

# -------------------------------------------------------------
# Step 5 : Encode categorical variables
# -------------------------------------------------------------
  
print("Unique values in column PreviousDefault")
print(data["PreviousDefault"].unique())  
# Binary Encoding
data["PreviousDefault"] = data["PreviousDefault"].map({
    "Yes" : 1,
    "No" : 0
 })

 
print("Unique values in column HomeOwnership")
print(data["HomeOwnership"].unique())
# One-Hot Encoding
data = pd.get_dummies(
    data, 
    columns=["HomeOwnership"], 
    dtype=int
)

print("Data after Encoding:")
print(data.head())

# -------------------------------------------------------------
# Step 6 : Seperate independent(X) and dependent(Y) variables 
# ------------------------------------------------------------- 

X = data.drop(columns="Default")

Y = data["Default"]

print("Shape of X : ")
print(X.shape)

print("Shape of Y : ")
print(Y.shape) 

# -------------------------------------------------------------
# Step 7 : Split the dataset for Training and Testing  
# ------------------------------------------------------------- 

X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=0.3,random_state=42,stratify=Y)

print("Shape of Training Input : ",X_train.shape)
print("Shape of Training Output : ",Y_train.shape)
print("Shape of Testing Input : ",X_test.shape)
print("Shape of Testing Output :",Y_test.shape)

print("Original:")
print(Y.value_counts(normalize=True))

print("\nTraining:")
print(Y_train.value_counts(normalize=True))

print("\nTesting:")
print(Y_test.value_counts(normalize=True))

# -------------------------------------------------------------
# Step 8 : Explain whether statified splitting should be used 
# ------------------------------------------------------------- 
# yes , because the dataset is inbalanced the class (0) has 879 and class (1) has 321 records that why using the stratify=Y 
# it split the target class in proportaion in training and testing part 

# -------------------------------------------------------------
# Step 9 : Scale the features
# ------------------------------------------------------------- 

scalar = StandardScaler()

X_train_scaled = scalar.fit_transform(X_train)

X_test_scaled = scalar.transform(X_test)

print("Scaled Training data : ")
print(X_train_scaled[:5])

print("Scaled Testing Data : ")
print(X_test_scaled[:5])    

# -------------------------------------------------------------
# Step 10 : Create a MLPClassifier (Hyperparameter Experiment) 1 Activation
# ------------------------------------------------------------- 

def EvaluateModel(model):
    
    model.fit(X_train_scaled,Y_train)

    Y_pred = model.predict(X_test_scaled)
 
    accuracy = accuracy_score(Y_test,Y_pred)
    precision = precision_score(Y_test,Y_pred)
    recall = recall_score(Y_test,Y_pred)
    f1 = f1_score(Y_test,Y_pred)

    return accuracy,precision,recall,f1


activations = ["identity", "logistic", "tanh", "relu"]

activation_results = []

for activation_name in activations:

    model=MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation=activation_name,
        solver="adam",
        max_iter=1000,
        random_state=42
    )     

    accuracy, precision, recall, f1 = EvaluateModel(model)

    activation_results.append([activation_name,accuracy,precision,recall,f1])

print("Acivation Result :",activation_results)
activation_results_df = pd.DataFrame(
    activation_results,
    columns=[
        "Activation",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\nActivation Function Experiment:")
print(activation_results_df)

# -------------------------------------------------------------
# Step 10 : Create a MLPClassifier (Hyperparameter Experiment) 2-Hidden Layers
# ------------------------------------------------------------- 

hidden_layers = [
        (10,),
        (20,10),
        (50,25),
        (100,50,25)
    ]

hidden_layers_results = []

for layers in hidden_layers:
    
    model=MLPClassifier(
        hidden_layer_sizes=layers,
        activation='relu',
        solver="adam",
        max_iter=1000,
        random_state=42
    )     

    accuracy, precision, recall, f1 = EvaluateModel(model)

    hidden_layers_results.append([
        str(layers),
        accuracy,
        precision,
        recall,
        f1
    ])

hidden_layers_results_df = pd.DataFrame(
    hidden_layers_results,
    columns=[
        "Hidden Layers",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\n\nHidden Layer Experiment: ")
print(hidden_layers_results_df)

# -------------------------------------------------------------
# Step 10 : Create a MLPClassifier (Hyperparameter Experiment) 3-Learning Rate
# -------------------------------------------------------------

learning_rates = [
    0.0001,
    0.0005,
    0.001,
    0.005,
    0.01
]

learning_rates_result = []


for lr in learning_rates:

    model=MLPClassifier(
        hidden_layer_sizes=(32,16),
        activation='relu', 
        solver='adam',
        learning_rate_init=lr, 
        max_iter=1000, 
        random_state=42 
    ) 

    accuracy, precision, recall, f1 = EvaluateModel(model)

    learning_rates_result.append([lr,accuracy,precision,recall,f1])

learning_rate_results_df = pd.DataFrame(
    learning_rates_result,
    columns=[
        "Learning Rate",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
) 

print("\n\nLearning Rate Experiment:")
print(learning_rate_results_df)


model = MLPClassifier(
    hidden_layer_sizes=(32, 16),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)   

# -------------------------------------------------------------
# Step 11 : Train the model 
# ------------------------------------------------------------- 

model.fit(X_train_scaled,Y_train) 

# -------------------------------------------------------------
# Step 12 : Calculate training Accuracy
# ------------------------------------------------------------- 
print("Number of Training Iterations :", model.n_iter_)

Y_Pred_train = model.predict(X_train_scaled)

training_accuracy = accuracy_score(Y_train,Y_Pred_train)

print(f"Training Accuracy : {training_accuracy * 100:.2f}%")  


# -------------------------------------------------------------
# Step 12 : Calculate Testing Accuracy
# ------------------------------------------------------------- 

Y_pred = model.predict(X_test_scaled)

testing_accuracy = accuracy_score(Y_test,Y_pred)

print(f"Testing Accuracy : {testing_accuracy * 100:.2f}%")

# -------------------------------------------------------------
# Step 13 : Confusion Matrix
# ------------------------------------------------------------- 

print("Confusion Matrix : ")   

Confusion_Matrix = confusion_matrix(Y_test,Y_pred)

print(Confusion_Matrix)

# -------------------------------------------------------------
# Step 14 : Classification report
# ------------------------------------------------------------- 
print("Classification Report : ")
print(classification_report(Y_test,Y_pred)) 

# -------------------------------------------------------------
# Step 15 : Calculate Precision, Recall and F1-Score
# -------------------------------------------------------------

precision = precision_score(Y_test, Y_pred)
recall = recall_score(Y_test, Y_pred) 
f1 = f1_score(Y_test, Y_pred)
  
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}") 
print(f"F1-Score  : {f1:.4f}")  
# -------------------------------------------------------------
# Step 16 : Plot Training loss 
# ------------------------------------------------------------- 

plt.figure(figsize=(8,5))

plt.plot(model.loss_curve_,linewidth=2)

plt.title("MLP Training loss curve")
plt.xlabel("Iterations")
plt.ylabel("Loss")

plt.grid(True)
plt.show()

# -------------------------------------------------------------
# Step 18 : Test the model on new loan applicants
# ------------------------------------------------------------- 

def PredictDefault(new_loan_aaplicant):

    new_loan_aaplicant_scaled = scalar.transform(new_loan_aaplicant)

    new_loan_aaplicant_pred = model.predict(new_loan_aaplicant_scaled)

    return new_loan_aaplicant_pred

# -------------------------------------------------------------
# Step 18 : new loan applicants data 
# ------------------------------------------------------------- 

new_loan_aaplicant = pd.DataFrame([
    {
        "Age": 18,
        "Income":500000,
        "LoanAmount":50000,
        "CreditScore":761,
        "EmploymentYears":2,
        "ExistingLoans":0, 
        "MonthlyDebt":5182, 
        "LoanTerm":13, 
        "PreviousDefault":0, 
        "HomeOwnership_Mortgage":0,
        "HomeOwnership_Own":0,
        "HomeOwnership_Rent":1
    },
    {
        "Age": 23,
        "Income":600000,
        "LoanAmount":80000,
        "CreditScore":781,
        "EmploymentYears":5,
        "ExistingLoans":1, 
        "MonthlyDebt":12000, 
        "LoanTerm":12, 
        "PreviousDefault":1, 
        "HomeOwnership_Mortgage":0,
        "HomeOwnership_Own":0,
        "HomeOwnership_Rent":1 
    },
    {
        "Age": 50,
        "Income":1200000,
        "LoanAmount":100000,
        "CreditScore":655,
        "EmploymentYears":5,
        "ExistingLoans":2, 
        "MonthlyDebt":10000, 
        "LoanTerm":12, 
        "PreviousDefault":0, 
        "HomeOwnership_Mortgage":0,
        "HomeOwnership_Own":0,
        "HomeOwnership_Rent":1 
    }
 ])


Result = PredictDefault(new_loan_aaplicant)
print("Predicted Result for new applicants : ")

for i , prediction in enumerate (Result,start=1) :
    
    if prediction == 0 :
        print(f"Applicant {i} : has Low Risk")
    else: 
        print(f"Applicant {i} : has High Risk")