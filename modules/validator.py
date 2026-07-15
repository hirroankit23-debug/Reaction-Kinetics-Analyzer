import pandas as pd


class DataValidator:

    def __init__(self, experiment, rc1_data):
        self.experiment = experiment
        self.rc1_data = rc1_data

    def validate(self):

        errors = []

        required_columns = [
            "Time(min)",
            "Reactor_Temperature(C)",
            "Jacket_Temperature(C)",
            "HeatFlow(W)",
            "Pressure(bar)"
        ]

        # Check required columns first
        for col in required_columns:
            if col not in self.rc1_data.columns:
                errors.append(f"Missing column: {col}")

        # If columns are missing, stop here
        if errors:
            return errors

        # Missing values
        if self.rc1_data.isnull().values.any():
            errors.append("RC1e data contains missing values.")

        # Duplicate time values
        if self.rc1_data["Time(min)"].duplicated().any():
            errors.append("Duplicate time values detected.")

        # Time increasing
        if not self.rc1_data["Time(min)"].is_monotonic_increasing:
            errors.append("Time column is not in increasing order.")

        # Numeric columns
        numeric_cols = [
            "Time(min)",
            "Reactor_Temperature(C)",
            "Jacket_Temperature(C)",
            "HeatFlow(W)",
            "Pressure(bar)"
        ]

        for col in numeric_cols:
            if not pd.api.types.is_numeric_dtype(self.rc1_data[col]):
                errors.append(f"{col} must contain numeric values.")

        return errors