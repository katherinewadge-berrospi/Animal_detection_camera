import streamlit as st
import pandas as pd

from app_pages.ProjectSummary import page_project_summary
from app_pages.AnimalVisualizer import page_animal_visualizer


df = pd.read_csv("inputs/datasets/animal_predictions.csv")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Project Summary", "Animal Visualizer"])

    if page == "Project Summary":
        page_project_summary()

    elif page == "Animal Visualizer":
        page_animal_visualizer(df)

if __name__ == "__main__":
    main()
