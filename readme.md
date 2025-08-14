
# 📊 Keyword Marketing Optimization Platform

**Course:** CSP 572 – Data Science Practicum (Spring 2025)  
**Client:** LabelMaster  
**Advisor:** Dr. Yong Zheng  

**Contributors:**  
- Ram Prakash Bollam  
- Bharath Suresh Sanu  
- Nihal Korukanti  
- Ayesha Saif  

---

## 🚀 Overview
This project is a data-driven keyword marketing optimization system designed to help businesses improve ROI and strategic keyword targeting across organic and paid search channels.

---

## 🎯 Main Objectives

**1. ROI Prediction**
- Predict whether a keyword investment will be profitable based on historical performance metrics.
- Supports two ROI labeling strategies:
	- **Conservative:** ROI ≥ 1.5
	- **Inclusive:** ROI ≥ 1.2
- **Final model:** XGBoost Classifier (97.1% accuracy, 0.96 F1-score)

**2. Business Classification**
- Classify keywords into six strategic business categories based on their strength in organic and paid channels:
	- all_keywords_with_labels
	- strong_in_both
	- strong_in_organic_not_paid
	- strong_in_paid_not_organic
	- weak_moderate
	- weak_near_thresholds
	- weak_very_low
- **Final model:** Random Forest Classifier

Both objectives are integrated into a Streamlit application for non-technical marketing teams.

---

## 📂 Project Structure

```text
STREAMLIT/
│
├── app/
│   ├── __init__.py
│   └── app.py
│
├── data/
│   ├── business_labels/
│   ├── expected output/
│   ├── expected_output/
│   └── test_sets/
│
├── docs/
│   ├── LM IIT Project PPT.pdf
│   └── Project Technical Documentation.pdf
│
├── images/
│
├── models/
│   └── roi_prediction/
│       ├── scaler_1_2.pkl
│       └── xgb_model_1_2.pkl
│
├── notebooks/
│   ├── business_labels.ipynb
│   └── ROI>=1.2.ipynb
│
├── venv/
│
├── .gitignore
├── README.md
├── README_STRUCTURE.md
├── requirements.txt
```

> 📎 For a deeper breakdown of folders and file roles, see `README_STRUCTURE.md`

---

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

| File Name                                 | Purpose                                      |
|-------------------------------------------|----------------------------------------------|
| app/app.py                                | Main Streamlit application file               |
| models/roi_prediction/xgb_model_1_2.pkl   | Trained XGBoost model for prediction         |
| models/roi_prediction/scaler_1_2.pkl      | Trained StandardScaler used during training  |
| data/test_sets/test_keywords.csv           | Example input file for bulk testing          |
| requirements.txt                          | List of Python packages for setup            |

---

## 🖥️ How to Use the App

**ROI Prediction Tab**
- Upload a CSV with keyword metrics or enter data manually.
- Select ROI threshold (1.2 or 1.5).
- Download predictions.

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

| Issue                    | Solution                                         |
|--------------------------|-------------------------------------------------|
| ModuleNotFoundError      | Run `pip install -r requirements.txt`            |
| App not launching        | Ensure you're running in the virtual environment |
| Model not found          | Confirm xgb_model.pkl and scaler.pkl exist       |
| App restarts continuously| Avoid modifying code while app is running        |

---

## 📜 License
This project is for academic and demonstration purposes only.  
All sensitive datasets are excluded to comply with confidentiality agreements.

