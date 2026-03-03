import os
from dotenv import load_dotenv

from src.data_cleaning import load_data, clean_data
from src.rfm import create_rfm, segment_customers
from src.model import train_model, save_model

def main():
    load_dotenv()

    data_path = os.getenv("DATA_PATH")

    #Load and clean data
    df = load_data(data_path)
    df = clean_data(df)

    #Save cleaned data
    df.to_csv("data/processed/cleaned_online_retail.csv", index=False)

    #Get RFM values and segment customers
    rfm = create_rfm(df)
    rfm = segment_customers(rfm)

    # Train model and encoder and perform validation and evaluation
    model, encoder = train_model(rfm)
    save_model(model, encoder)

if __name__ == "__main__":
    main()