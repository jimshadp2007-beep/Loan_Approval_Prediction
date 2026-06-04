# 🏦 Loan Approval Prediction Using Machine Learning

## 📌 Project Overview

This project predicts whether a loan application will be approved or rejected based on applicant information such as income, education, credit history, loan amount, and other relevant factors.

The project follows a complete Machine Learning workflow including:

- Problem Definition
- Data Collection
- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Model Training & Evaluation
- Hyperparameter Tuning
- Pipeline Integration
- Model Serialization
- Streamlit Deployment

---

## 🎯 Problem Statement

Financial institutions receive thousands of loan applications every year. Manually evaluating each application can be time-consuming and prone to errors.

This project develops a Machine Learning model capable of predicting loan approval decisions based on historical applicant data.

### Target Variable

**Loan_Status**

- 1 → Approved
- 0 → Rejected

---

## 📊 Dataset Information

**Source:** Kaggle Loan Approval Dataset

### Features

- Gender
- Married
- Dependents
- Education
- Self Employed
- Applicant Income
- Coapplicant Income
- Loan Amount
- Loan Amount Term
- Credit History
- Property Area

---

## 🔍 Exploratory Data Analysis (EDA)

The following analyses were performed:

- Data distribution visualization
- Missing value analysis
- Correlation heatmap
- Outlier detection
- Class distribution analysis

### Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

---

## 🧹 Data Preprocessing

The following preprocessing techniques were applied:

- Missing value handling
- Categorical encoding
- Feature scaling
- SMOTE for class balancing

---

## 🤖 Machine Learning Models

The following models were trained and compared:

1. Logistic Regression
2. Decision Tree Classifier
3. Random Forest Classifier

### Evaluation Metrics

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC Score

---

## ⚙️ Hyperparameter Tuning

Hyperparameter optimization was performed using:

- GridSearchCV
- Cross Validation

The best-performing parameters were selected for the final model.

---

## 🔄 Pipeline Integration

A Scikit-Learn Pipeline was created using:

- ColumnTransformer
- StandardScaler
- OneHotEncoder
- Random Forest Classifier

This prevents data leakage and automates the entire prediction workflow.

---

## 💾 Model Export

The final trained pipeline was saved using Joblib.

```python
joblib.dump(pipeline, "loan_approval_pipeline.pkl")
```

Generated file:

```text
loan_approval_pipeline.pkl
```

---

## 🌐 Streamlit Deployment

The project includes a Streamlit web application that allows users to:

- Enter applicant details
- Generate predictions instantly
- View loan approval results in real time

Run the application:

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```text
Loan-Approval-Prediction/
│
├── Loan_Approval_Prediction.ipynb
├── app.py
├── loan_approval_pipeline.pkl
├── README.md
└── requirements.txt
```

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Imbalanced-Learn (SMOTE)
- Joblib
- Streamlit

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Loan-Approval-Prediction.git
```

Move into the project directory:

```bash
cd Loan-Approval-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
streamlit run app.py
```

---

## 📈 Results

The final model achieved strong classification performance and was selected based on comparison with multiple machine learning algorithms and hyperparameter tuning.

---

## 👥 Team Members

- jimshad
- ashik 
- anshad
- afshan


---
