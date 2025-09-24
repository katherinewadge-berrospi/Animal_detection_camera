import pandas as pd
import os

def load_metadata_csv(csv_path: str) -> pd.DataFrame:
    """Load dataset metadata from CSV (must contain filepath + label)."""
    df = pd.read_csv(csv_path)
    if not {'filepath', 'label'}.issubset(df.columns):
        raise ValueError("CSV must contain 'filepath' and 'label' columns")
    return df
