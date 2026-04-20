🏥 Insurance Cost Prediction (Machine Learning Project)
📌 Project Overview

This project predicts medical insurance charges based on user attributes like age, BMI, smoking habits, and region using Machine Learning models.

The goal is to analyze key factors affecting insurance costs and build a model that can accurately estimate charges.

## 🌐 Live Demo

Access the deployed application here:

👉 https://insurance-charges-predictor-premkumark.streamlit.app/
⚙️ Tech Stack
Python
Pandas & NumPy → Data processing
Matplotlib & Seaborn → Data visualization
Scikit-learn → ML models & preprocessing
SciPy → Statistical analysis
Joblib → Model saving
📊 Features of the Project
1️⃣ Data Analysis & Visualization
Dataset exploration using:
.info(), .describe(), .isnull()
Visualizations:
Histograms (distribution)
Boxplots (outliers)
Countplots (categorical data)
Heatmap (correlation)
2️⃣ Data Preprocessing
Removed duplicate records
Converted categorical features:
sex → is_female
smoker → is_smoker
One-hot encoding:
region
bmi_category
Feature scaling using StandardScaler
3️⃣ Feature Engineering
Created BMI categories:
Underweight
Normal
Overweight
Obese
4️⃣ Statistical Analysis
✔️ Pearson Correlation
Used to find relationship between numerical features and target (charges)
✔️ Chi-Square Test
Applied on categorical features
Selected only significant features based on p-value
5️⃣ Model Building

Models used:

Linear Regression
Decision Tree Regressor
Random Forest Regressor ✅ (Best Model)
Gradient Boosting Regressor
K-Nearest Neighbors
6️⃣ Model Evaluation

Metrics used:

MAE (Mean Absolute Error)
RMSE (Root Mean Squared Error)
R² Score
Adjusted R² Score
7️⃣ Final Model Selection
Random Forest Regressor selected as final model
Trained with optimized parameters:
n_estimators = 200
random_state = 42
