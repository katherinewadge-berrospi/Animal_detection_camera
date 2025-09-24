import pandas as pd
import os

def load_metadata_csv(csv_path: str) -> pd.DataFrame:
    """Load dataset metadata from CSV (must contain filepath + label)."""
    df = pd.read_csv(csv_path)
    if not {'filepath', 'label'}.issubset(df.columns):
        raise ValueError("CSV must contain 'filepath' and 'label' columns")
    return df

def build_metadata_from_folders(root_dir: str) -> pd.DataFrame:
    """
    Build dataframe with 'filepath' and 'label' columns
    directly from image folders structured as: root/class_name/image.png
    """
    records = []
    for label in os.listdir(root_dir):
        class_dir = os.path.join(root_dir, label)
        if os.path.isdir(class_dir):
            for file in os.listdir(class_dir):
                if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                    records.append({
                        "filepath": os.path.join(class_dir, file),
                        "label": label
                    })
    return pd.DataFrame(records)
