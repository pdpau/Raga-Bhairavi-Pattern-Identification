# Scripts for data cleaning, smoothing, source separation, etc.

import numpy as np
import pandas as pd


def load_data(path: str) -> np.array:
    """
    TODO: Load data from a given path
    """
    return np.array([1, 2, 3, 4, 5])

def normalize(data: np.array) -> np.array:
    """
    Normalize data
    """
    return data / np.linalg.norm(data)