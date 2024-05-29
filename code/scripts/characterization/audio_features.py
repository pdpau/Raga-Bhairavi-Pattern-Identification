import librosa
#import librosa.display
from librosa.feature import rms
from librosa.feature import zero_crossing_rate as zcr

from processing.load_audio import load_audio_file


# Main function
def extract_audio_features(audio_file_path: str):
    """
    Extract rmse and zcr features from an audio file

    :param audio_file_path: The path to the audio file
    :return: A dictionary containing the audio features
    """

    # Load audio file
    audio_time_series, sampling_rate = load_audio_file(audio_file_path, 44100)

    # EXTRACT FEATURES
    # Root Mean Square Energy
    rms_energy = rms(y=audio_time_series)[0]
    # Zero Crossing Rate
    zcr_rate = zcr(y=audio_time_series)[0]

    return rms_energy, zcr_rate