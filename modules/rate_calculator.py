import numpy as np


class RateCalculator:

    def __init__(self, rc1_data):

        self.data = rc1_data.copy()

    def calculate(self):

        time = self.data["Time(min)"].values

        conversion = self.data["Conversion"].values

        rate = np.gradient(conversion, time)

        self.data["dX/dt"] = rate

        CA = self.data["CA (mol/L)"].values

        self.data["Rate (mol/L/min)"] = rate * CA

        return self.data