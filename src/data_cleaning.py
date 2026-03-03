import pandas as pd

def load_data(path):
    return pd.read_csv(path)

def clean_data(df):
    # Remove cancelled invoices
    df = df[~df['InvoiceNo'].str.startswith('C')]

    # Remove negative values
    df = df[df['Quantity'] > 0]
    df = df[df['UnitPrice'] > 0]

    # Remove missing CustomerID
    df = df[df['CustomerID'].notnull()]

    # Convert types
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    df['CustomerID'] = df['CustomerID'].astype(int)

    # Create Revenue
    df['Revenue'] = df['Quantity'] * df['UnitPrice']
    
    return df