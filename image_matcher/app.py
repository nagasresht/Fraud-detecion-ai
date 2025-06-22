# image_matcher/app.py

import streamlit as st
from PIL import Image
import torch
from torchvision import transforms
from transformers import CLIPProcessor, CLIPModel

# Load model & processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Title
st.title("🖼️ Return vs Product Image Validator")
st.markdown("Upload two images: one from the **product listing**, and one from the **returned item**.")

# File upload
uploaded_file1 = st.file_uploader("Upload Product Image", type=["jpg", "jpeg", "png"], key="img1")
uploaded_file2 = st.file_uploader("Upload Return Image", type=["jpg", "jpeg", "png"], key="img2")

# When both images are uploaded
if uploaded_file1 and uploaded_file2:
    image1 = Image.open(uploaded_file1).convert("RGB")
    image2 = Image.open(uploaded_file2).convert("RGB")

    st.image([image1, image2], caption=["Product Image", "Return Image"], width=300)

    if st.button("🔍 Compare Images"):
        # Preprocess
        inputs = processor(images=[image1, image2], return_tensors="pt", padding=True)

        # Get embeddings
        with torch.no_grad():
            embeddings = model.get_image_features(**inputs)

        # Normalize & calculate cosine similarity
        image1_feat = embeddings[0] / embeddings[0].norm()
        image2_feat = embeddings[1] / embeddings[1].norm()
        similarity = torch.cosine_similarity(image1_feat, image2_feat, dim=0).item()

        # Display result
        st.subheader("🔎 Similarity Score: {:.2f}".format(similarity))
        if similarity > 0.90:
            st.success("✅ Images Match – Likely Same Product")
        elif similarity > 0.75:
            st.warning("⚠️ Partial Match – Possibly Altered or Used")
        else:
            st.error("❌ Mismatch Detected – Return Likely Invalid")
