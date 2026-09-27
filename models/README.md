\# Model Documentation



\## Final Model



The final fraud detection model is a tuned Random Forest classifier trained to classify credit card transactions as legitimate or fraudulent.



\## Model Configuration



\- Model: Tuned Random Forest

\- Number of trees: 200

\- Maximum depth: 30

\- Minimum samples split: 2

\- Minimum samples leaf: 4

\- Maximum features: `log2`

\- Class weight: `balanced\_subsample`

\- Random state: 42



\## Training Configuration



\- Training records: 226,980

\- Testing records: 56,746

\- Number of input features: 32

\- Target variable: `Class`



\## Input Features



The model uses:



\- `Time`

\- `V1`–`V28`

\- `Amount`

\- `Log\_Amount`

\- `Transaction\_Hour`



\## Model Selection



The Random Forest model was selected after comparing multiple classification algorithms, including:



\- Logistic Regression

\- Decision Tree

\- Random Forest

\- Gradient Boosting

\- XGBoost



Hyperparameter tuning was performed using RandomizedSearchCV with F1-score as the optimization metric.



\## Test Performance



The tuned Random Forest achieved:



\- Accuracy: 99.95%

\- Precision: 93.33%

\- Recall: 73.68%

\- F1-score: 82.35%

\- ROC-AUC: 94.17%



\## Model File



The trained model is stored as:



`final\_fraud\_detection\_model.pkl`



The corresponding configuration is stored in:



`model\_config.json`



\## Important Note



The model is intended as a fraud-screening and decision-support component. Production deployment should include threshold optimization, monitoring for model drift, human review procedures, and periodic model validation.

