import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd


def page_hypotheses_validation():
    """Page 4: Project Hypotheses and Validation"""
    st.header("Project Hypotheses and Validation")

    st.markdown("## Hypothesis 1")
    st.write(
        """
        The model can differentiate between animal species based on visual 
        features such as colour and shape.
        """
    )
    st.markdown("### **Validation**")
    st.markdown("#### Training History")
    col1, col2 = st.columns(2)
    with col1:
        st.image("outputs/v1/model_training_acc.png", caption="Accuracy Curve")
    with col2:
        st.image("outputs/v1/model_training_losses.png", caption="Loss Curve")
    st.image(
        "outputs/v1/confusion_matrix.png",
        caption="Confusion Matrix: True vs Predicted Species"
        )
    st.success("Supported: Model achieves high accuracy across species.")
    st.write("---")
    st.markdown("## Hypothesis 2")
    st.write(
        """
        Training the model on a smaller dataset reduces model performance and 
        accuracy.
        """
    )
    st.markdown("### **Validation**: Compare results on smaller vs. larger " \
    "subsets.")
    
    st.markdown("#### Training History")
    col1, col2 = st.columns(2)
    with col1:
        st.image("outputs/v1/small-data/small_model_training_acc.png", 
            caption="Accuracy Curve")
    with col2:
        st.image("outputs/v1/small-data/small_model_training_losses.png", 
            caption="Loss Curve")
    st.image("outputs/v1/small-data/confusion_matrix.png",
        caption="Confusion Matrix: True vs Predicted Species (small data)")
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
    st.write("---")
    st.markdown("## Hypothesis 3")
    st.write(
        """
        Training the model on non-augmented images will reduce model 
        performance and accuracy.
        """
    )
    st.markdown("- **Validation**: Train with/without augmentation and " \
    "compare performance.")

    st.markdown("#### Without Augmentation")
    col1, col2 = st.columns(2)
    with col1:
        st.image("outputs/v1/no_aug/model_training_acc.png", 
            caption="Accuracy Curve")
    with col2:
        st.image("outputs/v1/no_aug/model_training_losses.png", 
            caption="Loss Curve")
    st.image("outputs/v1/no_aug/confusion_matrix_no_aug.png",
        caption="Confusion Matrix: No Augmentation")

    augmentation_results = {
        "Setting": ["With Augmentation", "Without Augmentation"],
        "Accuracy": [0.98, 0.99],
        "Loss": [0.05, 0.02],
        "F1 score": [0.98, 0.99]
    }
    aug_results_df = pd.DataFrame(augmentation_results)
    st.dataframe(aug_results_df)

    st.bar_chart(aug_results_df.set_index("Setting")[["Accuracy"]])
    st.bar_chart(aug_results_df.set_index("Setting")[["Loss"]])

    st.error(
        "Not supported: The model trained without augmentation performed " \
        "slightly better than the augmented model. Non-augmentation did " \
        "improve accuracy or F1 score, indicating that in this case, " \
        "augmentation may not be required."
    )