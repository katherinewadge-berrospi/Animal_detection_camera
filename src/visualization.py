import os
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


APP_IMG_DIR = "app_images"


def compute_average_image(species):
    """
    Compute the average image for a species from pre-saved app_images.
    Expects files saved like: app_images/<species>_*.jpg
    """
    files = [os.path.join(APP_IMG_DIR, f) for f in os.listdir(APP_IMG_DIR)
            if f.startswith(f"{species}_") and f.endswith(".jpg")]
    if not files:
        raise FileNotFoundError(f"No images found for species {species} in {APP_IMG_DIR}")

    imgs = [np.array(Image.open(fp).convert("L")) for fp in files]
    avg_img = np.mean(imgs, axis=0)
    return avg_img


def compute_variability_image(species):
    """
    Compute the std deviation image for a species from pre-saved app_images.
    """
    files = [os.path.join(APP_IMG_DIR, f) for f in os.listdir(APP_IMG_DIR)
            if f.startswith(f"{species}_") and f.endswith(".jpg")]
    imgs = [np.array(Image.open(fp).convert("L")) for fp in files]
    std_img = np.std(imgs, axis=0)
    return std_img


def plot_mean_variability_for_classes(classes):
    """
    Create a matplotlib plot showing avg & std images for given species.
    Works only with app_images/ folder.
    """
    fig, axes = plt.subplots(len(classes), 2, figsize=(8, 4*len(classes)))

    if len(classes) == 1:
        axes = [axes]

    for i, cls in enumerate(classes):
        avg_img = compute_average_image(cls)
        std_img = compute_variability_image(cls)

        axes[i][0].imshow(avg_img, cmap="gray")
        axes[i][0].set_title(f"{cls} - Average")
        axes[i][0].axis("off")

        axes[i][1].imshow(std_img, cmap="gray")
        axes[i][1].set_title(f"{cls} - Variability")
        axes[i][1].axis("off")

    plt.tight_layout()
    return fig


def plot_montage(species, n_images=9):
    """
    Plot a montage of pre-saved images for a species from app_images/.
    """
    files = [os.path.join(APP_IMG_DIR, f) for f in os.listdir(APP_IMG_DIR)
            if f.startswith(f"{species}_") and f.endswith(".jpg")]
    sample_files = files[:n_images]

    n_cols = 3
    n_rows = int(np.ceil(len(sample_files) / n_cols))
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(8, 8))
    axes = axes.flatten()

    for i, (ax, fp) in enumerate(zip(axes, sample_files)):
        img = Image.open(fp)
        ax.imshow(img)
        ax.set_title(species, fontsize=8)
        ax.axis("off")

    for j in range(i+1, len(axes)):
        axes[j].axis("off")

    plt.tight_layout()
    return fig
