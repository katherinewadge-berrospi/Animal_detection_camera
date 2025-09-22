import streamlit as st
from multipage import MultiPage
from app_pages import ProjectSummary, AnimalVisualizer, AnimalDetection, HypothesesValidation, MLMetrics


# Create app instance
app = MultiPage("Animal Detection App")

# Register pages
app.app_page("Project Summary", ProjectSummary.page1_body)
app.app_page("Animal Visualizer", AnimalVisualizer.page2_body)
app.app_page("Animal Detection App", AnimalDetection.page3_body)
app.app_page("Project Hypotheses and Validation", HypothesesValidation.page4_body)
app.app_page("ML Metrics", MLMetrics.page5_body)

# Run the app
if __name__ == "__main__":
    app.run()
