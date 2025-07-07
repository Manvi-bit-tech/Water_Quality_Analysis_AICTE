
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
import xgboost

# Page configuration
st.set_page_config(page_title="Water Quality Predictor", page_icon="💧", layout="centered")

# Load model and scaler safely
@st.cache_resource
def load_model_and_scaler():
    try:
        model = joblib.load("stacking_model.pkl")
        scaler = joblib.load("scaler.pkl")
        return model, scaler
    except Exception as e:
        st.error("❌ Failed to load model or scaler. Please check your files.")
        st.stop()

model, scaler = load_model_and_scaler()

# Custom CSS for background and button styling
st.markdown("""
    <style>
        .main {
            background-color: #f0f8ff;
        }
        .stButton>button {
            background-color: #0077b6;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5em 1em;
        }
        footer {visibility: hidden;}
    </style>
""", unsafe_allow_html=True)



st.markdown("""
<div style='text-align: center; padding: 10px 0'>
    <h1 style='color: #0077b6;'>💧 Water Quality Predictor</h1>
    <h4 style='color: #023e8a;'>Predict O₂, BSK5, and Suspended solids using water chemistry data</h4>
    <p style='font-size:16px;'>Powered by a Stacking ML Model · Created by <b>Manvi Dhamija</b></p>
</div>
""", unsafe_allow_html=True)

# 📥 Input fields in sidebar
st.sidebar.header("Enter Water Sample Measurements")
nh4 = st.sidebar.number_input("NH4 (mg/L)", 0.0, 100.0, 1.0)
no3 = st.sidebar.number_input("NO3 (mg/L)", 0.0, 100.0, 1.0)
no2 = st.sidebar.number_input("NO2 (mg/L)", 0.0, 100.0, 1.0)
so4 = st.sidebar.number_input("SO4 (mg/L)", 0.0, 100.0, 1.0)
po4 = st.sidebar.number_input("PO4 (mg/L)", 0.0, 100.0, 1.0)
cl  = st.sidebar.number_input("CL (mg/L)",  0.0, 100.0, 1.0)

#  Prediction logic
if st.sidebar.button("🔍 Predict Water Quality"):
    try:
        input_data = pd.DataFrame([[nh4, no3, no2, so4, po4, cl]],
                                  columns=['NH4', 'NO3', 'NO2', 'SO4', 'PO4', 'CL'])

        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)[0]
        labels = ['O₂ (mg/L)', 'BSK5 (mg/L)', 'Suspended Solids (mg/L)']

        st.success("✅ Prediction Complete!")
        st.subheader("📈 Predicted Pollutant Levels:")
        st.bar_chart(pd.DataFrame([prediction], columns=labels ))
        
        for label, value in zip(labels, prediction):
            st.markdown(f"🔹 **{label}:** `{value:.2f}`")
    except Exception as e:
        st.error(f"⚠️ Prediction failed: {str(e)}")

#  Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size:14px;'>© 2025 Manvi Dhamija · All Rights Reserved</p>", unsafe_allow_html=True)
