import os
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import random


def compute_average_image(filepaths):
    """
    Compute the average image for a list of filepaths.
    Returns numpy array.
    """
    imgs = [np.array(Image.open(fp).convert("L")) for fp in filepaths]
    return np.mean(imgs, axis=0)

def compute_variability_image(filepaths):
    """
    Compute the standard deviation image for a list of filepaths.
    """
    imgs = [np.array(Image.open(fp).convert("L")) for fp in filepaths]
    return np.std(imgs, axis=0)

def plot_mean_variability_for_classes(df, classes, n_samples=20):
    """
    Create a matplotlib plot.
    Shows avg & std images for given classes.
    """
    fig, axes = plt.subplots(len(classes), 2, figsize=(8, 4*len(classes)))
    if len(classes) == 1:
        axes = [axes]

    for i, cls in enumerate(classes):
        subset = df[df['true_label'] == cls]
        class_files = subset['filepath'].sample(min(n_samples, len(subset)))

        avg_img = compute_average_image(class_files)
        std_img = compute_variability_image(class_files)

        axes[i][0].imshow(avg_img, cmap="gray")
        axes[i][0].set_title(f"{cls} - Average")
        axes[i][0].axis("off")

        axes[i][1].imshow(std_img, cmap="gray")
        axes[i][1].set_title(f"{cls} - Variability")
        axes[i][1].axis("off")

    plt.tight_layout()
    return fig

def plot_montage(df, cls, n_images=9):
    """
    Plot a montage of random sample images for a class.
    """
    subset = df[df['true_label'] == cls]
    sample_files = subset['filepath'].sample(min(n_images, len(subset)))
    
    n_cols = 3
    n_rows = int(np.ceil(len(sample_files) / n_cols))

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(8, 8))
    axes = axes.flatten()

    for i, (ax, fp) in enumerate(zip(axes, sample_files)):
        img = Image.open(fp)
        ax.imshow(img)
        ax.set_title(cls, fontsize=8)
        ax.axis("off")

    for j in range(i+1, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    return fig

def get_available_visualizations(img_dir="app_images"):
    """
    Return a dict of species -> filepaths for saved average/variability images.
    Looks for files named avg_var_<species>.png
    """
    files = [f for f in os.listdir(img_dir) if f.startswith("avg_var_") and f.endswith(".jpg")]
    species = {f.replace("avg_var_", "").replace(".jpg", ""): os.path.join(img_dir, f) for f in files}
    return species

def load_visualization_for_species(species, img_dir="app_images"):
    """
    Load pre-saved avg/var visualization for a species.
    Returns filepath if exists, else None.
    """
    path = os.path.join(img_dir, f"avg_var_{species}.jpg")
    if os.path.exists(path):
        return path
    return None
