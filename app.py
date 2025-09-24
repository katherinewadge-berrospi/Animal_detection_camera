import streamlit as st
import pandas as pd

from app_pages.ProjectSummary import page_project_summary
from app_pages.AnimalVisualizer import page_animal_visualizer
from app_pages.AnimalDetection import page_animal_detection
from app_pages.HypothesesValidation import page_hypotheses_validation


df = pd.read_csv("inputs/datasets/animal_predictions.csv")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", [
        "Project Summary",
        "Animal Visualizer",
        "Animal Detection",
        "Hypotheses and Validation"
        ])

    if page == "Project Summary":
        page_project_summary()

    elif page == "Animal Visualizer":
        page_animal_visualizer(df)
    
    elif page == "Animal Detection":
        page_animal_detection(df)
    
    elif page == "Hypotheses and Validation":
        page_hypotheses_validation()


if __name__ == "__main__":
    main()
