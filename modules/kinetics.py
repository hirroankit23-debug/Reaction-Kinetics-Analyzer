import numpy as np
from scipy.optimize import curve_fit


class Kinetics:

    def __init__(self, rc1_data):

        self.data = rc1_data.copy()

    def model(self, CA, k, n):

        return k * (CA ** n)

    def estimate(self):

        df = self.data.copy()

        df = df[
            (df["CA (mol/L)"] > 0) &
            (df["Rate (mol/L/min)"] > 0)
        ]

        CA = df["CA (mol/L)"].values
        Rate = df["Rate (mol/L/min)"].values

        popt, _ = curve_fit(
            self.model,
            CA,
            Rate,
            p0=[1.0, 1.0],
            bounds=(0, np.inf)
        )

        k = popt[0]
        n = popt[1]

        Predicted = self.model(CA, k, n)

        Residual = Rate - Predicted

        rmse = np.sqrt(np.mean(Residual**2))

        r2 = 1 - np.sum(
            Residual**2
        ) / np.sum(
            (Rate - np.mean(Rate))**2
        )

        df["Predicted Rate"] = Predicted
        df["Residual"] = Residual

        return {
            "Reaction Order": n,
            "Rate Constant": k,
            "R2": r2,
            "RMSE": rmse,
            "Data": df
        }