# chat_investigator/app.py

import streamlit as st
from openai import OpenAI

# ✅ Configure Groq client (OpenAI-compatible)
client = OpenAI(
    api_key="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",
    base_url="https://api.groq.com/openai/v1"
)

# UI Setup
st.title("🕵️‍♂️ Groq-Powered AI Fraud Investigator")
st.markdown("Ask questions about review/return fraud, suspicious buyers, or anomalies.")

# Example context
sample_context = """
Review: "Loved the product! Will buy again!"
Verdict: Possibly fake - very generic and overly positive
Image Match Score: 0.57 — Return item is different
User Behavior: Multiple return requests within 5 days, different delivery addresses
"""

# Inputs
context = st.text_area("📄 Case Context", value=sample_context, height=180)
query = st.text_input("💬 Ask your question about this case:")

# On submission
if st.button("🔍 Investigate"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("🚀 Groq LLaMA 3 is analyzing..."):
            try:
                response = client.chat.completions.create(
                    model="llama3-70b-8192",
                    messages=[
                        {"role": "system", "content": "You are an expert fraud investigator assistant."},
                        {"role": "user", "content": f"CASE:\n{context}\n\nQUESTION:\n{query}"}
                    ]
                )
                st.success(response.choices[0].message.content)
            except Exception as e:
                st.error(f"Groq API Error: {e}")
