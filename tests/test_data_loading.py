# tests/test_data_loading.py
# Test that the linear regression prediction file has data

import pandas as pd
import os

def test_data_loading():
    filepath = os.path.join("data", "linear_regression_predictions.csv")
    df = pd.read_csv(filepath)
    assert df.shape[0] > 0, "The data file should contain at least one row."