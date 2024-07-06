import streamlit as st
import torch
from transformers import DPTFeatureExtractor, DPTForDepthEstimation
from PIL import Image
import numpy as np

# Titles and descriptions
st.title("Image Depth Estimation")
st.write("Upload an image and apply the depth estimation technique using the DPT model.")

# Load the MiDaS model and feature extractor
@st.cache_resource
def load_model():
    feature_extractor = DPTFeatureExtractor.from_pretrained("Intel/dpt-large")
    model = DPTForDepthEstimation.from_pretrained("Intel/dpt-large")
    return feature_extractor, model

feature_extractor, model = load_model()

# Upload user image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    MAX_SIZE = (600, 400)
    image.thumbnail(MAX_SIZE)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Processing...")

    # Prepare the image for the model
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        outputs = model(**inputs)
        predicted_depth = outputs.predicted_depth

    # Interpolate to the original image size
    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=image.size[::-1],
        mode="bicubic",
        align_corners=False,
    )

    # Visualize the depth estimation
    output = prediction.squeeze().cpu().numpy()
    formatted = (output * 255 / np.max(output)).astype("uint8")
    depth = Image.fromarray(formatted)
    st.image(depth, caption='Estimated Depth', use_column_width=True)
