import streamlit as st
import pandas as pd
import joblib

# --- Load the new trained model and scaler ---
model = joblib.load("models/xgb_model_1_2.pkl")   # XGBoost model with ROI ≥ 1.2
scaler = joblib.load("models/scaler_1_2.pkl")         # Scaler used during training

# --- App Title ---
st.title("💡 Keyword ROI Classifier (ROI ≥ 1.2)")
st.write("Predict whether to **Keep Paying** or **Cut Paid** based on Paid Cost, Revenue, and Period.")

# --- Sidebar Inputs ---
st.sidebar.header("📥 Enter Keyword Metrics")
cost = st.sidebar.number_input("Paid Cost ($)", min_value=0.0, value=100.0)
revenue = st.sidebar.number_input("Revenue ($)", min_value=0.0, value=200.0)
period = st.sidebar.number_input("Period (1–19)", min_value=1, max_value=30, value=14)

# --- Predict Button ---
if st.sidebar.button("🚀 Predict"):
    input_df = pd.DataFrame([[cost, revenue, period]], columns=['Paid_Cost', 'revenue', 'period'])
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    
    if prediction == 1:
        st.success("✅ Recommendation: **Keep Paying** (ROI expected to be profitable)")
    else:
        st.error("❌ Recommendation: **Cut Paid** (ROI likely below 1.2 threshold)")

# --- CSV Upload for Bulk Prediction ---
st.markdown("### 📂 Upload CSV for Bulk Prediction")
uploaded_file = st.file_uploader("Upload a CSV file with: Paid_Cost, revenue, period", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    try:
        X = scaler.transform(df[['Paid_Cost', 'revenue', 'period']])
        df['Prediction'] = model.predict(X)
        df['Prediction Label'] = df['Prediction'].map({1: "✅ Keep Paying", 0: "❌ Cut Paid"})
        st.write(df)
        st.download_button("📥 Download Results", df.to_csv(index=False), "predictions.csv")
    except Exception as e:
        st.error(f"❌ Error processing the file: {e}")
