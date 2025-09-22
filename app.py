import streamlit as st
from multipage import MultiPage
from app_pages import ProjectSummary
from app_pages import AnimalVisualizer

# Create app instance
app = MultiPage("Animal Detection App")

# Register pages
app.app_page("Project Summary", ProjectSummary.page1_body)
app.app_page("Animal Visualizer", AnimalVisualizer.page2_body)

# Run the app
if __name__ == "__main__":
    app.run()
