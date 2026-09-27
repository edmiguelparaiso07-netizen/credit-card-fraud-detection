from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import json

app = Flask(__name__)

# Load trained model
MODEL_PATH = "models/final_fraud_detection_model.pkl"
CONFIG_PATH = "models/model_config.json"
DEMO_PATH = "demo_transactions.json"

model = joblib.load(MODEL_PATH)

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

with open(DEMO_PATH, "r") as file:
    demo_transactions = json.load(file)

FEATURES = config["features"]


@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":

        try:
            time_value = float(request.form["Time"])
            amount_value = float(request.form["Amount"])

            transaction = {
                "Time": time_value,
                "Amount": amount_value
            }

            for i in range(1, 29):
                transaction[f"V{i}"] = float(request.form[f"V{i}"])

            # Feature engineering
            transaction["Log_Amount"] = np.log1p(amount_value)
            transaction["Transaction_Hour"] = (time_value / 3600) % 24

            input_data = pd.DataFrame([transaction])

            # Correct feature order
            input_data = input_data[FEATURES]

            # Model prediction
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]

            if prediction == 1:

                result = {
                    "status": "POTENTIAL FRAUD",
                    "class": "fraud",
                    "probability": round(probability * 100, 2)
                }

            else:

                result = {
                    "status": "LEGITIMATE TRANSACTION",
                    "class": "legitimate",
                    "probability": round(probability * 100, 2)
                }

        except Exception as e:

            result = {
                "status": "ERROR",
                "class": "error",
                "probability": 0,
                "message": str(e)
            }

    return render_template(
        "index.html",
        result=result
    )


@app.route("/demo/<transaction_type>")
def demo(transaction_type):

    if transaction_type not in demo_transactions:
        return jsonify({
            "error": "Demo transaction not found"
        }), 404

    return jsonify(demo_transactions[transaction_type])


if __name__ == "__main__":
    app.run(debug=True)