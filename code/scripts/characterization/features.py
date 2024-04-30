# Functions for feature extraction.

import numpy as np
import pandas as pd
# import dtw library

def extract_features(data: np.array) -> np.array:
    """
    Main function for extracting features from the data
    """
    return np.array([1, 2, 3, 4, 5])




def euclidean_distance(data1: np.array, data2: np.array) -> float: # TODO: Implement this function using an already existing library for Euclidean distance
    """
    Compute the Euclidean distance between two signals
    """
    return np.linalg.norm(data1 - data2) #¿?

def dtw(data1: np.array, data2: np.array) -> float: # TODO: Implement this function using an already existing library for DTW
    """
    Compute the Dynamic Time Warping distance between two signals
    """
    return 0.0