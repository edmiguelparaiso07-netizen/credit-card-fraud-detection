import pandas as pd
import numpy as np


def load_data(file_path):
    """Load the credit card transaction dataset."""
    return pd.read_csv(file_path)


def remove_duplicates(df):
    """Remove duplicate transaction records."""
    return df.drop_duplicates().copy()


def add_features(df):
    """Create engineered features used by the model."""
    df = df.copy()

    # Reduce right-skew in transaction amount
    df["Log_Amount"] = np.log1p(df["Amount"])

    # Approximate transaction hour from elapsed time
    df["Transaction_Hour"] = (df["Time"] / 3600) % 24

    return df


def preprocess_data(file_path):
    """
    Complete preprocessing pipeline:
    1. Load data
    2. Remove duplicates
    3. Create engineered features
    """
    df = load_data(file_path)
    df = remove_duplicates(df)
    df = add_features(df)

    return df