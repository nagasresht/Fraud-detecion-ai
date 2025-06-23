# review_checker/app.py

import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

st.set_page_config(page_title="Review Checker", layout="centered")
st.title("📋 Review Authenticity Checker")

review = st.text_area("Paste a Product Review:")

if st.button("Analyze"):
    if not review.strip():
        st.warning("Please enter a review.")
    else:
        result = sentiment_pipeline(review)[0]
        label = result["label"]
        score = result["score"]

        # 🌡️ Confidence threshold
        if score < 0.85:
            st.warning("⚠️ Confidence is low. Redirecting to human review panel.")
            st.markdown("🔗 [Open Reviewer Panel](reviewer_panel.py)")
        else:
            if label == "POSITIVE":
                st.success(f"✅ Review seems Legit (Confidence: {score:.2f})")
            else:
                st.error(f"⚠️ Likely FAKE or Manipulated Review (Confidence: {score:.2f})")
