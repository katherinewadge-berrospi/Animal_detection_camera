import streamlit as st


def page_project_summary():
    """Page 1: Project Summary"""
    st.header("Project Summary")

    st.subheader("General Information")
    st.write(
        """
        The project focuses on automatic detection of animal species from 
        images for our client, Steve B. The aim is to support ecological 
        research, wildlife monitoring, and conservation efforts by classifying 
        animals accurately using machine learning techniques.
        """
    )

    st.subheader("Project Dataset")
    st.write(
        """
        The dataset contains 14.7k images of animals across 64 species,
        sourced from Kaggle (including, but not exclusive to, antelope, beaver, 
        chimpanzee, and dolphin). 
        Images were pre-processed, augmented, and split into training, 
        validation, and test sets.
        """
    )
    st.markdown(
        "[Project README]"
        "(https://github.com/katherinewadge-berrospi/Animal_detection_camera/blob/main/README.md)",
        unsafe_allow_html=True
    )

    st.subheader("Business Requirements")
    st.write(
        """
        1. Can the system highlight visual differences between species (e.g., 
        average features, variability)?  
        2. Can the system predict which animal species is present in an uploaded 
        image with high accuracy?
        """
    )
    
    st.subheader("Hypotheses")
    st.write(
        """
        - **Hypothesis 1**: The model can differentiate between animal species
        based on visual features such as colour and shape.
        - **Hypothesis 2**: Training the model on a smaller dataset reduces 
        model performance and accuracy.
        - **Hypothesis 3**: Training the model on images without augmentation 
        will reduce model performance and accuracy.
        """
    )

    st.write("---")
    st.warning("**Disclaimer:** The dataset used in this project includes "
            "AI-generated images of animals. Results should therefore be "
            "interpreted as a demonstration of predictive modelling, not as a "
            "production-ready wildlife identification system."
    )