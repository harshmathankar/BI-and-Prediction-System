import streamlit as st
import joblib
import numpy as np

model = joblib.load("models/logistic_model.pkl")
encoder = joblib.load("models/label_encoder.pkl")

st.title("Customer Value Prediction")

recency = st.number_input("Recency (days)")
frequency = st.number_input("Frequency")
monetary = st.number_input("Monetary")

if st.button("Predict"):
    prediction = model.predict([[recency, frequency, monetary]])
    segment = encoder.inverse_transform(prediction)
    st.success(f"Predicted Segment: {segment[0]}")