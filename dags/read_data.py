import pandas as pd
import logging
def read_data():
    # This data need transformation columns to normalize note capitalize >> transformation_data.py
    try:
        data = pd.read_csv("dags/data/F1_2022_data.csv")
        return data
    except Exception as e:
        logging.error(f"Could not retrive data {e}")

