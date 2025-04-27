# tests/test_model_output.py

# To test there is no null in predicted result

import pandas as pd

def test_model_predictions():
    pred = pd.read_csv('outputs/linear_regression_predictions.csv')
    assert pred['Predicted'].notnull().all()
