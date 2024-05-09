import pandas as pd
import numpy as np

# Main function
def load_pitch_file(path: str) -> tuple:
    """
    Load a pitch file from a given path.

    :param path: Path to the pitch file.
    :return: pd.DataFrame pitch_file
                np.array time
                np.array pitch
                float timestep
    """
    pitch_file = pd.read_csv(path, sep="\t", header=None)
    pitch_file.columns = ["time", "pitch"]

    time = pitch_file["time"].values
    pitch = pitch_file["pitch"].values
    timestep = time[1] - time[0]

    return pitch_file, time, pitch, timestep

# Test main function
""" pitch_df_kj, time_kj, pitch_kj, timestep_kj = load_pitch_file("data/raw/Koti Janmani/Koti Janmani.pitch.txt")
print(pitch_df_kj) """