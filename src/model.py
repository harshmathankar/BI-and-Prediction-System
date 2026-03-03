import os
import numpy as np
from dotenv import load_dotenv
import joblib
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

def train_model(rfm):
    X = rfm[['Recency', 'Frequency', 'Monetary']]
    y = rfm['Segment']

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # Split the data into training and testing
    X_train, X_test, y_train, y_test = train_test_split( X, y_encoded, test_size=0.2, random_state=42 )

    model = LogisticRegression(max_iter=1000)

    # 5 - fold Cross Validation
    cv_scores = cross_val_score(model, X, y_encoded, cv=5)
    print("K-Fold Cross Validation Scores:", cv_scores)
    print("Mean CV Accuracy:", np.mean(cv_scores))
    print("Standard Deviation:", np.std(cv_scores))

    model.fit(X_train, y_train)

    # Evaluate the model
    y_pred = model.predict(X_test)
    print(classification_report(y_test, y_pred))

    return model, le

def save_model(model, encoder):
    load_dotenv()

    model_path = os.getenv("MODEL_PATH")
    encoder_path = os.getenv("ENCODER_PATH")

    joblib.dump(model, model_path)
    joblib.dump(encoder, encoder_path)