import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Animal Detection Camera",
    page_icon="🦉",
)

from app_pages.ProjectSummary import page_project_summary
from app_pages.AnimalVisualizer import page_animal_visualizer
from app_pages.AnimalDetection import page_animal_detection
from app_pages.HypothesesValidation import page_hypotheses_validation
from app_pages.MLMetrics import page_ml_prediction_metrics


df = pd.read_csv(
    "src/machine_learning/animal_predictions.csv")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", [
        "Project Summary",
        "Animal Visualizer",
        "Animal Detection",
        "Hypotheses and Validation",
        "ML Prediction Metrics"
        ])

    if page == "Project Summary":
        page_project_summary()

    elif page == "Animal Visualizer":
        page_animal_visualizer(df)
    
    elif page == "Animal Detection":
        page_animal_detection(df)
    
    elif page == "Hypotheses and Validation":
        page_hypotheses_validation()
    
    elif page == "ML Prediction Metrics":
        page_ml_prediction_metrics()


if __name__ == "__main__":
    main()
