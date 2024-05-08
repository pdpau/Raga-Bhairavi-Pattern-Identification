# Scripts for data cleaning, smoothing, source separation, etc.

import numpy as np
import pandas as pd

def process(data: np.array) -> pd.DataFrame : # TODO: Implement this function
    """
    Main data_processing function. Apply necessary processing functions to the data
    """
    return data # ¿¿dataframe or array??


def load_data(path: str) -> np.array: # TODO: Implement this function
    """
    Load data from a given path
    """
    return np.array([1, 2, 3, 4, 5])

def normalize(data: np.array) -> np.array: # Z-score for normalization to all features
    """
    Normalize data
    """
    return data / np.linalg.norm(data)


# Apuntes
# Trim start and end of the signal
# Interpolate silences of less than 350 ms
# If we have to compare two samples of slightly different lengths, we can resample them to the same length (or DTW)
# ...

def trim_signal_start_end(data: np.array) -> np.array: # TODO: Implement this function
    """
    Trim start and end of the signal
    """
    return data[100:-100]

def interpolate_silences(data: np.array) -> np.array: # TODO: Implement this function
    """
    Interpolate silences of less than 350 ms
    """
    return data

def resample(data: np.array, new_length: int) -> np.array: # TODO: Implement this function
    """
    Resample data to a new length
    """
    return data

