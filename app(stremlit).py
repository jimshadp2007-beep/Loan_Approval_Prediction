import streamlit as st
import pandas as pd
import joblib

# Load model
pipeline = joblib.load("loan_approval_pipeline.pkl")

st.title("Loan Approval Prediction")

# Inputs
no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    value=0
)
education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

education = 1 if education == "Graduate" else 0

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

self_employed = 1 if self_employed == "Yes" else 0
income_annum = st.number_input(
    "Annual Income",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=1
)

loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1
)

cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=700
)

residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0
)

commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0
)

luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0
)

bank_asset_value = st.number_input(
    "Bank Asset Value",
    min_value=0
)

# Predict Button
if st.button("Predict"):

    # Derived Features
    total_assets = (
        residential_assets_value
        + commercial_assets_value
        + luxury_assets_value
        + bank_asset_value
    )

    loan_income_ratio = loan_amount / max(income_annum, 1)

    assets_loan_ratio = total_assets / max(loan_amount, 1)

    emi_income_ratio = (
        (loan_amount / max(loan_term, 1))
        / max((income_annum / 12), 1)
    )

    # Create DataFrame
    data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education],
        "self_employed": [self_employed],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value],
        "total_assets": [total_assets],
        "loan_income_ratio": [loan_income_ratio],
        "assets_loan_ratio": [assets_loan_ratio],
        "emi_income_ratio": [emi_income_ratio]
    })
try:
    prediction = pipeline.predict(data)

    st.write("Raw Prediction:", prediction[0])

    if prediction[0] == 0:
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")

except Exception as e:
    st.error(f"Error: {e}")