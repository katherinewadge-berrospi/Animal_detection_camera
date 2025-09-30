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
    st.markdown("- **Validation**: Review training history and confusion matrix.")
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
    st.write(
        """
        **Accuracy:**
        - The images above show that the model's training accuracy improved
        steadily after the first few epochs.
        - The validation accuracy remained constantly higher than training 
        which shows the model is not overfitting.
        - This could be down to augmenting the images first or the dropout layers
        making it tougher to train but boosted validation performance.
        """
    )
    st.write(
        """
        **Loss:**
        - Both training and validation losses decreased over time, which
        shows that the model is optimizing well.
        - There is also a small gap between training and validation losses 
        which indicates the model is not overfitting.
        - The low validation loss also indicates strong performance.
        """
    )
    st.write(
        """
        **Confusion Matrix:**
        - The confusion matrix shows that the model is performing well across 
        all species, as the diagonal line is the most prominent feature.
        - Only a few off-diagonal values are seen but these are faint which 
        means that the model rarely misclassified species. This is also evidence 
        of high precision and recall.
        """
    )
    st.success("Supported: The model can distinguish between species with high " \
    " validation accuracy around 0.98 and low loss, indicating a strong " \
    " performance. The confusion matrix also shows the model rarely " \
    " misclassified species.")

    st.write("---")

    st.markdown("## Hypothesis 2")
    st.write(
        """
        Training the model on a smaller dataset reduces model performance and 
        accuracy.
        """
    )
    st.markdown("- **Validation**: Compare results on smaller vs. larger " \
    "subsets.")
    
    st.markdown("#### Training History")
    
    col1, col2 = st.columns(2)
    with col1:
        st.image("app_images/small-data/small_model_training_acc.jpg", 
            caption="Accuracy Curve Small Dataset")
    with col2:
        st.image("app_images/small-data/small_model_training_losses.jpg", 
            caption="Loss Curve Small Dataset")

    st.image("app_images/small-data/confusion_matrix.jpg",
        caption="Confusion Matrix: True vs Predicted Species (Small Dataset)")
    st.write(
        """
        **Accuracy:**
        - The accuracy curves show that the smaller dataset achieved high
        accuracy quickly, then improved steadily. 
        - The validation accuracy remained higher than the training accuracy and
        also remained steady after first few epochs.
        - The difference between training and validation accuracy is larger than
        the full dataset, which shows weaker generalisation.
        """
    )
    st.write(
        """
        **Loss:**
        - Training and validation losses decrease but become more steady which
        shows that the model is optimizing well.
        - The gap between training and validation loss is larger than the full
        dataset which indicates reduced stability.
        """
    )
    st.write(
        """
        **Confusion Matrix:**
        - The confusion matrix shows that the model is still performing well 
        across species, as the diagonal line is still a prominent feature.
        - However, more off-diagonal values are seen which means that the model
        misclassified species more often. 
        - This shows reduced precision and recall as certain species are being
        confused with one another.
        """
    )
    results = {
        "Dataset": ["Full Data", "Small Data"],
        "Accuracy": [0.98, 0.96],
        "Loss": [0.05, 0.14],
        "F1-score": [0.98, 0.96]
    }
    subset_results_df = pd.DataFrame(results)
    st.table(subset_results_df)
    st.bar_chart(subset_results_df.set_index("Dataset")[["Accuracy"]])
    st.bar_chart(subset_results_df.set_index("Dataset")[["Loss"]])
    st.success(
        "Support: The full dataset achieved **98%** accuracy and F1-score with"
        " a loss of **5%**. Whereas, the smaller dataset achieved **96%**"
        " accuracy and F1-score with a higher loss of **14%**."
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
        st.image("app_images/no_aug/model_training_acc.jpg", 
            caption="Accuracy Curve Without Image Augmentation")
    with col2:
        st.image("app_images/no_aug/model_training_losses.jpg", 
            caption="Loss Curve Without Image Augmentation")

    st.image("app_images/no_aug/confusion_matrix_no_aug.jpg",
        caption="Confusion Matrix: No Augmentation")

    augmentation_results = {
        "Setting": ["With Augmentation", "Without Augmentation"],
        "Accuracy": [0.98, 0.99],
        "Loss": [0.05, 0.03], 
        "F1-score": [0.98, 0.99]
    }
    aug_results_df = pd.DataFrame(augmentation_results)
    st.table(aug_results_df)
    st.bar_chart(aug_results_df.set_index("Setting")[["Accuracy"]])
    st.bar_chart(aug_results_df.set_index("Setting")[["Loss"]])

    st.error(
        "Rejected: The augmented model achieved **98%** accuracy and F1-score**"
        " with a loss of **5%**, while the non-augmented model achieved "
        "**99%** accuracy and F1-score with a lower loss of just **3%**. "
        "This contradicts the hypothesis, showing that augmentation did not "
        "improve performance and may not be required for this dataset."
    )