import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def page_hypotheses_validation():
    """Page 4: Project Hypotheses and Validation"""
    st.header("Project Hypotheses and Validation")

    st.markdown("## Hypothesis 1")
    st.write(
        """
        **The model can differentiate between species based on visual patterns 
        (colour, shape, texture).**
        """
    )
    st.markdown("### **Validation**")
    st.markdown("#### Training History")
    st.image("outputs/v1/model_training_acc.png", caption="Accuracy Curve")
    st.image("outputs/v1/model_training_losses.png", caption="Loss Curve")
    st.image(
        "outputs/v1/confusion_matrix.png",
        caption="Confusion Matrix: True vs Predicted Species"
        )
    st.success("Supported: Model achieves high accuracy across species.")

    st.markdown("## Hypothesis 2")
    st.write(
        """
        **Increasing dataset size and diversity improves accuracy.**
        """
    )
    st.markdown("### **Validation**: Compare results on smaller vs. larger subsets.")
    
    st.markdown("#### Training History")
    st.image("outputs/v1/small-data/small_model_training_acc.png", caption="Accuracy Curve")
    st.image("outputs/v1/small-data/small_model_training_losses.png", caption="Loss Curve")
    st.image(
        "outputs/v1/small-data/confusion_matrix.png",
        caption="Confusion Matrix: True vs Predicted Species (small data)"
        )

    results = {
    "Dataset": ["Full Data", "Small Data"],
    "Accuracy": [0.98, 0.96],
    "Loss": [0.05, 0.13],
    "F1 score": [0.98, 0.96]
    }
    subset_results_df = pd.DataFrame(results)

    st.dataframe(subset_results_df)

    st.bar_chart(subset_results_df.set_index("Dataset")[["Accuracy"]])
    st.bar_chart(subset_results_df.set_index("Dataset")[["Loss"]])

    st.info(
        "Partial support: Larger dataset improved accuracy by..."
        "This confirms(?) the hypothesis that more data improves performance."
    )

    st.markdown("## Hypothesis 3")
    st.write(
        """
        **Data augmentation improves model generalization.**
        """
    )
    st.markdown("- **Validation**: Train with/without augmentation and compare performance.")

    st.markdown("#### Without Augmentation")
    st.image("outputs/v1/no_aug/model_training_acc.png", caption="Accuracy Curve (No Augmentation)")
    st.image("outputs/v1/no_aug/model_training_losses.png", caption="Loss Curve (No Augmentation)")
    st.image(
        "outputs/v1/no_aug/confusion_matrix_no_aug.png",
        caption="Confusion Matrix: No Augmentation"
    )