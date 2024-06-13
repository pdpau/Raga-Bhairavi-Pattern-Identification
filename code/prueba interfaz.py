import ipywidgets as widgets
from IPython.display import display, clear_output
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import io
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

# Function to analyze the audio file
def analyze_audio(file_content):
    y, sr = librosa.load(io.BytesIO(file_content))
    duration = librosa.get_duration(y=y, sr=sr)
    return y, sr, round(duration,2)

# Function to handle the file upload event
def handle_file_upload(change):
    file_content = change['new'][0]['content']
    with output:
        clear_output(wait=True)
        loading_label.value = "Loading, please wait..."
        y, sr, duration = analyze_audio(file_content)
        
        fig = plt.figure(figsize=(15, 5))
        gs = fig.add_gridspec(1, 2)
        
        # Plot the audio signal
        ax1 = fig.add_subplot(gs[0, 0])
        librosa.display.waveshow(y, sr=sr, ax=ax1)
        ax1.set(title='Waveform', xlabel='Time (s)', ylabel='Amplitude')
        
        # Plot the spectrogram
        ax2 = fig.add_subplot(gs[0, 1])
        D = librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max)
        img = librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax2)
        fig.colorbar(img, ax=ax2, format='%+2.0f dB')
        ax2.set(title='Spectrogram', xlabel='Time (s)', ylabel='Frequency (Hz)')
        
        plt.show()
        print(f'Audio duration: {duration} seconds')
        
        # Run final_notebook.py and display its output
        run_and_display_notebook('C:/Users/alexf/Downloads/Raga-Bhairavi-Pattern-Identification/code/final_notebook_test.ipynb')
        
        loading_label.value = ""

# Function to run and display another notebook
notebook_path = "C:/Users/alexf/Downloads/Raga-Bhairavi-Pattern-Identification/code/final_notebook_test.ipynb"
def run_and_display_notebook(notebook_path):
    with open(notebook_path) as f:
        nb = nbformat.read(f, as_version=4)
        
    ep = ExecutePreprocessor(timeout=600, kernel_name='python3')
    ep.preprocess(nb, {'metadata': {'path': './'}})
    
    # Display the notebook's output
    for cell in nb.cells:
        if cell.cell_type == 'code':
            for output in cell.outputs:
                if output.output_type == 'stream':
                    print(output.text)
                elif output.output_type == 'display_data':
                    display(output.data)

# File upload widget
file_upload = widgets.FileUpload(accept='.wav, .mp3', multiple=False)
file_upload.observe(handle_file_upload, names='value')

# Output widget to display the result
output = widgets.Output()

# Create image widget
image_path = 'C:/Users/alexf/Downloads/pattern.png'  # Replace with the path to your image
file = open(image_path, "rb")
image = file.read()

img_widget = widgets.Image(
    value=image,
    format='png',
    width=300,
    height=300,
)

# Style the button and output area
file_upload.style.button_color = 'lightblue'
output.layout.backgroundColor = 'lightyellow'

# Label widget to display the loading message
loading_label = widgets.Label(value='')

# Title widget
title = widgets.HTML(
    value="<h2 style='font-weight:bold; font-size:18px;'>Carnatic Music: Pattern Identification</h2>"
)

# Display the interface in a separate window
window = widgets.VBox([
    title,
    widgets.Label('Upload an audio file you want to analyze (.wav or .mp3):'),
    file_upload,
    img_widget,
    loading_label,
    output
])
display(window)


