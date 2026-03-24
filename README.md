# 🔥 Calorie Burnt Analysis using Machine Learning

## 📌 Project Overview

This project focuses on predicting the number of calories burned based on user-related features such as gender, physical attributes, and activity data. Multiple regression models are trained and compared to identify the most effective model.

---

## 🎯 Objectives

* Clean and preprocess the dataset
* Train multiple machine learning models
* Evaluate models using regression metrics
* Compare performance to determine the best model

---

## 📂 Dataset

* File used: `calories.csv`
* The dataset contains features related to user activity and physical parameters.
* The target variable is:

  * **Calories burned**

---

## ⚙️ Data Preprocessing

* Removed unnecessary column: `User_ID`
* Encoded categorical feature:

  * `Gender` → Male = 1, Female = 0
* Split data into training and testing sets (80:20 ratio)

---

## 🧠 Models Implemented

1. **Linear Regression**
2. **Random Forest Regressor**
3. **XGBoost Regressor**

---

## 📊 Model Evaluation Metrics

Each model is evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

A reusable evaluation function is implemented for consistency across models.

---

## 📈 Visualization

* Scatter plots of:

  * Actual vs Predicted values
* Helps in visually analyzing model performance

---

## 📊 Model Comparison

A comparison table is created showing:

* MAE
* RMSE
* R² Score

This allows direct comparison of all models.

---

## 🏆 Conclusion

* Ensemble models like **Random Forest** and **XGBoost** generally perform better than Linear Regression.
* These models capture non-linear relationships more effectively.

---

## 📁 Project Structure

```
calorie-burnt-analysis/
│
├── CalBurntAnalysis.ipynb
├── calories.csv
├── requirements.txt
└── README.md
```

---

## 🚀 How to Run

1. Clone the repository:

```
git clone https://github.com/your-username/calorie-burnt-analysis.git
cd calorie-burnt-analysis
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Launch Jupyter Notebook:

```
jupyter notebook
```

4. Open:

```
CalBurntAnalysis.ipynb
```

---

## 📌 Future Improvements

* Hyperparameter tuning for better accuracy
* Feature engineering for improved predictions
* Deployment using Streamlit or Flask
* Integration with real-time fitness tracking data

---

## 👨‍💻 Author

Tanay Pandey
