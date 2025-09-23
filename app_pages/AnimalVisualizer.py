import streamlit as st
import pandas as pd

from src.visualization import (
    plot_mean_variability_for_classes,
    plot_montage,
    compute_average_image
)


def page2_body():
    """ Page 2: Animal Visualizer"""
    st.header("Animal Visualizer")
    st.write("This page addresses **Business Requirement 1**.")

    # Checkbox 1 – Average and variability images
    if st.checkbox("Display differences between average and variability images per species"):
        st.subheader("Average & Variability Images")
        st.info("📌 This section will show average and standard deviation images for selected species.")
        # TODO: Insert code here to compute and display avg/std images
        # st.write("⚠️ Functionality not yet implemented")

    # Checkbox 2 – Compare average images across species
    if st.checkbox("Compare average images of different species"):
        st.subheader("Comparison of Average Images")
        st.info("📌 This section will compare average images between different animal classes.")
        # TODO: Insert code here to compare averages
        # st.write("⚠️ Functionality not yet implemented")

    # Checkbox 3 – Image montage
    if st.checkbox("Generate an image montage of sample animals per class"):
        st.subheader("Image Montage")
        st.info("📌 This section will display a montage/grid of sample images per class.")
        # TODO: Insert montage display function here
        #st.write("⚠️ Functionality not yet implemented")
