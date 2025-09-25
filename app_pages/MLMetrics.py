import streamlit as st


def page_ml_prediction_metrics():
    """Page 5: ML Prediction Metrics"""
    st.header("ML Prediction Metrics")

    st.subheader("Label Frequencies")
    st.write(
        """
        Display the frequencies of labels in the **Train**, **Validation**, 
        and **Test** datasets.
        """
    )

    st.subheader("Model Training History")
    st.write(
        """
        Show accuracy and loss curves over the training process 
        to illustrate how the model learned.
        """
    )

    st.subheader("Final Model Evaluation")
    st.markdown(
        """
        - Accuracy  
        - Precision  
        - Recall  
        - F1-score  
        - Confusion matrix  
        """
    )
