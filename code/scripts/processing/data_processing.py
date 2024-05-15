# Scripts for data cleaning, interpolation, smoothing, source separation, etc.

import numpy as np
import pandas as pd

# Main function




# Other functions

def zscore_normalization(data: pd.DataFrame, features) -> pd.DataFrame: # Z-score for normalization to all features
    """
    Normalize data using Z-score normalization.
    """
    for feat in features:
        data[feat] = (data[feat] - data[feat].mean()) / data[feat].std()
    return data


# Apuntes
# Trim start and end of the signal
# Interpolate silences of less than 350 ms
# If we have to compare two samples of slightly different lengths, we can resample them to the same length (or DTW)
# ...

