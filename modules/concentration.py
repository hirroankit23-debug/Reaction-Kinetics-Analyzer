class Concentration:

    def __init__(self, rc1_data, experiment):

        self.data = rc1_data.copy()
        self.exp = experiment

    def calculate(self):

        CA0 = float(self.exp.loc[0, "Initial_EA_M"])
        CB0 = float(self.exp.loc[0, "Initial_NaOH_M"])

        self.data["CA (mol/L)"] = CA0 * (
            1 - self.data["Conversion"]
        )

        self.data["CB (mol/L)"] = CB0 * (
            1 - self.data["Conversion"]
        )

        self.data["Moles Reacted"] = (
            self.data["Conversion"] *
            CA0 *
            float(self.exp.loc[0, "Working_Volume_L"])
        )

        return self.data