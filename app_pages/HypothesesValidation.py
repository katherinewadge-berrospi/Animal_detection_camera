import streamlit as st
import matplotlib.pyplot as plt


def page_hypotheses_validation():
    """Page 4: Project Hypotheses and Validation"""
    st.header("Project Hypotheses and Validation")

    st.subheader("Hypothesis 1")
    st.write(
        """
        **The model can differentiate between species based on visual patterns 
        (colour, shape, texture).**
        """
    )
    st.markdown("- **Validation**: Accuracy/loss curves, confusion matrix.")

    st.subheader("Hypothesis 2")
    st.write(
        """
        **Increasing dataset size and diversity improves accuracy.**
        """
    )
    st.markdown("- **Validation**: Compare results on smaller vs. larger subsets.")

    st.subheader("Hypothesis 3")
    st.write(
        """
        **Data augmentation improves model generalization.**
        """
    )
    st.markdown("- **Validation**: Train with/without augmentation and compare performance.")

    # TODO
    #st.info("⚠️ Validation outputs (plots, metrics) will be added later.")
