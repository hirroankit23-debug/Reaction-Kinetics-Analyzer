class Conversion:

    def __init__(self, rc1_data, experiment):

        self.data = rc1_data.copy()
        self.exp = experiment

    def calculate(self):

        delta_h = abs(
            float(self.exp.loc[0, "Heat_of_Reaction_kJ_mol"])
        ) * 1000

        CA0 = float(self.exp.loc[0, "Initial_EA_M"])

        volume = float(
            self.exp.loc[0, "Working_Volume_L"]
        )

        initial_moles = CA0 * volume

        total_heat = initial_moles * delta_h

        self.data["Conversion"] = (
            self.data["Cumulative_Heat(J)"] /
            total_heat
        )

        self.data["Conversion"] = self.data[
            "Conversion"
        ].clip(0, 1)

        return self.data