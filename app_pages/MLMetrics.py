import streamlit as st
import pandas as pd
import plotly.express as px


def page_ml_prediction_metrics():
    """Page 5: ML Prediction Metrics"""
    st.header("ML Prediction Metrics")

    st.markdown("## Label Distribution")
    label_counts = pd.read_csv("app_artifacts/label_distribution.csv")
    # Sort alphabetically
    label_counts = label_counts.sort_values("Label")
    fig = px.bar(
        label_counts,
        x="Frequency",
        y="Label",
        color="Set",
        title="Label Distribution",
        barmode="group",
        orientation="h"
    )
    fig.update_yaxes(
        categoryorder="array",
        categoryarray=sorted(label_counts["Label"].unique())
    )
    fig.update_layout(
        height=15 * label_counts["Label"].nunique(),
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("## Model Training History")
    st.markdown("### Accuracy Curves")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("app_images/model_training_acc.jpg", 
            caption="Accuracy Curve Original Dataset")
    with col2:
        st.image("app_images/small-data/small_model_training_acc.jpg", 
            caption="Accuracy Curve Small Dataset")
    with col3:
        st.image("app_images/no_aug/model_training_acc.jpg", 
            caption="Accuracy Curve Without Image Augmentation")
    st.write("---")
    st.markdown("### Loss Curves")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("app_images/model_training_losses.jpg", 
            caption="Loss Curve Original Dataset")
    with col2:
        st.image("app_images/small-data/small_model_training_losses.jpg", 
            caption="Loss Curve Small Dataset")
    with col3:
        st.image("app_images/no_aug/model_training_losses.jpg", 
            caption="Loss Curve Without Image Augmentation")
    st.write("---")
    st.markdown("### Confusion Matrices: True vs Predicted Species")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("app_images/confusion_matrix_full.jpg",
            caption="Original Dataset")
    with col2:
        st.image("app_images/small-data/confusion_matrix.jpg",
            caption="Small Dataset")
    with col3:
        st.image("app_images/no_aug/confusion_matrix_no_aug.jpg",
            caption="Without Image Augmentation")
    st.write("---")

    st.markdown("## Final Model Evaluation")
    st.markdown("### Classification Reports")

    option = st.selectbox(
        "Choose which report to view:",
        ["Full Dataset", "Small Dataset", "Without Augmentation"]
    )

    if option == "Full Dataset":
        df = load_report_df("app_images/report/classification_full.txt")
    elif option == "Small Dataset":
        df = load_report_df("app_images/report/classification_small.txt")
    else:
        df = load_report_df("app_images/report/classification_no_aug.txt")
    st.dataframe(df, use_container_width=True, hide_index=True)

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
