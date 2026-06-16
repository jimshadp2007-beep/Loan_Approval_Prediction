import streamlit as st
import pandas as pd
import joblib
import time

# ------------------------------------------------------------------
# Page Config
# ------------------------------------------------------------------
st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="💰",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------------
# Custom CSS Animations & Styling
# ------------------------------------------------------------------
st.markdown("""
<style>
@keyframes fadeInDown {
    from {opacity: 0; transform: translateY(-30px);}
    to {opacity: 1; transform: translateY(0);}
}
@keyframes fadeInUp {
    from {opacity: 0; transform: translateY(30px);}
    to {opacity: 1; transform: translateY(0);}
}
@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.03); }
    100% { transform: scale(1); }
}
@keyframes gradientShift {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
@keyframes bounceIn {
    0% { transform: scale(0.3); opacity: 0; }
    50% { transform: scale(1.05); opacity: 1; }
    70% { transform: scale(0.9); }
    100% { transform: scale(1); }
}
@keyframes shake {
    0%, 100% { transform: translateX(0); }
    20%, 60% { transform: translateX(-8px); }
    40%, 80% { transform: translateX(8px); }
}

/* Animated gradient title */
.title-banner {
    background: linear-gradient(270deg, #4facfe, #00f2fe, #43e97b, #38f9d7);
    background-size: 800% 800%;
    animation: gradientShift 8s ease infinite, fadeInDown 1s ease;
    padding: 28px;
    border-radius: 16px;
    text-align: center;
    margin-bottom: 25px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.15);
}
.title-banner h1 {
    color: white;
    font-size: 2.4rem;
    margin: 0;
    text-shadow: 1px 1px 6px rgba(0,0,0,0.2);
}
.title-banner p {
    color: #f0f0f0;
    margin: 5px 0 0 0;
    font-size: 1rem;
}

/* Section card */
.section-card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 14px;
    padding: 18px 22px;
    margin-bottom: 18px;
    animation: fadeInUp 0.7s ease;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}
.section-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 10px 25px rgba(0,0,0,0.18);
}

/* Predict button */
div.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #11998e, #38ef7d);
    color: white;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 0.75em 1em;
    border-radius: 12px;
    border: none;
    transition: all 0.3s ease;
    animation: pulse 2.5s infinite;
}
div.stButton > button:hover {
    transform: scale(1.04);
    box-shadow: 0 6px 18px rgba(56,239,125,0.4);
    animation: none;
}

/* Result boxes */
.result-approved {
    background: linear-gradient(135deg, #11998e, #38ef7d);
    padding: 28px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 1.6rem;
    font-weight: 800;
    animation: bounceIn 0.8s ease;
    box-shadow: 0 8px 24px rgba(56,239,125,0.35);
}
.result-rejected {
    background: linear-gradient(135deg, #eb3349, #f45c43);
    padding: 28px;
    border-radius: 16px;
    text-align: center;
    color: white;
    font-size: 1.6rem;
    font-weight: 800;
    animation: shake 0.6s ease, fadeInUp 0.6s ease;
    box-shadow: 0 8px 24px rgba(235,51,73,0.35);
}

/* Metric cards */
.metric-card {
    background: rgba(255,255,255,0.04);
    border-radius: 12px;
    padding: 14px;
    text-align: center;
    animation: fadeInUp 0.9s ease;
    border: 1px solid rgba(255,255,255,0.08);
}
.metric-card h3 {
    margin: 0;
    font-size: 1.4rem;
}
.metric-card p {
    margin: 4px 0 0 0;
    opacity: 0.7;
    font-size: 0.85rem;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Load model
# ------------------------------------------------------------------
@st.cache_resource
def load_pipeline():
    return joblib.load("loan_approval_pipeline.pkl")

pipeline = load_pipeline()

# ------------------------------------------------------------------
# Header
# ------------------------------------------------------------------
st.markdown("""
<div class="title-banner">
    <h1>💰 Loan Approval Prediction</h1>
    <p>Fill in your details below to instantly check your loan approval status</p>
</div>
""", unsafe_allow_html=True)

# ------------------------------------------------------------------
# Input Sections
# ------------------------------------------------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("👤 Personal Details")
col1, col2, col3 = st.columns(3)
with col1:
    no_of_dependents = st.number_input("Number of Dependents", min_value=0, value=0)
with col2:
    education = st.selectbox("Education", ["Graduate", "Not Graduate"])
with col3:
    self_employed = st.selectbox("Self Employed", ["Yes", "No"])
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("💵 Loan & Income Details")
col1, col2 = st.columns(2)
with col1:
    income_annum = st.number_input("Annual Income (₹)", min_value=0, step=10000)
    loan_amount = st.number_input("Loan Amount (₹)", min_value=1, step=10000)
with col2:
    loan_term = st.number_input("Loan Term (Months)", min_value=1)
    cibil_score = st.number_input("CIBIL Score", min_value=300, max_value=900, value=700)
st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="section-card">', unsafe_allow_html=True)
st.subheader("🏠 Asset Details")
col1, col2 = st.columns(2)
with col1:
    residential_assets_value = st.number_input("Residential Assets Value (₹)", min_value=0, step=10000)
    commercial_assets_value = st.number_input("Commercial Assets Value (₹)", min_value=0, step=10000)
with col2:
    luxury_assets_value = st.number_input("Luxury Assets Value (₹)", min_value=0, step=10000)
    bank_asset_value = st.number_input("Bank Asset Value (₹)", min_value=0, step=10000)
st.markdown('</div>', unsafe_allow_html=True)

# Encode categorical
education_enc = 1 if education == "Graduate" else 0
self_employed_enc = 1 if self_employed == "Yes" else 0

# ------------------------------------------------------------------
# Predict Button
# ------------------------------------------------------------------
if st.button("🔍 Predict Loan Approval"):

    # Animated progress bar
    progress_text = "Analyzing your application..."
    progress_bar = st.progress(0, text=progress_text)
    for pct in range(0, 101, 10):
        time.sleep(0.03)
        progress_bar.progress(pct, text=progress_text)
    progress_bar.empty()

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

    data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "education": [education_enc],
        "self_employed": [self_employed_enc],
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

        # Try to get probability for extra flair
        proba_text = ""
        try:
            proba = pipeline.predict_proba(data)[0]
            confidence = max(proba) * 100
            proba_text = f"<p style='margin-top:10px; font-size:1rem; opacity:0.9;'>Model Confidence: {confidence:.1f}%</p>"
        except Exception:
            pass

        if prediction[0] == 0:
            st.balloons()
            st.markdown(f"""
            <div class="result-approved">
                ✅ Loan Approved!
                {proba_text}
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="result-rejected">
                ❌ Loan Rejected
                {proba_text}
            </div>
            """, unsafe_allow_html=True)

        # Animated metric summary
        st.markdown("### 📊 Application Summary")
        m1, m2, m3, m4 = st.columns(4)
        with m1:
            st.markdown(f"""
            <div class="metric-card"><h3>₹{total_assets:,.0f}</h3><p>Total Assets</p></div>
            """, unsafe_allow_html=True)
        with m2:
            st.markdown(f"""
            <div class="metric-card"><h3>{loan_income_ratio:.2f}</h3><p>Loan/Income Ratio</p></div>
            """, unsafe_allow_html=True)
        with m3:
            st.markdown(f"""
            <div class="metric-card"><h3>{assets_loan_ratio:.2f}</h3><p>Assets/Loan Ratio</p></div>
            """, unsafe_allow_html=True)
        with m4:
            st.markdown(f"""
            <div class="metric-card"><h3>{emi_income_ratio:.2f}</h3><p>EMI/Income Ratio</p></div>
            """, unsafe_allow_html=True)

        with st.expander("🔧 Raw Model Output"):
            st.write("Raw Prediction:", prediction[0])
            st.dataframe(data)

    except Exception as e:
        st.error(f"Error: {e}")
