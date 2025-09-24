import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from tensorflow.keras.models import load_model
import joblib
import base64
from datetime import datetime
from io import BytesIO
import gc


# Cache model + class mapping so they load once
@st.cache_resource
def load_detector():
    model = load_model("outputs/v1/final_model.keras")
    class_indices = joblib.load("outputs/v1/class_indices.pkl")
    target_map = {v: k for k, v in class_indices.items()}
    return model, target_map


def page_animal_detection(df=None):
    st.header("Animal Detection App")
    st.info(
        """
        Upload an image of an animal, and the model will predict the most likely species.  
        You can upload multiple images, and results can be exported to CSV.
        """
    )

    uploaded_files = st.file_uploader(
        "Upload one or more animal images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"{len(uploaded_files)} file(s) uploaded successfully.")
        for uploaded_file in uploaded_files:
            st.image(uploaded_file, caption=uploaded_file.name, use_column_width=True)

    st.subheader("Planned Features")
    st.markdown(
        """
        - File uploader widget for one or multiple images  
        - Display of the uploaded image(s)  
        - Prediction of the species  
        - Probability (confidence score) for each prediction  
        - Results table with image names and predictions  
        - Download button to export predictions as a CSV  
        """
    )

    # TODO
    # st.info("⚠️ Functionality will be implemented later.")
