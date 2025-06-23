# review_checker/reviewer_panel.py

import streamlit as st

st.set_page_config(page_title="Review Escalation Panel", layout="wide")
st.title("🧑‍⚖️ Human Review Panel for Escalated Cases")

# Sample Suspicious Case
case = {
    "buyer_id": "user_1024",
    "trust_score": 93,
    "model_confidence": 0.71,
    "flag_reason": "Return claim says 'wrong item' but image similarity = 91%",
    "review_text": "Received wrong product. Total scam.",
    "product_image": "sample_images/shoe_original.jpg",
    "return_image": "sample_images/shoe_returned.jpg"
}

st.markdown(f"""
### Case ID: {case["buyer_id"]}

- **Buyer Trust Score**: {case["trust_score"]} ⭐
- **Model Confidence (Fraud)**: {round(case["model_confidence"]*100)}%
- **Reason for Flag**: _{case["flag_reason"]}_
""")

# Layout: 2 Columns - Product vs Returned Image
col1, col2 = st.columns(2)
with col1:
    st.subheader("🛍️ Product Shipped")
    st.image(case["product_image"], caption="Original Product Image", use_column_width=True)

with col2:
    st.subheader("📦 Item Returned")
    st.image(case["return_image"], caption="Returned Item Image", use_column_width=True)

# Review
st.subheader("📝 Review Text")
st.info(case["review_text"])

# Action Buttons
st.subheader("👨‍⚖️ Take Action")
action = st.radio("Select a resolution:", ["✅ Approve Return", "❌ Reject as Fraud", "🔁 Request More Evidence"])

if st.button("Submit Decision"):
    st.success(f"Action recorded: {action}")
