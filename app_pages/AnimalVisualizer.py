import streamlit as st
import pandas as pd

from src.visualization import (
    plot_mean_variability_for_classes,
    plot_montage,
    compute_average_image
)


def page_animal_visualizer(df: pd.DataFrame):
    """ Page 2: Animal Visualizer"""
    st.header("Animal Visualizer")
    st.write("This page addresses **Business Requirement 1**.")
    labels = df['true_label'].unique().tolist()


    # Checkbox 1 – Average and variability images
    if st.checkbox("Display differences between average and variability images per species"):
        st.subheader("Average & Variability Images")
        selected_classes = st.multiselect("Select species:", labels, default=labels[:2])
        if selected_classes:
            fig = plot_mean_variability_for_classes(df, selected_classes)
            st.pyplot(fig)

    # Checkbox 2 – Compare average images across species
    if st.checkbox("Compare average images of different species"):
        st.subheader("Comparison of Average Images")
        selected_classes = st.multiselect("Select species for comparison:", labels, default=labels[:3])
        if selected_classes:
            import matplotlib.pyplot as plt
            fig, axes = plt.subplots(1, len(selected_classes), figsize=(5*len(selected_classes), 5))
            if len(selected_classes) == 1:
                axes = [axes]

            for ax, cls in zip(axes, selected_classes):
                avg_img = compute_average_image(df[df['true_label'] == cls]['filepath'])
                ax.imshow(avg_img, cmap="gray")
                ax.set_title(cls)
                ax.axis("off")

            st.pyplot(fig)

    # Checkbox 3 – Image montage
    if st.checkbox("Generate an image montage of sample animals per class"):
        st.subheader("Image Montage")
        selected_class = st.selectbox("Choose a class:", labels)
        if selected_class:
            fig = plot_montage(df, selected_class)
            st.pyplot(fig)
