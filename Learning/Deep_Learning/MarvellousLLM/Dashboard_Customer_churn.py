import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Marvellous Infosystem Dashboard")


st.title("Marvellous Infosystem by piush manohar kahirna")
st.header("Customer Churn Prediction")
st.write("Machine Learning APllication Dashboard")

model = joblib.load("Marvellous_ML_Customer_Churn.pkl")

st.subheader("Enter Customer Details :")

age =st.number_input("Customer age",min_value=1)
tenure = st.number_input("Tenure (Months)",min_value=1)
charges =st.number_input("Monthl Charges",min_value=1)
calls = st.number_input("Support calls",min_value=1) 

if st.button("Predict Churn"):
    NewCusromer = pd.DataFrame({
    "Age":[age],
    "Tenure":[tenure],
    "MonthlyCharges":[charges],
    "SupportCalls":[calls]
    })

    prediction = model.predict(NewCusromer)[0]

    if prediction == 1:
      st.error("Customer is likely to churn") 
    else:
      st.sucess("Customer is Unlikely to churn") 

# st.divider()

st.caption("Marvellous Infodydtems Dashboard")