# End-to-End Business Intelligence & Customer Value Prediction System
## Project Overview
This project builds a complete Business Intelligence and Predictive Modeling system to measure and predict Customer Value using historical online retail transaction data.
The objective is to:
- Understand customer purchasing behavior
- Segment customers based on value
- Train a machine learning model to predict customer segments
- The segmentation framework used in this project is RFM (Recency, Frequency, Monetary).
---

## Problem Statement
Using historical online retail transaction data:
    - Segment customers based on purchasing behavior and build a predictive model to classify them into value segments (High, Medium, Low) to support better business decisions.
---

## Dataset Description
- The dataset contains transactional data from an online retail store.
- Features:
    -- InvoiceNo – Unique transaction ID (Invoices starting with 'C' indicate cancellations)
    -- StockCode – Product code
    -- Description – Product name
    -- Quantity – Number of units purchased
    -- InvoiceDate – Date and time of transaction
    -- UnitPrice – Price per unit
    -- CustomerID – Unique customer identifier
    -- Country – Customer location
- Total Records: 541,908
- Total Features: 8
---

## Project Workflow

- The project follows a structured end-to-end pipeline:

### Data Understanding & Validation

### Data Cleaning & Preparation

### Business Intelligence (BI) Analysis

### Customer-Level Aggregation

### RFM Feature Engineering

### Customer Segmentation

### Predictive Modeling

### Model Evaluation

### Data Cleaning
The following steps were performed:
- Removed cancelled transactions
- Removed records where Quantity ≤ 0
- Removed records where UnitPrice ≤ 0
- Removed missing CustomerID values
- Converted CustomerID to numeric
- Created a new feature:
    -- Revenue = Quantity × UnitPrice
- After cleaning, the dataset represents only valid completed purchases.

### Business Intelligence Analysis
- Before building the model, exploratory analysis was performed:
- Checked number of unique customers, products, and countries
- Analyzed revenue distribution and identified skewness
- Calculated revenue per customer
- Identified top revenue-generating customers
- Analyzed purchase frequency
- Calculated recency of purchase
- This analysis confirmed that customer value is unevenly distributed and justified segmentation.

### RFM Segmentation
- Customers were segmented using the RFM framework:
    -- Recency → Days since last purchase
    -- Frequency → Number of unique invoices
    -- Monetary → Total revenue per customer

- Each metric was divided into 3 quantile-based scores (1–3).

- `Final RFM Score`:
    -- RFM Score = R_score + F_score + M_score

- `Customer Segments`:
    -- High Value → Score ≥ 7
    -- Medium Value → Score ≥ 5
    -- Low Value → Score < 5
This created labeled customer segments used for model training.


### Model Training
- `Features`:
    -- Recency
    -- Frequency
    -- Monetary

- `Target`:
    -- Customer Segment (High / Medium / Low)
---

### Steps performed:
- Encoded target variable
- Train-test split
- 5-fold cross validation
- Trained Logistic Regression model
- Evaluated using precision, recall, F1-score
---

### Why Logistic Regression?
- Logistic Regression was chosen because:
- This is a classification problem
- Only 3 numeric behavioral features are used
- Relationship between RFM features and segments is structured
- Dataset size is moderate (~4300 customers)
- Provides good interpretability
- Acts as a strong baseline model
- Shows low variance and stable generalization
- More complex models like XGBoost were not required due to the structured nature of segmentation.
---

### Model Performance
- Accuracy: ~88%
- Balanced precision and recall across segments
- Low variance (train and test performance consistent)
- Cross-validation confirmed stable model performance.
---

### Project Structure
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
│   ├── model.py
│
├── models/
│
├── app/
│   └── app.py
│
├── main.py
├── requirements.txt
└── README.md
---

### Deployment
- A simple Streamlit application was created to:
- Input Recency, Frequency, Monetary values
- Predict customer segment
- Display predicted value category
- The model and encoder are saved and loaded using environment variables for deployment flexibility.
---

### Key Learnings
- Importance of data cleaning before modeling
- Role of BI in justifying segmentation
- Practical implementation of RFM framework
- Understanding bias–variance tradeoff in model selection
- Building modular, industry-style project structure
- Deploying ML models using Streamlit
---

### Conclusion
- This project demonstrates a complete end-to-end pipeline:
- From raw transactional data → business analysis → segmentation → predictive modeling → deployment.
- It reflects both business reasoning and technical implementation for customer value prediction.
---