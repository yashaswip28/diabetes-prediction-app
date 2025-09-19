import streamlit as st
import numpy as np
import joblib

# Load model and scaler
model = joblib.load('../backend/diabetes_model.pkl')
scaler = joblib.load('../backend/scaler.pkl')

st.title("🩺 Diabetes Risk Predictor")
st.write("Enter your health details to assess your diabetes risk.")

# Input fields
age = st.number_input("Age", min_value=1, max_value=120)
bmi = st.number_input("BMI", min_value=10.0, max_value=60.0)
hba1c = st.number_input("HbA1c Level", min_value=3.0, max_value=15.0)
glucose = st.number_input("Blood Glucose Level", min_value=50.0, max_value=300.0)

gender = st.selectbox("Gender", ["Male", "Female", "Other"])
smoking = st.selectbox("Smoking History", ["never", "former", "current", "ever", "not current", "No Info"])

hypertension = st.selectbox("Hpertension",["Yes", "No"])
heart_disease = st.selectbox("Heart Disease", ["Yes","No"])

# Encode categorical inputs
gender_map = {"Male": 1, "Female": 0, "Other": 2}
smoking_map = {"No Info": 0, "current": 1, "ever": 2, "former": 3, "never": 4, "not current": 5}
hypertension_map = {"Yes":1, "No":0}
heart_disease_map = {"Yes":1, "No":0}

input_data = np.array([[age, bmi, hba1c, glucose, gender_map[gender], smoking_map[smoking], hypertension_map[hypertension], heart_disease_map[heart_disease]]])
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("⚠️ High risk of diabetes. Please consult a doctor.")
    else:
        st.success("✅ Low risk of diabetes. Keep up the healthy habits!")
