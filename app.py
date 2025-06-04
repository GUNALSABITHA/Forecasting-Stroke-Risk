import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load('stroke_model.pkl')
scaler = joblib.load('scaler.pkl')
label_encoders = joblib.load('label_encoders.pkl')

st.title("🧠 Stroke Risk Predictor")

# Input fields
gender = st.selectbox("Gender", ['Male', 'Female', 'Other'])
age = st.slider("Age", 0, 100, 30)
hypertension = st.selectbox("Hypertension", ['No', 'Yes'])
heart_disease = st.selectbox("Heart Disease", ['No', 'Yes'])
ever_married = st.selectbox("Ever Married", ['No', 'Yes'])
work_type = st.selectbox("Work Type", ['Govt_job', 'Never_worked', 'Private', 'Self-employed'])
residence_type = st.selectbox("Residence Type", ['Urban', 'Rural'])
avg_glucose_level = st.number_input("Average Glucose Level", 50.0, 300.0, 100.0)
bmi = st.number_input("BMI", 10.0, 50.0, 25.0)
smoking_status = st.selectbox("Smoking Status", ['formerly smoked', 'never smoked', 'smokes', 'Unknown'])

def safe_encode(encoder, value, fallback=0):
    try:
        return encoder.transform([value])[0]
    except ValueError:
        return fallback  # fallback to a default encoded value

input_dict = {
    'gender': safe_encode(label_encoders['gender'], gender),
    'age': age,
    'hypertension': 1 if hypertension == 'Yes' else 0,
    'heart_disease': 1 if heart_disease == 'Yes' else 0,
    'ever_married': safe_encode(label_encoders['ever_married'], ever_married),
    'work_type': safe_encode(label_encoders['work_type'], work_type),
    'Residence_type': safe_encode(label_encoders['Residence_type'], residence_type),
    'avg_glucose_level': avg_glucose_level,
    'bmi': bmi,
    'smoking_status': safe_encode(label_encoders['smoking_status'], smoking_status)
}


# Convert to DataFrame and scale
input_df = np.array([list(input_dict.values())])
input_scaled = scaler.transform(input_df)

# Predict
if st.button("Predict Stroke Risk"):
    prediction = model.predict(input_scaled)[0]
    if prediction == 1:
        st.error("⚠️ High risk of stroke. Consult a doctor immediately.")
    else:
        st.success("✅ Low risk of stroke. Stay healthy!")
