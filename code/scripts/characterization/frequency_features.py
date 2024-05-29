import numpy as np
import librosa
from librosa.feature import spectral_centroid as sc
from librosa.feature import spectral_bandwidth as sb
from librosa.feature import mfcc

from processing.load_audio import load_audio_file


# BER function (Band Energy Ratio)
def compute_band_energy_ratio(y, sr, fmin, fmax):
    # Compute the Short-Time Fourier Transform (STFT)
    S = np.abs(librosa.stft(y))**2
    
    # Get the frequency values for each bin
    freqs = librosa.fft_frequencies(sr=sr)
    
    # Find the indices corresponding to the specified frequency band
    band_indices = np.where((freqs >= fmin) & (freqs <= fmax))[0]
    
    # Compute the energy in the specified frequency band
    band_energy = np.sum(S[band_indices, :], axis=0)
    
    # Compute the total energy
    total_energy = np.sum(S, axis=0)
    
    # Compute the Band Energy Ratio
    ber = band_energy / total_energy
    
    return ber, total_energy, band_energy

# Main function
def extract_frequency_features(audio_file_path: str): # TODO: Extract BER
    """
    Extract spectral centroid, spectral bandwidth, and MFCC features from an audio file

    :param audio_file_path: The path to the audio file
    :return: A dictionary containing the frequency features
    """

    # Load audio file
    audio_time_series, sampling_rate = load_audio_file(audio_file_path, 44100)

    # EXTRACT FEATURES
    # Spectral Centroid
    spectral_centroid = sc(y=audio_time_series, sr=sampling_rate)[0]
    # Spectral Bandwidth
    spectral_bandwidth = sb(y=audio_time_series, sr=sampling_rate)[0]
    # Mel-Frequency Cepstral Coefficients (MFCC)
    mfcc_features = mfcc(y=audio_time_series, sr=sampling_rate, n_mfcc=13)

    return spectral_centroid, spectral_bandwidth, mfcc_features
