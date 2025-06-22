# review_checker/app.py

import streamlit as st
from transformers import pipeline

# Load LLM pipeline
classifier = pipeline("sentiment-analysis")

def check_review(text):
    result = classifier(text)[0]
    label = result['label']
    score = result['score']

    if label == "NEGATIVE" and score > 0.9:
        return "⚠️ Likely FAKE or Manipulated Review", score
    elif label == "POSITIVE" and score < 0.6:
        return "⚠️ Possibly Overly Polished – Needs Review", score
    else:
        return "✅ Review seems Legit", score

# Streamlit UI
st.title("🕵️ Review Authenticity Checker")
st.markdown("Paste a review below to check if it's genuine or suspicious.")

user_input = st.text_area("✍️ Enter review text:", height=150)

if st.button("🔍 Check Review"):
    if user_input.strip() == "":
        st.warning("Please enter a review to analyze.")
    else:
        verdict, confidence = check_review(user_input)
        st.subheader(verdict)
        st.write(f"**Model confidence**: {confidence:.2f}")
