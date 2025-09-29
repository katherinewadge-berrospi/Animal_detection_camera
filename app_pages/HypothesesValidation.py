import streamlit as st
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
        st.image("app_images/model_training_acc.jpg", caption="Accuracy Curve")
    with col2:
        st.image("app_images/model_training_losses.jpg", caption="Loss Curve")
    st.image(
        "app_images/confusion_matrix_full.jpg",
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
        st.image("app_images/model_training_acc.jpg", 
            caption="Accuracy Curve Full Dataset")
    with col2:
        st.image("app_images/small-data/small_model_training_acc.jpg", 
            caption="Accuracy Curve Small Dataset")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("app_images/model_training_losses.jpg", 
            caption="Loss Curve Full Dataset")
    with col2:
        st.image("app_images/small-data/small_model_training_losses.jpg", 
            caption="Loss Curve Small Dataset")

    st.image("app_images/small-data/confusion_matrix.jpg",
        caption="Confusion Matrix: True vs Predicted Species (Small Dataset)")
    results = {
        "Dataset": ["Full Data", "Small Data"],
        "Accuracy": [0.98, 0.96],
        "Loss": [0.05, 0.13],
        "F1-score": [0.98, 0.96]
    }
    subset_results_df = pd.DataFrame(results)
    st.dataframe(subset_results_df)
    st.bar_chart(subset_results_df.set_index("Dataset")[["Accuracy"]])
    st.bar_chart(subset_results_df.set_index("Dataset")[["Loss"]])
    st.success(
        "Support: The full dataset achieved **98%** accuracy and F1-score with"
        " a loss of **5%**. Whereas, the smaller dataset achieved **96%**"
        " accuracy and F1-score with a higher loss of **13%**."
        "This confirms that the larger dataset delivered stronger performance, "
        "though the small dataset still performed well."
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
        st.image("app_images/model_training_acc.jpg", 
            caption="Accuracy Curve With Image Augmentation")
    with col2:
        st.image("app_images/no_aug/model_training_acc.jpg", 
            caption="Accuracy Curve Without Image Augmentation")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("app_images/model_training_losses.jpg", 
            caption="Loss Curve With Image Augmentation")
    with col2:
        st.image("app_images/no_aug/model_training_losses.jpg", 
            caption="Loss Curve Without Image Augmentation")

    st.image("app_images/no_aug/confusion_matrix_no_aug.jpg",
        caption="Confusion Matrix: No Augmentation")

    augmentation_results = {
        "Setting": ["With Augmentation", "Without Augmentation"],
        "Accuracy": [0.98, 0.99],
        "Loss": [0.05, 0.02],
        "F1-score": [0.98, 0.99]
    }
    aug_results_df = pd.DataFrame(augmentation_results)
    st.dataframe(aug_results_df)

    st.bar_chart(aug_results_df.set_index("Setting")[["Accuracy"]])
    st.bar_chart(aug_results_df.set_index("Setting")[["Loss"]])

    st.error(
        "Rejected: The augmented model achieved **98%** accuracy and F1-score**"
        " with a loss of **5%**, while the non-augmented model achieved "
        "**99%** accuracy and F1-score with a lower loss of just **2%**. "
        "This contradicts the hypothesis, showing that augmentation did not "
        "improve performance and may not be required for this dataset."
    )