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
