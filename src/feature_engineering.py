import pandas as pd
import numpy as np


def create_log_amount(df):
    """Create a log-transformed transaction amount feature."""
    df = df.copy()
    df["Log_Amount"] = np.log1p(df["Amount"])
    return df


def create_transaction_hour(df):
    """Create an approximate transaction-hour feature."""
    df = df.copy()
    df["Transaction_Hour"] = (df["Time"] / 3600) % 24
    return df


def engineer_features(df):
    """
    Apply all feature engineering steps.
    """
    df = create_log_amount(df)
    df = create_transaction_hour(df)

    return df