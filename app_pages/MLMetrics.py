import streamlit as st


def page_ml_prediction_metrics():
    """Page 5: ML Prediction Metrics"""
    st.header("ML Prediction Metrics")

    st.subheader("Label Distribution")
    ## st.plotly_chart('outputs/v1/labels_distribution_rows.png')

    st.subheader("Model Training History")
    st.write("**Accuracy Curves**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("outputs/v1/model_training_acc.png", 
            caption="Accuracy Curve Orignal Dataset")
    with col2:
        st.image("outputs/v1/small-data/small_model_training_acc.png", 
            caption="Accuracy Curve Small Dataset")
    with col3:
        st.image("outputs/v1/no_aug/model_training_acc.png", 
            caption="Accuracy Curve Without Image Augmentation")
    st.write("---")
    st.write("**Loss Curves**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("outputs/v1/model_training_losses.png", 
            caption="Loss Curve Orignal Dataset")
    with col2:
        st.image("outputs/v1/small-data/small_model_training_losses.png", 
            caption="Loss Curve Small Dataset")
    with col3:
        st.image("outputs/v1/no_aug/model_training_losses.png", 
            caption="Loss Curve Without Image Augmentation")
    st.write("---")
    st.write("**Confusin Matrices: True vs Predicted Species**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("outputs/v1/confusion_matrix.png",
            caption="Original Dataset")
    with col2:
        st.image("outputs/v1/small-data/confusion_matrix.png",
            caption="Small Dataset")
    with col3:
        st.image("outputs/v1/no_aug/confusion_matrix_no_aug.png",
            caption="Without Image Augmentation")
    st.write("---")
    st.header("Classification Reports")

    show_report("outputs/v1/reports/classification_report_full.txt", "Full Dataset")
    show_report("outputs/v1/reports/classification_report_small.txt", "Small Dataset")
    show_report("outputs/v1/reports/classification_report_no-aug.txt", "No Augmentation")

    st.subheader("Final Model Evaluation")
    st.markdown(
        """
        - Precision  
        - Recall  
        - F1-score   
        """
    )

def show_report(file_path, title):
    st.subheader(title)
    with open(file_path) as f:
        report_text = f.read()
    st.text_area("Report", report_text, height=300)
