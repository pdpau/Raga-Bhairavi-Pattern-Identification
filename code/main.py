from scripts.processing.data_processing import load_data, normalize
from scripts.characterization.features import extract_features    # Import all functions from the features.py file


# Dataset creation

# Load data
data = load_data(path)

# Pre-processing
norm_data = normalize(data)

# Feature extraction
y = extract_features(norm_data)

# Modelling

# ...
