# 🏥 Insurance Cost Prediction (Machine Learning Project)

## 📌 Project Overview

This project focuses on predicting **medical insurance charges** based on user attributes such as age, BMI, smoking habits, and region using Machine Learning models.

The goal is to analyze key factors affecting insurance costs and build an accurate predictive model.

---

## 🌐 Live Demo

👉 https://insurance-charges-predictor-premkumark.streamlit.app/

---

## 🎯 Objectives

* Analyze factors affecting insurance charges
* Perform data preprocessing and feature engineering
* Build multiple regression models
* Evaluate model performance using metrics
* Deploy the best model for real-time prediction

---

## ⚙️ Tech Stack

* **Language:** Python
* **Libraries:**

  * Pandas & NumPy → Data processing
  * Matplotlib & Seaborn → Visualization
  * Scikit-learn → Machine Learning models
  * SciPy → Statistical analysis
  * Joblib → Model saving

---

## 📊 Features of the Project

---

### 🔹 1. Data Analysis & Visualization

* Dataset exploration using:

  * `.info()`, `.describe()`, `.isnull()`
* Visualizations:

  * Histograms (distribution)
  * Boxplots (outliers)
  * Countplots (categorical features)
  * Heatmap (correlation)

---

### 🔹 2. Data Preprocessing

* Removed duplicate records
* Converted categorical features:

  * `sex → is_female`
  * `smoker → is_smoker`
* Applied one-hot encoding:

  * `region`
  * `bmi_category`
* Feature scaling using **StandardScaler**

---

### 🔹 3. Feature Engineering

* Created BMI categories:

  * Underweight
  * Normal
  * Overweight
  * Obese

---

### 🔹 4. Statistical Analysis

* ✔️ **Pearson Correlation**

  * Identified relationships between numerical features and target

* ✔️ **Chi-Square Test**

  * Applied on categorical features
  * Selected significant features based on p-value

---

### 🔹 5. Model Building

Models used:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor ✅ (Best Model)
* Gradient Boosting Regressor
* K-Nearest Neighbors (KNN)

---

### 🔹 6. Model Evaluation

Metrics used:

* MAE (Mean Absolute Error)
* RMSE (Root Mean Squared Error)
* R² Score
* Adjusted R² Score

---

### 🔹 7. Final Model Selection

* **Random Forest Regressor** selected as final model
* Trained with optimized parameters:

  * `n_estimators = 200`
  * `random_state = 42`

---

## 🔄 Workflow

* Data Collection
* Data Cleaning & Preprocessing
* Feature Engineering
* Statistical Analysis
* Model Training
* Model Evaluation
* Model Selection
* Deployment

---

## 📈 Key Insights

* Smoking significantly increases insurance charges
* BMI and age strongly influence costs
* Feature engineering improves model performance
* Random Forest provides the best accuracy and stability

---

## 🚀 Future Improvements

* Hyperparameter tuning (Grid Search / Random Search)
* Use advanced models (XGBoost, LightGBM)
* Improve feature engineering
* Enhance UI/UX of the web app
* Deploy using scalable cloud services

---

## 🙌 Conclusion

This project demonstrates how **Machine Learning can be used to predict real-world financial outcomes**, helping users estimate insurance costs based on personal and health-related factors.

---
