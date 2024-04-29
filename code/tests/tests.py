def test_load_data():
    path = "example_path"
    y = load_data(path)
    assert isinstance(y, np.array)


# testing packages
# pytest
# unittest
