import json
import joblib
import pandas as pd


def load_model(model_path):
    """Load the trained fraud detection model."""
    return joblib.load(model_path)


def load_model_config(config_path):
    """Load the saved model configuration."""
    with open(config_path, "r") as file:
        return json.load(file)


def prepare_features(df, feature_names):
    """Prepare input data using the same features used during training."""
    missing_features = [feature for feature in feature_names if feature not in df.columns]

    if missing_features:
        raise ValueError(
            f"Missing required features: {missing_features}"
        )

    return df[feature_names]


def predict_transaction(model, df, feature_names):
    """Predict whether transactions are legitimate or fraudulent."""
    X = prepare_features(df, feature_names)

    predictions = model.predict(X)

    if hasattr(model, "predict_proba"):
        probabilities = model.predict_proba(X)[:, 1]
    else:
        probabilities = None

    results = pd.DataFrame({
        "Prediction": predictions,
        "Fraud_Probability": probabilities
    })

    results["Prediction_Label"] = results["Prediction"].map({
        0: "Legitimate",
        1: "Fraud"
    })

    return results