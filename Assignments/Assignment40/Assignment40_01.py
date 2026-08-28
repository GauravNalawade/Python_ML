import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score,confusion_matrix

def main():
    Border="_"*50

    ##########################################################
    # Step 1: Load the Dataset 
    ##########################################################
    
    print(Border)
    print("Step 1: Load the Dataset")
    print(Border)

    DataPath="student_performance_ml.csv"
    df=pd.read_csv(DataPath)

    ##########################################################
    # Step 2: Data Analysis (EDA) 
    ##########################################################
    print(Border)
    print("Step 2: Data Analysis (EDA)")
    print(Border)

    print("Shape of dataset:",df.shape)
    print("Coulumn Names:",list(df.columns))

    print("Missing values per column:")
    print(df.isnull().sum())

    print("Class Distribution (FinalResult):")
    print(df["FinalResult"].value_counts())

    print("Statistical report of dataset:")
    print(df.describe()) 

    ##########################################################
    # Step 3: Visualisation of dataset
    ##########################################################

    # print(Border)
    # print("Step 3: Visualisation of dataset")
    # print(Border)
     
    # # Scatter Plot

    # plt.figure(figsize=(7,5))

    # for sp in df["FinalResult"].unique():
    #     temp=df[df["FinalResult"]==sp]  
    #     plt.scatter(temp["StudyHours"],temp["PreviousScore"],label=sp)

    # plt.title("Student Pass Fail StudyHours vs PreviousScore")
    # plt.xlabel("StudyHours")
    # plt.ylabel("PreviousScore")

    # plt.legend()
    # plt.grid()
    # plt.show()


    # # Histogram 

    # plt.hist(
    #     df["StudyHours"],
    #     bins=4,
    #     color="skyblue",
    #     edgecolor="black"
    # )

    # plt.title("Histogram for Student Performance")
    # plt.xlabel("StudyHours")
    # plt.ylabel("Frequency")

    # plt.show()

    # # Boxplot
    
    # sns.boxplot(
    #     x=df["FinalResult"],
    #     y=df["AssignmentsCompleted"]
    # )
    # plt.title("Boxplot for Assignments Completed Vs Final Result")
    # plt.xlabel("Final Result")
    # plt.ylabel("Assignmet Completed")
    # plt.show()
    
    
    ##########################################################
    # Step 4: Decide Independent and Dependent Variables
    ##########################################################

    print(Border)
    print("Step 4: Decide Independent and Dependent Variables")
    print(Border)

    # features_cols=[
    #     "StudyHours",  
    #     "Attendance", 
    #     "PreviousScore", 
    #     "AssignmentsCompleted", 
    #     "SleepHours" 
    #     ]
  
    X=df.drop("FinalResult",axis=1)
    Y=df["FinalResult"]  

    print("Shape of X :",X.shape)   
    print("Shape of Y :",Y.shape)

    ##########################################################
    # Step 5: Split Dataset for training and testing 
    ##########################################################

    print(Border)
    print("Step 5:Split the dataset for training and testing")  
    print(Border)


    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

    print("Dataset splitting activity done")  

    print("X_train :",X_train.shape)
    print("X_test :",X_test.shape)

    print("Y_train :",Y_train.shape)
    print("Y_test :",Y_test.shape)

    #######################################################################################
    # Step 6: Build the model with using DecisionTreeClassifier with different max_depths
    #######################################################################################

    print(Border) 
    print("Step 6: Build the model with using DecisionTreeClassifier with different max_depths") 
    print(Border) 

    # max_depth=5
    model=DecisionTreeClassifier(max_depth=5,random_state=42)

    # # max_depth=1
    # model1=DecisionTreeClassifier(max_depth=1) 

    # # max_depth=3
    # model3=DecisionTreeClassifier(max_depth=3)
    
    # # max_depth=None
    # modelN=DecisionTreeClassifier(max_depth=None)


    ########################################################## 
    # Step 7 : Train the models
    ##########################################################

    print(Border) 
    print("Step 7: Train the models")
    print(Border) 

    # max_depth=5
    model.fit(X_train,Y_train)

    # # max_depth=1
    # model1.fit(X_train,Y_train)

    # # max_depth=3
    # model3.fit(X_train,Y_train) 

    # # max_depth=None
    # modelN.fit(X_train,Y_train) 

    ########################################################## 
    # Step  : Feature Importance
    ##########################################################
    print(Border)
    print("Step  : Feature Importance")
    print(Border)

    for feature, importance in zip(X.columns, model.feature_importances_):
        print(feature, ":", importance)

    ########################################################## 
    # Step 8 : Evaluate the performance
    ##########################################################

    print(Border)
    print(" Step 8 : Evaluate the performance")
    print(Border)

    # # Training Accuracy
    # print(Border)
    # print(" Step  : Training Accuracy of model")
    # print(Border)
    # Y__train_pred=model.predict(X_train)
    # Training_Accuracy=accuracy_score(Y_train,Y__train_pred)
    # print("Training Accuracy:",Training_Accuracy)
    # print("Actual Values    :", Y_train.to_numpy())
    # print("Predicted Values :", Y__train_pred)

    
    # Testing Accuracy
    print(Border)
    print("Step  : Testing Accuracy of model")
    print(Border)
    Y_Test_pred=model.predict(X_test)
    Testing_Accuracy=accuracy_score(Y_test,Y_Test_pred)
    print("Testing Accuracy :",Testing_Accuracy *100)
    print("Actual Values    :", Y_test.to_numpy())
    print("Predicted Values :", Y_Test_pred)

    # # Testing Accuracy
    # print(Border)
    # print(" Step  : Testing Accuracy of model1")
    # print(Border)
    # Y_model1_Pred=model1.predict(X_test)
    # Accuracy_Score_m1=accuracy_score(Y_test,Y_model1_Pred)
    # print("Testing Accuracy :",Accuracy_Score_m1*100)
    # print("Actual Values    :", Y_test.to_numpy())
    # print("Predicted Values :", Y_model1_Pred)

    # # Testing Accuracy
    # print(Border)
    # print(" Step  : Testing Accuracy of model3")
    # print(Border)
    # Y_Pred_model3=model3.predict(X_test)
    # Accuracy_Score_m3=accuracy_score(Y_test,Y_Pred_model3)
    # print("Testing Accuracy :",Accuracy_Score_m3*100)
    # print("Actual Values    :", Y_test.to_numpy())
    # print("Predicted Values :", Y_Pred_model3)

    # # Testing Accuracy
    # print(Border)
    # print(" Step  : Testing Accuracy of modelN")
    # print(Border)
    # Y_Pred_modelN=modelN.predict(X_test)
    # Accuracy_Score_mN=accuracy_score(Y_test,Y_Pred_modelN)
    # print("Testing Accuracy :",Accuracy_Score_mN*100)
    # print("Actual Values    :", Y_test.to_numpy())
    # print("Predicted Values :", Y_Pred_modelN)


    # Confusion Matrix of Model
    print(Border)
    print("Confusion Matrix")
    print(Border)

    Confusion_matrix=confusion_matrix(Y_test,Y_Test_pred)
    print("Confusion Matrix is:")
    print(Confusion_matrix)

    # # Predict new record
    # new_student=pd.DataFrame(  
    #     {   "StudyHours":[6],
    #         "Attendance":[85],
    #         "PreviousScore":[66],
    #         "AssignmentsCompleted":[7], 
    #         "SleepHours":[7]
    #     })

    # prediction = model.predict(new_student) 

    # if prediction[0]==1:
    #     print("Predicted result: Pass")
    # else:
    #     print("Predicted Result: Fail")


    ########################################################### 
    # Step  : Remove the column SleepHours from the dataset
    ##########################################################
    print(Border)
    print("Step  : Remove the column SleepHours from the dataset")
    print(Border)

    X=df.drop(columns=["FinalResult","SleepHours"])

    Y=df["FinalResult"]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

    model.fit(X_train,Y_train)

    print(Border)
    print("Testing Accuracy of model after removing SleepHours Column")
    print(Border)
    Y_pred=model.predict(X_test)
    Accuracy_Score=accuracy_score(Y_test,Y_pred)
    print("Testing Accuracy :",Accuracy_Score *100)
    print("Actual Values    :", Y_test.to_numpy())
    print("Predicted Values :", Y_pred)

    ########################################################### 
    # Step  : Train the model using only:
    # StudyHours
    # Attendance  
    ##########################################################
    print(Border)
    print("Step  : Train the model using only:")
    print("StudyHours")
    print("Attendance")
    print(Border)

    features_cols=["StudyHours","Attendance"]
    X=df[features_cols]
    Y=df["FinalResult"]

    X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.5,random_state=42)

    model.fit(X_train,Y_train)

    Y_pred=model.predict(X_test)

    Accuracy_ScoreX=accuracy_score(Y_test,Y_pred)
    print("Accuracy Score  :",Accuracy_ScoreX*100)
    print("Actual Values   :",Y_test.to_numpy())
    print("Predicted Values:",Y_pred)

    # 4. Create a new DataFrame with details of 5 new students.
    # Use the trained model to predict their results.
    # Display predictions clearly.

    new_students=pd.DataFrame([
                     {
                        "StudyHours":10.0,
                        "Attendance":95
                      },
                      {
                        "StudyHours":7.5,
                        "Attendance":85
                      }, 
                      {
                        "StudyHours":3.5,
                        "Attendance":70
                      }, 
                     {
                        "StudyHours":9.5,
                        "Attendance":95
                     }, 
                     {
                        "StudyHours":8.5,
                        "Attendance":95
                     }
                    ]) 

    Result=model.predict(new_students)

    for student in Result:
        if(student == 1):
           print("Student  : ","Pass")
        else:
           print("Student  : ","Fail")


if __name__=="__main__":
    main() 