import numpy as np
import librosa
from IPython.display import Audio

# Main function
def load_audio_file(path: str, sampling_rate: int) -> tuple:
    """
    Load audio from a file

    :param path: The path to the audio file
    :param sampling_rate: The sampling rate to use
    :return: The audio time series and the sampling rate
    """
    # Load the audio file
    audio_time_series, sr = librosa.load(path, sr=sampling_rate)

    return audio_time_series, sr

# Test main function
""" audio_kj, sr_kj = load_audio_file("data/raw/Koti Janmani/Koti Janmani.mp3.mp3", 44100)
print(audio_kj) """

#Audio(data=audio_kj, rate=sr_kj)