# main.py

import streamlit as st
import os

st.set_page_config(page_title="AI Fraud Detection", layout="wide")

st.title("🛡️ AI-Powered Trust & Safety Platform")

st.markdown("""
Welcome to the **Fraud Detection Dashboard** for buyers & sellers on marketplaces.

Use the sidebar to explore different modules that help:
- Detect fake reviews
- Compare return images
- Spot unusual behaviors
- Catch fraud rings
- Investigate using AI
""")

# Sidebar navigation
page = st.sidebar.selectbox(
    "🔍 Choose Module",
    [
        "📋 Review Checker",
        "🖼️ Image Matcher",
        "🧠 Behavior Anomaly Detector",
        "🕸️ Graph Fraud Detector",
        "🤖 Chat Investigator",
        "🧾 OCR Tag Validator"
    ]
)

# Launch selected module
if page == "📋 Review Checker":
    os.system("streamlit run review_checker/app.py")

elif page == "🖼️ Image Matcher":
    os.system("streamlit run image_matcher/app.py")

elif page == "🧠 Behavior Anomaly Detector":
    os.system("streamlit run behavior_model/app.py")

elif page == "🕸️ Graph Fraud Detector":
    os.system("streamlit run graph_fraud/app.py")

elif page == "🤖 Chat Investigator":
    os.system("streamlit run chat_investigator/app.py")
elif page == "🧾 OCR Tag Validator":
    os.system("streamlit run tag_validator/app.py")
    
