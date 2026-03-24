import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Calorie Burn Predictor", layout="centered")

model = joblib.load("calorie_model.pkl")

st.markdown("<h1 style='text-align: center;'>🔥 Calorie Burn Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Track your workout impact instantly</p>", unsafe_allow_html=True)

st.divider()

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 1, 100)

with col2:
    height = st.number_input("Height (cm)")
    weight = st.number_input("Weight (kg)")

st.divider()

st.subheader("🏃 Activity Details")

col3, col4 = st.columns(2)

with col3:
    duration = st.number_input("Duration (minutes)")
    heart_rate = st.number_input("Heart Rate")

with col4:
    body_temp = st.number_input("Body Temperature (°C)")

st.divider()

gender_val = 1 if gender == "Male" else 0

if st.button("🔥 Predict Calories Burned"):

    input_data = np.array([[gender_val, age, height, weight, duration, heart_rate, body_temp]])
    prediction = model.predict(input_data)[0]

    st.subheader("📊 Results")

    st.metric("Calories Burned", f"{prediction:.2f}")

    progress_val = min(int(prediction / 500 * 100), 100)
    st.progress(progress_val)

    if prediction < 200:
        level = "Light Activity"
    elif prediction < 400:
        level = "Moderate Activity"
    else:
        level = "High Intensity 🔥"

    st.info(f"Activity Level: {level}")

    bmi = weight / ((height / 100) ** 2)
    st.metric("BMI", f"{bmi:.2f}")

    if bmi < 18.5:
        st.warning("Underweight - consider a balanced diet")
    elif bmi < 25:
        st.success("Healthy BMI - keep it up!")
    else:
        st.warning("Overweight - consider regular exercise")

    st.divider()

    st.success("💡 Stay consistent. Fitness is a journey, not a race!")
