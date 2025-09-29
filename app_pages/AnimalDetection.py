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
    model = load_model("app_artifacts/final_model.keras")
    class_indices = joblib.load("outputs/v1/class_indices.pkl")
    target_map = {v: k for k, v in class_indices.items()}
    return model, target_map


def page_animal_detection(df=None):
    st.header("Animal Detection")
    st.info(
        """
        Upload an image of an animal, and the model will predict the most likely 
        species. You can upload multiple images, and results can be exported to 
        CSV.
        """
    )
    st.write("---")

    model, target_map = load_detector()

    uploaded_files = st.file_uploader(
        "Upload animal images (JPG/PNG)",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    if uploaded_files:
        results = []

        for uploaded_file in uploaded_files:
            image_stream = BytesIO(uploaded_file.read())
            image_stream.seek(0)

            with Image.open(image_stream) as img_pil:
                img_pil = img_pil.convert("RGB")
                img_resized = img_pil.resize((128, 128))

            st.image(
                img_resized,
                caption=f"Resized image: {uploaded_file.name} (128x128 pixels)",
                use_container_width=True,
            )

            img_array = np.array(img_resized) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Clear RAM
            del img_pil
            gc.collect()

            # Integrate Model Predictions
            predictions = model.predict(img_array)
            pred_idx = np.argmax(predictions)
            pred_species = target_map[pred_idx]
            confidence = predictions[0][pred_idx] * 100

            if confidence < 50:
                st.warning(
                    f"⚠️ Low confidence prediction ({confidence:.1f}%). "
                    "The result may be unreliable — try a clearer image."
                )

            results.append({
                "Image": uploaded_file.name,
                "Predicted Species": pred_species,
                "Confidence": f"{confidence:.1f}%"
            })
            top_3 = np.argsort(predictions[0])[-3:][::-1]
            top_results = [
                {"Species": target_map[i], 
                "Confidence": f"{predictions[0][i]*100:.1f}%"}
                for i in top_3
            ]
            st.write("Top 3 predictions for this image:")
            st.table(pd.DataFrame(top_results))

        # Results table
        df_predictions = pd.DataFrame(results)
        st.success(
            "Analysis Report: Predictions completed — see results below ✅")
        st.table(df_predictions)

        # Download CSV
        st.markdown(df_as_csv(df_predictions), unsafe_allow_html=True)


def df_as_csv(df):
    """Allow users to download predictions as CSV."""
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv(index=False).encode()
    b64 = base64.b64encode(csv).decode()
    return (
        f'<a href="data:file/csv;base64,{b64}" '
        f'download="AnimalPredictions_{datetime_now}.csv" '
        f'target="_blank">📥 Download Predictions as CSV</a>'
    )