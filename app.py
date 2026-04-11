import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load model, scaler, columns
# -----------------------------
try:
    model = joblib.load("model.pkl")
    scaler = joblib.load("scaler.pkl")
    columns = joblib.load("columns.pkl")
except Exception as e:
    st.error(f"❌ Error loading files: {e}")
    st.stop()

# -----------------------------
# Page config
# -----------------------------
st.set_page_config(page_title="Insurance Charges Predictor", layout="centered")

st.title("💰 Insurance Charges Predictor")

# -----------------------------
# User Inputs
# -----------------------------
age = st.number_input("Age", min_value=18, max_value=100, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", min_value=10.0, max_value=50.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["No", "Yes"])
region = st.selectbox("Region Southeast", ["No", "Yes"])

# Auto-generate BMI category (more realistic)
bmi_obese = 1 if bmi >= 30 else 0

# -----------------------------
# Convert inputs (MATCH TRAINING)
# -----------------------------
input_dict = {
    "age": age,
    "is_female": 1 if gender == "Female" else 0,
    "bmi": bmi,
    "children": children,
    "is_smoker": 1 if smoker == "Yes" else 0,
    "region_southeast": 1 if region == "Yes" else 0,
    "bmi_category_Obese": bmi_obese
}

# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):
    try:
        # Convert to DataFrame
        input_df = pd.DataFrame([input_dict])

        # Ensure correct column order
        input_df = input_df[columns]

        # Scale input (VERY IMPORTANT)
        input_scaled = scaler.transform(input_df)

        # Predict
        prediction = model.predict(input_scaled)[0]

        st.success(f"💸 Estimated Charges: ₹ {round(prediction, 2)}")

    except Exception as e:
        st.error(f"❌ Prediction Error: {e}")