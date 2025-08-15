
## Keyword Marketing Optimization Platform

**Course:** CSP 572 – Data Science Practicum (Spring 2025)  
**Client:** Confidential B2B Logistics Company  
**Advisor:** Dr. Yong Zheng  

**Contributors:**  
- Ram Prakash Bollam  
- Bharath Suresh Sanu  
- Nihal Korukanti  
- Ayesha Saif  

---

### Overview
This project is a data-driven keyword marketing optimization system designed to help businesses improve ROI and strategic keyword targeting across organic and paid search channels.

#### Main Objectives

**1. ROI Prediction**
- Predict whether a keyword investment will be profitable based on historical performance metrics.
- Supports two ROI labeling strategies:
	- **Conservative:** ROI ≥ 1.5
	- **Inclusive:** ROI ≥ 1.2
- **Final model:** XGBoost Classifier (97.1% accuracy, 0.96 F1-score).

**2. Business Classification**
- Classify keywords into six strategic business categories based on their strength in organic and paid channels.
- Categories include:
    - all keywords with labels
	- strong_in_both
	- strong_in_organic_not_paid
	- strong_in_paid_not_organic
	- weak_moderate
    - weak_near_thresholds
    - weak_very_low

- **Final model:** Random Forest Classifier.

The ROI objective is integrated into a Streamlit application for non-technical marketing teams.

---

### Data Sources (Simulated)
- Google data 
- Bing data
- Organic traffic scores
- Sales transactions
- Session-level engagement data

*All datasets used in this repository are synthetic and do not reflect any proprietary or confidential information.*

---

### Key Features

**Feature Engineering:**
- Log transformation of skewed features
- Min-Max normalization
- Composite scores for Organic and Paid performance
- KMeans clustering for tier segmentation

**Modeling:**
- ROI Prediction: Logistic Regression, Random Forest, Gradient Boosting, XGBoost
- Business Classification: Random Forest
- Reinforcement Learning: Deep Q-Network (DQN) for dynamic budget reallocation

**Deployment:**
- Streamlit Web App
- Upload CSV or enter keywords manually
- Download predictions directly

---

### 📁 Project Structure

```text
STREAMLIT
│
├── app
│   ├── __init__.py
│   └── app.py
│
├── data
│   ├── business_labels
│   │   ├── synthetic_all_keywords_with_labels.csv
│   │   ├── synthetic_keywords_Strong_in_both_cut_reduce_paid.csv
│   │   ├── synthetic_keywords_Strong_in_organic,_not_paid_in.csv
│   │   ├── synthetic_keywords_Strong_in_paid,_not_organic_in.csv
│   │   ├── synthetic_keywords_Weak_moderate_-_deprioritize_b.csv
│   │   ├── synthetic_keywords_Weak_near_thresholds_-_small_o.csv
│   │   ├── synthetic_keywords_Weak_very_low_-_drop_or_archiv.csv
│   ├── expected output
│   │   ├── sample_synthetic_predictions_1.csv
│   │   └── sample_synthetic_predictions_2.csv
│   ├── test_sets
│   │   ├── synthetic_keywords_test_set_1.csv
│   │   ├── synthetic_keywords_test_set_1.csv
│   │   ├── synthetic_keywords_test_set_1.csv  
│
├── images
|   ├── Bulk Predction.png
│   ├── downloaded_predictions.png
│   ├── Keyword_prediction_based_on_cost_rev_period.png
│   ├── Streamlit app default page.png
| 
│
├── models
│   └── roi_prediction
│       ├── first_scaler.pkl
│       ├── first_xgb_model.pkl
│       ├── scaler_1_2.pkl
│       └── xgb_model_1_2.pkl
│
├── notebooks
│   ├── notebooks/final.py
│   └── notebooks/roi_2.py
│
├── venv
│
├── .gitignore
├── README_STRUCTURE.md
├── readme.md
└── requirements.txt
```

## ⚙️ Installation & Setup

**1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/keyword-marketing-optimization.git
cd keyword-marketing-optimization
```

**2. Create a Virtual Environment**
```bash
python -m venv venv
```

**3. Activate the Environment**
- **Windows:**
	```bash
	venv\Scripts\activate
	```
- **macOS/Linux:**
	```bash
	source venv/bin/activate
	```

**4. Install Dependencies**
```bash
pip install -r requirements.txt
```

**5. Run the Streamlit App**
```bash
streamlit run app/app.py
```

The app will launch in your default browser at: [http://localhost:8501](http://localhost:8501)

---

## 🧪 Required Files to Run the App

| File Name                    | Purpose                                     |
|------------------------------|---------------------------------------------|
| app.py                       | Main Streamlit application file             |
| xgb_model_1_2.pkl            | Trained XGBoost model for prediction        |
| scaler_1_2.pkl               | Trained StandardScaler used during training |
| test_keywords.csv            | Example input file for bulk testing         |
| requirements.txt             | List of Python packages for setup           |

---

## 🖥️ How to Use the App

**ROI Prediction Tab**
- Upload a CSV with keyword metrics or enter data manually.
- View predictions and download results.

---

## 📈 Expected Outcomes
- Identify keywords with high profitability potential.
- Prioritize marketing investments accordingly.
- Empower business teams to make data-driven decisions without technical intervention.

---

## 🔮 Future Work
- Extend to campaign-level optimization.
- Improve RL agent for multi-channel budget allocation.

---

## 🛠️ Troubleshooting

| Issue                    | Solution                                        |
|--------------------------|------------------------------------------------ |
| ModuleNotFoundError      | Run `pip install -r requirements.txt`           |
| App not launching        | Ensure you're running in the virtual environment|
| Model not found          | Confirm xgb_model.pkl and scaler.pkl exist      |
| App restarts continuously| Avoid modifying code while app is running       |

---

## 📜 License
This project is for academic and demonstration purposes only.  
All sensitive datasets are excluded to comply with confidentiality agreements.

## 🛡️ Disclaimer
This repository is for academic and demonstration purposes only. All data, labels, and visuals have been anonymized or synthetically generated to comply with confidentiality agreements. No proprietary information from the client is included.

