import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from load_annotations import load_annotations_file
from load_pitch import load_pitch_file
from load_audio import load_audio_file

# Main function
def get_observation_koti_janmani(i):
    annotations_df = load_annotations_file("data/raw/annotations_koti_janmani.txt")
    pitch_df, time, pitch, cents, timestep = load_pitch_file("data/raw/Koti Janmani/Koti Janmani.pitch.txt")
    audio_time_series, sr = load_audio_file("data/raw/Koti Janmani/Koti Janmani.mp3.mp3", 44100)

    row = annotations_df.loc[i]
    label = row.label
    
    start = round(row.start / timestep)
    end = round(row.end / timestep)
    """ start_sr = round(row.start * sampling_rate)
    end_sr = round(row.end * sampling_rate) """
    
    pitch_sample = pitch[start:end]
    time_sample = time[start:end]
    """ audio_sample = audio_file[start_sr:end_sr] """
    
    return pitch_sample, time_sample, label


# Test main function
pitch_sample, time_sample, label = get_observation_koti_janmani(0)

# Plot time series and pitch (TODO: Display in a frontend)
""" plt.plot(time_sample, pitch_sample)
plt.title(f'{label}')
plt.ylabel('Pitch (Hz)')
plt.xlabel('Time (s)')
plt.show() """



# Main function but general, not only for koti janmani
""" annotations_df = load_annotations_file("data/raw/annotations_koti_janmani.txt")
pitch_df, time, pitch, timestep = load_pitch_file("data/raw/Koti Janmani/Koti Janmani.pitch.txt")
audio_time_series, sr = load_audio_file("data/raw/Koti Janmani/Koti Janmani.mp3.mp3", 44100) """

def get_observation(i, pitch, time, annotations_df, timestep):
    row = annotations_df.loc[i]
    label = row.label
    
    start = round(row.start / timestep)
    end = round(row.end / timestep)
    """ start_sr = round(row.start * sampling_rate)
    end_sr = round(row.end * sampling_rate) """
    
    pitch_sample = pitch[start:end]
    time_sample = time[start:end]
    """ audio_sample = audio_file[start_sr:end_sr] """
    
    return pitch_sample, time_sample, label