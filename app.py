import streamlit as st
import numpy as np
import joblib
import time

st.set_page_config(page_title="Calorie Burn Predictor", layout="centered")

from xgboost import XGBRegressor
model = XGBRegressor()
model.load_model("model.json")

st.markdown("<h1 style='text-align: center;'>🔥 Calorie Burn Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Track your workout impact instantly</p>", unsafe_allow_html=True)

st.divider()

st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age", 1, 100)

with col2:
    height = st.number_input("Height (cm)", min_value=1.0)
    weight = st.number_input("Weight (kg)", min_value=1.0)

st.divider()

st.subheader("🏃 Activity Details")

col3, col4 = st.columns(2)

with col3:
    duration = st.number_input("Duration (minutes)", min_value=1.0)
    heart_rate = st.number_input("Heart Rate", min_value=1.0)

with col4:
    body_temp = st.number_input("Body Temperature (°C)", min_value=30.0)

st.divider()

gender_val = 1 if gender == "Male" else 0

if st.button("🔥 Predict Calories Burned"):

    # 🔒 Input validation
    if height <= 0 or weight <= 0:
        st.error("Height and Weight must be greater than 0")
    elif heart_rate < 40 or heart_rate > 200:
        st.warning("Heart rate seems unrealistic. Please check.")
    elif body_temp < 30 or body_temp > 45:
        st.warning("Body temperature seems incorrect.")
    else:
        try:
            # ⏳ Loading animation
            with st.spinner("Calculating calories burned..."):
                time.sleep(1.5)

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

            # 🧠 BMI Calculation
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

        except Exception as e:
            st.error("Something went wrong during prediction.")
            st.text(str(e))
