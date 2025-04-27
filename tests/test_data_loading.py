# tests/test_data_loading.py

# To test there is at least one line of data

import pandas as pd

def test_data_loading():
    df = pd.read_csv('data/cleaned_data_week1_2.csv')
    assert df.shape[0] > 0