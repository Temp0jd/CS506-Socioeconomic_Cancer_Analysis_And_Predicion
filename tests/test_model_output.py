# tests/test_model_output.py
# Test that there are no null values in the predicted results

import pandas as pd
import os

def test_model_predictions():
    filepath = os.path.join("notebooks", "linear_regression_predictions.csv")
    pred = pd.read_csv(filepath)
    assert pred['Predicted'].notnull().all(), "Predicted column should not have null values."