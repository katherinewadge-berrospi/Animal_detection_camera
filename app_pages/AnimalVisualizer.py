import os
import streamlit as st
from PIL import Image

APP_IMG_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "app_images"))

def page_animal_visualizer(df=None):
    st.header("Animal Visualizer")
    st.write("This page addresses Business Requirement 1.")

    # Map species -> filename for avg/var images
    available_species = {
        f.replace("avg_var_", "").replace(".jpg", ""): f
        for f in os.listdir(APP_IMG_DIR)
        if f.startswith("avg_var_") and f.endswith(".jpg")
    }

    if not available_species:
        st.error("No pre-computed images available in app_images.")
        return

    species_list = list(available_species.keys())

    # First selection
    selected_species_1 = st.selectbox(
        "Select first species:",
        species_list,
        index=0
    )

    # Second selection
    selected_species_2 = st.selectbox(
        "Select second species:",
        species_list,
        index=1 if len(species_list) > 1 else 0
    )

    # Display chosen images
    col1, col2 = st.columns(2)
    with col1:
        img1_path = os.path.join(APP_IMG_DIR, available_species[selected_species_1])
        st.image(img1_path, caption=f"Average & Variability – {selected_species_1}")

    with col2:
        img2_path = os.path.join(APP_IMG_DIR, available_species[selected_species_2])
        st.image(img2_path, caption=f"Average & Variability – {selected_species_2}")

    # Checkbox 3 – Image montage
    if st.checkbox("Generate an image montage of sample animals per species"):
        st.subheader("Image Montage")

        montage_species = {
            f.replace("montage_", "").replace(".jpg", ""): f
            for f in os.listdir(APP_IMG_DIR)
            if f.startswith("montage_") and f.endswith(".jpg")
        }

        if not montage_species:
            st.warning("No montage images available.")
        else:
            montage_list = list(montage_species.keys())
            selected_class = st.selectbox("Choose a species:", montage_list)
            img_path = os.path.join(APP_IMG_DIR, montage_species[selected_class])
            st.image(img_path, caption=f"Image Montage – {selected_class}")
