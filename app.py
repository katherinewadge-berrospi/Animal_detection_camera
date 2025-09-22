import streamlit as st
from multipage import MultiPage
from app_pages import ProjectSummary

# Create app instance
app = MultiPage("Animal Detection App")

# Register pages
app.app_page("Quick Project Summary", ProjectSummary.page1_body)

# Run the app
if __name__ == "__main__":
    app.run()
