import streamlit as st


def page1_body():
    """Page 1: Project Summary"""
    st.header("Project Summary")

    st.subheader("General Information")
    st.write(
        """
        The project focuses on automatic detection of animal species from images. 
        The aim is to support ecological research, wildlife monitoring, and conservation efforts 
        by classifying animals accurately using computer vision techniques.
        """
    )

    st.subheader("Project Dataset")
    st.write(
        """
        The dataset contains thousands of animal images across 64 species 
        (including, but not exclusive to, antelope, beaver, chimpanzee, and dolphin). 
        Images are split into training, validation, and test sets.
        """
    )
    st.markdown(
        "[Project README](../README.md)",
        unsafe_allow_html=True
    )

    st.subheader("Business Requirements")
    st.write(
        """
        - The client is interested in exploring visual differences between species 
        (e.g., variability and average features per class).  
        - The client is interested in an application that predicts which animal is 
        present in an uploaded image.
        """
    )
    
