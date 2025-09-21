import streamlit as st
from transformers import pipeline
from PIL import Image

model = pipeline("image-classification")

st.title("AI Image Analyzer")
uploaded_file = st.file_uploader("Upload an image", type=["jpg","png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image)
    results = model(image)
    st.write(results)
