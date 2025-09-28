import os
import streamlit as st
from PIL import Image

APP_IMG_DIR = "app_images"

def page_animal_visualizer(df=None):
    st.header("Animal Visualizer")
    st.write("This page addresses Business Requirement 1.")

    # Get species names from available jpg files
    available_species = []
    for f in os.listdir(APP_IMG_DIR):
        if f.endswith(".jpg") and f.startswith("avg_var_"):
            species = f.replace("avg_var_", "").replace(".jpg", "")
            available_species.append(species)

    if not available_species:
        st.error("No pre-computed images available in app_images.")
        return

    # First checkbox
    selected_species_1 = st.selectbox(
        "Select first species:", 
        available_species, 
        index=0
    )

    # Second checkbox
    selected_species_2 = st.selectbox(
        "Select second species:", 
        available_species, 
        index=1 if len(available_species) > 1 else 0
    )

    # Display chosen images
    col1, col2 = st.columns(2)
    with col1:
        img1 = Image.open(os.path.join(APP_IMG_DIR, f"avg_var_{selected_species_1}.jpg"))
        st.image(img1, caption=f"Average & Variability - {selected_species_1}")

    with col2:
        img2 = Image.open(os.path.join(APP_IMG_DIR, f"avg_var_{selected_species_2}.jpg"))
        st.image(img2, caption=f"Average & Variability - {selected_species_2}")

    # Checkbox 3 – Image montage
    if st.checkbox("Generate an image montage of sample animals per species"):
        st.subheader("Image Montage")

        # Find montage images in app_images
        montage_species = [
            f.replace("montage_", "").replace(".jpg", "")
            for f in os.listdir(APP_IMG_DIR)
            if f.startswith("montage_") and f.endswith(".jpg")
        ]

        if not montage_species:
            st.warning("No montage images available.")
        else:
            selected_class = st.selectbox("Choose a species:", montage_species)
            img_path = os.path.join(APP_IMG_DIR, f"montage_{selected_class}.jpg")
            st.image(img_path, caption=f"Image Montage – {selected_class}")
