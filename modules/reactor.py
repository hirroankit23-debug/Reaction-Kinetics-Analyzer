import math
import numpy as np
from scipy.optimize import fsolve


class ReactorCalculator:

    R = 8.314

    def __init__(self, k_ref, n):

        self.k_ref = k_ref
        self.n = n

    def arrhenius(self, Ea, T_ref, T):

        T_ref = T_ref + 273.15
        T = T + 273.15

        return self.k_ref * np.exp(
            (-Ea / self.R) * ((1 / T) - (1 / T_ref))
        )

    def reactor_volume(self, diameter, length):

        area = math.pi * diameter**2 / 4

        volume = area * length

        return volume * 1000

    def residence_time(self, volume_litre, flowrate):

        return volume_litre / flowrate

    def predict_conversion(self, CA0, tau, k):

        if k <= 0:
            return 0

        # First-order approximation
        if abs(self.n - 1) < 0.05:

            X = 1 - np.exp(-k * tau)

            return max(0, min(1, X))

        # General nth-order solution
        def equation(X):

            X = np.clip(X, 1e-6, 0.999)

            CA = CA0 * (1 - X)

            return tau - ((CA0 - CA) / (k * CA**self.n))

        X = fsolve(equation, 0.5)[0]

        return max(0, min(1, X))