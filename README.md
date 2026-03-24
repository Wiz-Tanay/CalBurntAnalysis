# 🔥 Calorie Burnt Analysis using Machine Learning

## 🌐 Live Web App

👉 https://wiztan-cal-burnt-analysis.streamlit.app/

> Try the app by entering your details and instantly get a prediction of calories burned along with health insights.

---

## 📌 Project Overview

This project focuses on predicting the number of calories burned based on user-related features such as gender, age, physical attributes, and exercise data. Multiple machine learning models were trained and compared to identify the most effective approach.

The final model is deployed as an interactive web application using Streamlit, allowing real-time predictions.

---

## 🎯 Objectives

* Perform data preprocessing and cleaning
* Train multiple machine learning models
* Evaluate and compare model performance
* Deploy the best model as a web application

---

## 📂 Dataset

* File used: `calories.csv`

* Contains features like:

  * Gender
  * Age
  * Height
  * Weight
  * Duration
  * Heart Rate
  * Body Temperature

* Target variable:

  * **Calories burned**

---

## ⚙️ Data Preprocessing

* Removed unnecessary column: `User_ID`
* Encoded categorical feature:

  * Gender → Male = 1, Female = 0
* Train-test split (80:20)

---

## 🧠 Models Implemented

* Linear Regression
* Random Forest Regressor
* XGBoost Regressor

---

## 📊 Model Evaluation

Models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

A comparison of all models was performed to determine the best-performing one.

---

## 🏆 Conclusion

* Ensemble models like **Random Forest** and **XGBoost** outperformed Linear Regression
* These models handle non-linear relationships more effectively

---

## 💻 Web Application Features

* Interactive input form for user data
* Real-time calorie prediction
* Activity level classification
* BMI calculation and health insights
* Clean and user-friendly interface

> The app is built using Streamlit, a framework that enables quick development of interactive ML web apps ([Medium][1])

---

## 📁 Project Structure

```
CalBurntAnalysis/
│
├── CalBurntAnalysis.ipynb
├── calorie_model.pkl
├── app.py
├── calories.csv
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run Locally

1. Clone the repository:

```
git clone https://github.com/Wiz-Tanay/CalBurntAnalysis.git
cd CalBurntAnalysis
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Run the app:

```
streamlit run app.py
```

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Enhanced UI/UX design
* Mobile optimization
* Integration with real-time fitness trackers

---

## 👨‍💻 Author

Tanay Pandey

[1]: https://medium.com/%40t21016/revolutionize-your-data-analysis-with-streamlit-an-interactive-web-app-for-analyzing-huge-nwh-data-5640d2f12e78?utm_source=chatgpt.com "Revolutionize Your Data Analysis with Streamlit"
