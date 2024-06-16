# Raga Ritigowla Pattern Identification
Pattern identification task - Build a methodology that is able to identify repeated instances of melodic patterns. Students will characterize the difference in performance of these annotated melodic patterns and develop a process that can identify them from audio.

## Overview
This notebook `final_notebook_nns.ipynb` aims to, through the selection of the most significant features, train a model that can identify the nns pattern, one of the most common ones in Raga Ritigowla. This notebook trains diferent models and compares their performance against a random prediction. The models are a Gradient Boosting Classifier (GBC) and Random Forest Classifier (RFC). The notebook includes data preparation, model training, evaluation, and comparison steps.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setting Up the Environment](#setting-up-the-environment)
- [Notebook Structure](#notebook-structure)
- [Running the Notebook](#running-the-notebook)
- [Understanding the Output](#understanding-the-output)

## Prerequisites

Before running the notebook, ensure you have the following installed:

- Python 3.12.2 or later
- Jupyter Notebook or JupyterLab
- Required Python libraries:
  - `numpy`
  - `pandas`
  - `librosa`
  - `math`
  - `scipy`
  - `scikit-learn`
  - `matplotlib`
  - `IPython.display`

You can install the required libraries using `pip`:

```bash
pip install numpy pandas librosa scipy scikit-learn matplotlib IPython
```

## Setting Up the Environment
#### Clone or Download the Repository:
Clone the repository to your local machine or download it as a ZIP file and extract it.
```bash
git clone https://github.com/pdpau/Raga-Bhairavi-Pattern-Identification.git
```

#### Navigate to the Directory:
Change to the directory where the notebook is located.
```bash
cd code
```

#### Start Jupyter Notebook:
Launch Jupyter Notebook or JupyterLab in the directory.
```bash
jupyter notebook
```

#### Open the Notebook:
In the Jupyter interface, open `final_notebook_nns.ipynb` from the list of files.


## Notebook Structure
The notebook is structured as follows:

#### 1. Installs and imports:
In this first section, all the main libraries are installed and imported, some of them are going to be imported when needed in the corresponding cell. The notebook uses the following libraries:
- `numpy` for numerical operations
- `pandas` for data manipulation
- `librosa` for audio processing
- `math` for mathematical operations
- `scipy` for scientific computing
- `scikit-learn` for machine learning
- `matplotlib` for plotting graphs
- `IPython.display` for displaying audio files

#### 2. Loading Data and Characterization:
The data is loaded from the `data` directory, there are two audio files, Koti Janmani and Vanajaksha Ninni Kore, and their corresponding annotations in a text file. The features are extracted from the annotations, audio and pitch of each song. Once the features are extracted, one single dataframe with 17 features and 2 targets is created.

#### 3. Model Training, Prediction and Evaluation:
The data is split into training and testing sets. Firstly, a random classifier is used to set the baseline results if the prediction was done by chance. Then, the Gradient Boosting Classifier (GBC) and Random Forest Classifier (RFC) models are trained on the training data. Afterwards, the models are used to predict the test data. Predictions are evaluated using accuracy scores, confusion matrices and other classification reports.


## Running the Notebook
To execute the notebook, follow these steps:

#### 1. Run All Cells:
You can run all cells sequentially by selecting Cell > Run All from the Jupyter menu.

#### 2. Step-by-Step Execution:
Alternatively, you can execute the cells one by one. This allows you to understand the code and outputs at each stage.

#### 3. Check for Dependencies:
Ensure all libraries are installed. If you encounter errors, check if all dependencies are satisfied.

#### 4. Modify Parameters (Optional):
If you wish to experiment, modify the parameters or try with different datasets.


## Understanding the Output

#### Data Visualization:
Each dataframe generated after each feature extraction is avaliable to visualize, as well as plots of the pitch to see the patterns in the data.

#### Model Performance and Random Baseline:
Visual and statistical summaries, like metrics and confusion matrices to understand the performance of each model. Also, the random baseline is shown to compare the performance of the models.

#### Comparison Analysis:
Side-by-side comparison of the GBC and RFC against random predictions. The analysis should show that the GBC and RFC perform better than random chance, indicating it has learned meaningful patterns in the data.
