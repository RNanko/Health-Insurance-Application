
# Health Insurance Prediction App

## Table of Contents
- [Project Overview](#project-overview)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Machine Learning Process](#machine-learning-process)
    - [Model Evaluation](#model-evaluation)
    - [Feature Importance](#feature-importance)
- [Application (Tkinter + ttkbootstrap)](#application-tkinter--ttkbootstrap)
- [Results](#results)
- [Future Improvements](#future-improvements)
- [Useful References](#useful-references)

---

## **Project Overview**
Our goal is to develop a **machine learning model** that can accurately predict **health insurance charges** based on personal and medical attributes.

### **Key Steps:**
✔ Explore Health Insurance dataset, get the key insight.
✔ Train multiple ML models to predict health insurance chareges and select the best one. 
✔ Build application.
✔ Deploy the model in a **Tkinter-based GUI application** using `ttkbootstrap`.  
✔ Handle **input validation** for user-friendly interaction.  

---

## **Exploratory Data Analysis (EDA)**
The dataset contains **1,338** records of insured individuals, including features such as:
- **Age**, **BMI**, **Number of children**, **Smoking habits**, **Region**, **Sex**
- **Target variable** → `charges` (insurance cost)

**Dataset Insights:**

✔ Age range: **18–64 years**  
✔ Dependents range: **0–5**  
✔ Average charges: **$13,270.42** (Min: **$4,740.28** | Max: **$63,770.42**)  

There are **no missing values** in the dataset.

![Dataset Preview](https://github.com/RNanko/Health-Insurance-Application/blob/main/Visualizations/head(10).png)

To better understand feature distributions, an **interactive dashboard** was created:  
![Dashboard](https://github.com/RNanko/Health-Insurance-Application/blob/main/Visualizations/Dashboard.png)

---

## **Machine Learning Process**

### **Data Preparation**
- **One-Hot Encoding** → For categorical features (`sex`, `region`).
- **Label Encoding** → For ordinal features (`smoker`).
- **Correlation Analysis** → Identified **smoker, BMI, and age** as the most significant predictors.

 **Correlation Matrix:**
![Feature Correlation](https://github.com/RNanko/Health-Insurance-Application/blob/main/Visualizations/Data%20corelation.png)

---

### **Model Evaluation**
We tested three different regression models:
 -**Random Forest Regressor**  
 -**Ridge Regression**  
 -**Gradient Boosting Regressor**  

Since **Random Forest and Gradient Boosting performed the best**, we **combined them into a Stacking Regressor** for improved accuracy.

**Model Performance Comparison:**
![Model Scores](https://github.com/RNanko/Health-Insurance-Application/blob/main/Visualizations/Models%20Scores%20Comparison.png)

✔ **Stacking Regressor R² Score** → **0.8807 (Best performance)**  
✔ **Mean Absolute Error (MAE)** → **$2,425.33**  
✔ **Root Mean Square Error (RMSE)** → **$4,302.92**  

---

### **Feature Importance**
Using feature importance analysis, we identified the **most influential variables** affecting insurance charges.

**Top Features Impacting Insurance Charges:**
![Feature Importance](https://github.com/RNanko/Health-Insurance-Application/blob/main/Visualizations/Most%20important%20feature.png)

**Smoker status and BMI** are the strongest predictors.

---

## **Application (Tkinter + ttkbootstrap)**
We developed a **Tkinter-based GUI** using `ttkbootstrap`, which allows users to:
✔ Input personal details.  
✔ Validate inputs in real-time (e.g., incorrect age format alerts).  
✔ Get instant insurance charge predictions.  

### **Application Features:**
 -**User-friendly interface with ttkbootstrap**  
 -**Handles input errors with warnings**  
 -**Displays predictions instantly**  

---

## **Results**
**Our final application accurately predicts health insurance costs.**  
**Working demo:** 

https://github.com/user-attachments/assets/edf508ac-0aa4-49dc-aa09-cf3048983f5b

Project demonstrates how **machine learning models** can automate pricing calculations, reducing **manual work and improving accuracy**.

---

## **Future Improvements**
To further enhance the model’s accuracy, we could add:
🔹 **Additional features** (e.g., Salary, Job type, Marital status).  
🔹 **Better handling of outliers** in insurance charges.  
🔹 **Integration with a database** for storing past predictions.  

---

## **Useful References**
**Dataset Source:** [Kaggle - US Health Insurance Dataset](https://www.kaggle.com/datasets/teertha/ushealthinsurancedataset/data)
---
Thank you for your time!
