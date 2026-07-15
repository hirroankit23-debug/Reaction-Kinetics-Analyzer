import numpy as np


class Thermodynamics:

    def __init__(self, rc1_data):

        self.data = rc1_data.copy()

    def calculate_cumulative_heat(self):

        time = self.data["Time(min)"].values * 60      # seconds
        heat = self.data["HeatFlow(W)"].values         # J/s

        cumulative = np.zeros(len(time))

        for i in range(1, len(time)):

            dt = time[i] - time[i-1]

            cumulative[i] = cumulative[i-1] + (
                heat[i] + heat[i-1]
            ) * dt / 2

        self.data["Cumulative_Heat(J)"] = cumulative

        return self.data

    def total_heat(self):

        return self.data["Cumulative_Heat(J)"].iloc[-1]