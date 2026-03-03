import pandas as pd

def create_rfm(df):
    reference_date = df['InvoiceDate'].max()

    recency = (reference_date - df.groupby('CustomerID')['InvoiceDate'].max()).dt.days
    frequency = df.groupby('CustomerID')['InvoiceNo'].nunique()
    monetary = df.groupby('CustomerID')['Revenue'].sum()

    rfm = pd.DataFrame({
        'Recency': recency,
        'Frequency': frequency,
        'Monetary': monetary
    })

    return rfm

def segment_customers(rfm):
    rfm['R_score'] = pd.qcut(rfm['Recency'], 3, labels=[3,2,1])
    rfm['F_score'] = pd.qcut(rfm['Frequency'].rank(method = 'first'), 3, labels=[1,2,3])
    rfm['M_score'] = pd.qcut(rfm['Monetary'], 3, labels=[1,2,3])

    rfm['R_score'] = rfm['R_score'].astype(int)
    rfm['F_score'] = rfm['F_score'].astype(int)
    rfm['M_score'] = rfm['M_score'].astype(int)

    rfm['RFM_Score'] = rfm['R_score'] + rfm['F_score'] + rfm['M_score']

    def segment(score):
        if score >= 7:
            return "High Value"
        elif score >= 5:
            return "Medium Value"
        else:
            return "Low Value"

    rfm['Segment'] = rfm['RFM_Score'].apply(segment)

    return rfm