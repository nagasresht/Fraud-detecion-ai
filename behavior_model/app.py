# behavior_model/app.py

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import IsolationForest

st.set_page_config(page_title="Behavior Model", layout="centered")

st.title("🧠 Behavioral Fraud Detector")

st.markdown("""
This module uses a simple **Isolation Forest** model to detect suspicious behavioral patterns 
in buyer or seller activities (like unusually high return rates or frequent account updates).
""")

# Simulate dummy user behavior data
def generate_user_data(n=200):
    np.random.seed(42)
    data = {
        "user_id": range(1, n + 1),
        "avg_return_rate": np.random.normal(0.1, 0.05, n),
        "account_modifications": np.random.poisson(2, n)
    }

    # Inject 10 anomalous users
    for i in range(10):
        data["avg_return_rate"][i] = np.random.uniform(0.3, 0.8)
        data["account_modifications"][i] = np.random.randint(10, 30)

    return pd.DataFrame(data)

df = generate_user_data()
st.write("### Sample of Behavior Data", df.head())

# Train Isolation Forest
model = IsolationForest(contamination=0.05)
df["anomaly_score"] = model.fit_predict(df[["avg_return_rate", "account_modifications"]])
df["is_anomaly"] = df["anomaly_score"].apply(lambda x: "❌ Suspicious" if x == -1 else "✅ Normal")

# Visualize
st.write("### Anomaly Detection Results")
fig, ax = plt.subplots()
colors = df["is_anomaly"].map({"✅ Normal": "green", "❌ Suspicious": "red"})
ax.scatter(df["avg_return_rate"], df["account_modifications"], c=colors)
ax.set_xlabel("Avg Return Rate")
ax.set_ylabel("Account Modifications")
ax.set_title("User Behavior Scatter Plot")
st.pyplot(fig)

# Show flagged users
st.write("### ⚠️ Flagged Suspicious Users")
st.dataframe(df[df["is_anomaly"] == "❌ Suspicious"])
