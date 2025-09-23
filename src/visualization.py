import numpy as np
import matplotlib.pyplot as plt
import random
from PIL import Image


def compute_average_image(filepaths):
    """
    Compute the average image for a list of filepaths.
    Returns numpy array.
    """
    imgs = [np.array(Image.open(fp).convert("L")) for fp in filepaths]
    avg_img = np.mean(imgs, axis=0)

    return avg_img

def compute_variability_image(filepaths):
    """
    Compute the standard deviation image for a list of filepaths.
    """
    imgs = [np.array(Image.open(fp).convert("L")) for fp in filepaths]
    std_img = np.std(imgs, axis=0)

    return std_img

def plot_mean_variability_for_classes(df, classes, n_samples=20):
    """
    Create a matplotlib plot.
    Shows avg & std images for given classes.
    """
    fig, axes = plt.subplots(len(classes), 2, figsize=(8, 4*len(classes)))

    if len(classes) == 1:
        axes = [axes]  # ensure iterable

    for i, cls in enumerate(classes):
        class_files = df[df['label'] == cls]['filepath'].sample(min(n_samples, len(df)))
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
