import pandas as pd

# Other functions
def to_seconds(t):
    return (t.hour * 60 * 60) + (t.minute * 60) + t.second + (t.microsecond / 1000000)

# Main function
def load_annotations_file(path: str) -> pd.DataFrame:
    """
    Load annotations from a file.

    :param path: Path to the file containing the annotations.
    :return: A pandas DataFrame containing the annotations.
    """
    # Read the annotations file
    annotations = pd.read_csv(path, sep="\t", header=None)

    # Add column names
    annotations.columns = ["level", "", "start", "end", "duration", "label"]
    del annotations[""]

    # Convert to seconds
    annotations["start"] = pd.to_datetime(annotations["start"])
    annotations["end"] = pd.to_datetime(annotations["end"])
    annotations["start"] = annotations["start"].apply(to_seconds)
    annotations["end"] = annotations["end"].apply(to_seconds)

    annotations.reset_index(inplace=True)

    return annotations

# Test main function
""" annotations_kj = load_annotations_file("data/raw/annotations_koti_janmani.txt")
print(annotations_kj.head()) """