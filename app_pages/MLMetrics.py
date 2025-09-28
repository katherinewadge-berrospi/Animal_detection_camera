import streamlit as st
import pandas as pd


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

def load_report_df(file_path):
    rows = []
    with open(file_path) as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) == 5 and parts[0] != "accuracy":
                label, precision, recall, f1, support = parts
                rows.append([label, float(precision), float(recall), float(f1),
                            int(support)])
            elif line.startswith("accuracy"):
                parts = line.strip().split()
                rows.append(["accuracy", "", "", float(parts[1]), int(parts[-1])])
            elif line.startswith("macro avg") or line.startswith("weighted avg"):
                label = " ".join(parts[:-4])
                precision, recall, f1, support = parts[-4:]
                rows.append([label, float(precision), float(recall), float(f1),
                            int(support)])
    return pd.DataFrame(rows, columns=["Label", "Precision", "Recall",
                        "F1-score", "Support"])

def show_report(file_path, title):
    st.subheader(title)
    df = load_report_df(file_path)
    st.dataframe(df, use_container_width=True, hide_index=True)
