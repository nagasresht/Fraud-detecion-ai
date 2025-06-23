import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
import streamlit as st
from ocr_engine import extract_text_from_image


st.set_page_config(page_title="OCR Tag Validator", page_icon="🔍")

st.title("🔍 Product Tag Validator (OCR + AI)")

st.markdown("""
Upload an image of the product tag (e.g., shirt label) to validate its content. 
This helps check for fake tags, mismatches, or swapped items.
""")

uploaded_file = st.file_uploader("Upload Tag Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with open("temp_uploaded_tag.jpg", "wb") as f:
        f.write(uploaded_file.read())

    st.image("temp_uploaded_tag.jpg", caption="Uploaded Tag", use_column_width=True)
    
    with st.spinner("Extracting text using OCR..."):
        extracted_text = extract_text_from_image("temp_uploaded_tag.jpg")
    
    st.success("🧾 Text Extracted from Tag:")
    st.code(extracted_text)

    # (Optional) Add validation keyword or brand check
    if "Nike" in extracted_text or "Adidas" in extracted_text:
        st.info("✅ Known brand detected in the tag.")
    else:
        st.warning("⚠️ Brand not confidently detected — check for authenticity.")
