# End-to-End Business Intelligence & Customer Value Prediction System

## Demo
[Click here to try the live app](https://bi-and-prediction-system.streamlit.app/)

---

## Project Overview

This project builds a complete **Business Intelligence and Predictive Modeling system** to measure and predict Customer Value using historical online retail transaction data.

**Objectives:**
- Understand customer purchasing behavior
- Segment customers based on value
- Train a machine learning model to predict customer segments

> The segmentation framework used in this project is **RFM (Recency, Frequency, Monetary)**.

---

## Problem Statement

Using historical online retail transaction data — segment customers based on purchasing behavior and build a predictive model to classify them into value segments (**High, Medium, Low**) to support better business decisions.

---

## Dataset Description

The dataset contains transactional data from an online retail store.

| Feature | Description |
|---|---|
| `InvoiceNo` | Unique transaction ID *(invoices starting with 'C' indicate cancellations)* |
| `StockCode` | Product code |
| `Description` | Product name |
| `Quantity` | Number of units purchased |
| `InvoiceDate` | Date and time of transaction |
| `UnitPrice` | Price per unit |
| `CustomerID` | Unique customer identifier |
| `Country` | Customer location |

- **Total Records:** 541,908
- **Total Features:** 8

---

## Project Workflow

The project follows a structured end-to-end pipeline across the following stages:

```
Data Understanding & Validation
        ↓
Data Cleaning & Preparation
        ↓
Business Intelligence (BI) Analysis
        ↓
Customer-Level Aggregation
        ↓
RFM Feature Engineering
        ↓
Customer Segmentation
        ↓
Predictive Modeling
        ↓
Model Evaluation
```

---

## 1. Data Cleaning

The following steps were performed to retain only valid, completed purchases:

- Removed cancelled transactions *(InvoiceNo starting with 'C')*
- Removed records where `Quantity ≤ 0`
- Removed records where `UnitPrice ≤ 0`
- Removed missing `CustomerID` values
- Converted `CustomerID` to numeric
- Engineered a new feature:

$$\text{Revenue} = \text{Quantity} \times \text{UnitPrice}$$

---

## 2. Business Intelligence Analysis

Exploratory analysis was performed before model building to understand the data and justify segmentation:

- Checked the number of unique customers, products, and countries
- Analyzed revenue distribution and identified skewness
- Calculated revenue per customer
- Identified top revenue-generating customers
- Analyzed purchase frequency
- Calculated recency of purchase

> This analysis confirmed that **customer value is unevenly distributed**, which justified segmentation.

---

## 3. RFM Segmentation

Customers were segmented using the RFM framework:

| Metric | Definition |
|---|---|
| **Recency (R)** | Days since last purchase |
| **Frequency (F)** | Number of unique invoices |
| **Monetary (M)** | Total revenue per customer |

Each metric was divided into **3 quantile-based scores (1–3)**.

**Final RFM Score:**

$$\text{RFM Score} = R\_score + F\_score + M\_score$$

**Customer Segments:**

| Segment | Condition |
|---|---|
| 🟢 High Value | RFM Score ≥ 7 |
| 🟡 Medium Value | RFM Score ≥ 5 |
| 🔴 Low Value | RFM Score < 5 |

These labeled segments were used as the target variable for model training.

---

## 4. Model Training

### Features & Target

| Type | Variables |
|---|---|
| **Features (X)** | Recency, Frequency, Monetary |
| **Target (y)** | Customer Segment (High / Medium / Low) |

### Steps Performed

1. Encoded the target variable
2. Train-test split
3. 5-fold cross-validation
4. Trained **Logistic Regression** model
5. Evaluated using precision, recall, and F1-score

### Why Logistic Regression?

Logistic Regression was selected for the following reasons:

- This is a **classification problem**
- Only **3 numeric behavioral features** are used
- The relationship between RFM features and segments is **structured and linear**
- Dataset size is moderate (~4,300 customers)
- Offers **high interpretability**
- Acts as a **strong baseline model**
- Exhibits **low variance** and stable generalization

> More complex models like XGBoost were not required due to the structured nature of the segmentation.

---

## 5. Model Performance

| Metric | Result |
|---|---|
| **Accuracy** | ~88% |
| **Precision** | Balanced across segments |
| **Recall** | Balanced across segments |
| **F1-Score** | Balanced across segments |
| **Variance** | Low — train/test performance consistent |
| **Cross-Validation** | Confirmed stable model performance |

---

## 6. Project Structure

```
customer-value-segmentation/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data_cleaning.py
│   ├── rfm.py
│   └── model.py
│
├── models/
│
├── app/
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 7. Deployment

A **Streamlit application** was built for real-time inference:

- Input **Recency, Frequency, Monetary** values
- Predict customer segment
- Display predicted value category

The model and encoder are saved and loaded using **environment variables** for deployment flexibility.

---

## Key Learnings

- Importance of thorough **data cleaning** before modeling
- Role of **BI analysis** in justifying segmentation decisions
- Practical implementation of the **RFM framework**
- Understanding the **bias–variance tradeoff** in model selection
- Building a **modular, industry-style project structure**
- Deploying ML models using **Streamlit**

---

## Conclusion

This project demonstrates a complete end-to-end pipeline:

**Raw transactional data → Business Analysis → Segmentation → Predictive Modeling → Deployment**

It reflects both **business reasoning** and **technical implementation** for customer value prediction.
