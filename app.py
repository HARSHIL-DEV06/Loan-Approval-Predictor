import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Loan Approval Prediction App")
st.write("Enter applicant details below:")

st.subheader("Applicant Inputs")

cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700)

loan_term = st.number_input("Loan Term (months)", min_value=1, max_value=360, value=12)

loan_amount = st.number_input("Loan Amount", min_value=10000, max_value=10000000, value=300000, step=10000)

no_of_dependents = 2
self_employed = 0
income_annum = 500000
residential_assets_value = 200000
commercial_assets_value = 150000
luxury_assets_value = 100000
bank_asset_value = 100000
education_Graduate = 1
education_Not_Graduate = 0

if st.button("Predict Loan Status"):
    input_data = np.array([[
        no_of_dependents,
        self_employed,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value,
        education_Graduate,
        education_Not_Graduate
    ]])

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Loan Approved ✅")
    else:
        st.error("Loan Rejected ❌")