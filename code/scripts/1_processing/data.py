import numpy as np


def load_data(path: str) -> np.array:
    """
    Load data from a given path
    """
    return np.array([1, 2, 3, 4, 5])

def normalize(data: np.array) -> np.array:
    """
    Normalize data
    """
    return data / np.linalg.norm(data)