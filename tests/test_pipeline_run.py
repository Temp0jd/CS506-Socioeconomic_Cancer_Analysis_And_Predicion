# tests/test_pipeline_run.py

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pytest

def test_pipeline_runs_on_expected_structure():
    # Simulate a snippet of the data
    data = pd.DataFrame({
        "avgdeathsperyear": [469, 70, 50],
        "povertypercent": [11.2, 18.6, 14.6],
        "medincome": [61898, 48127, 49348],
        "popest2015": [260131, 43269, 21026],
    })

    # Validate that required columns are present
    required_columns = ["avgdeathsperyear", "povertypercent", "medincome", "popest2015"]
    for col in required_columns:
        assert col in data.columns, f"Missing expected column: {col}"

    # Prepare features and labels
    X = data[["povertypercent", "medincome", "popest2015"]]
    y = data["avgdeathsperyear"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

    # Fit model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predict
    y_pred = model.predict(X_test)

    # Validate output
    assert len(y_pred) == len(y_test), "Prediction output size mismatch"
    assert not pd.isnull(y_pred).any(), "Predicted values contain nulls"