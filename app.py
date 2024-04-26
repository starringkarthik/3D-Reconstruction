import streamlit as st
import shutil
import os

colab_directory = "/content/3D-Reconstruction/pifuhd/sample_images"

if not os.path.exists(colab_directory):
    os.makedirs(colab_directory)

st.title("3D Reconstruction")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    image_path = os.path.join(colab_directory, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success(f"Image saved to {image_path}")
