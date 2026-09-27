\# Dataset Documentation



\## Dataset



This project uses a credit card transaction dataset for supervised machine learning-based fraud detection.



The raw dataset is intentionally not included in this public repository. Users should obtain the dataset from the original source and place it locally as:



`creditcard.csv`



\## Dataset Overview



\- Original records: 284,807

\- Original features: 30

\- Target variable: `Class`

\- Legitimate transactions (`Class = 0`): 284,315

\- Fraudulent transactions (`Class = 1`): 492

\- Missing values: 0

\- Duplicate rows identified: 1,081



\## Variables



| Variable | Type | Description |

|---|---|---|

| `Time` | Numerical | Seconds elapsed between each transaction and the first transaction |

| `V1`–`V28` | Numerical | Anonymized PCA-transformed transaction features |

| `Amount` | Numerical | Transaction amount |

| `Class` | Binary | Target variable: 0 = legitimate, 1 = fraudulent |



\## Data Preparation



During preprocessing:



\- Duplicate transaction records were removed.

\- Missing values were checked.

\- Statistical outliers were analyzed and retained because unusual transaction behavior may contain fraud-related information.

\- The dataset was split using stratified sampling to preserve the minority fraud class.

\- Additional engineered features included `Log\_Amount` and `Transaction\_Hour`.



\## Data Privacy



The raw transaction dataset is not committed to this public GitHub repository. The `.gitignore` file prevents `creditcard.csv` from being uploaded accidentally.



\## Reproducibility



To reproduce the analysis, obtain the dataset from its original source and place `creditcard.csv` in the project's root directory before running the analysis notebooks or scripts.

