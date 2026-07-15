import numpy as np


class Arrhenius:

    R = 8.314

    def __init__(self):
        self.temperature = []
        self.k = []

    def add_experiment(self, temperature_C, rate_constant):

        self.temperature.append(
            temperature_C + 273.15
        )

        self.k.append(rate_constant)

    def calculate(self):

        T = np.array(self.temperature)

        k = np.array(self.k)

        x = 1 / T

        y = np.log(k)

        slope, intercept = np.polyfit(x, y, 1)

        Ea = -slope * self.R

        A = np.exp(intercept)

        return Ea, A