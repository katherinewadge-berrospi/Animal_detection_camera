import streamlit as st


def page3_body():
    """Page 3: Animal Detection App"""
    st.header("Animal Detection App")
    st.write("This page addresses **Business Requirement 2**.")

    st.subheader("Overview")
    st.write(
        """
        This section provides an interface for detecting animals in uploaded images.
        Users will be able to upload one or multiple animal images, and the app will
        process them using the trained classification model.
        """
    )

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
