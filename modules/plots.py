import plotly.express as px


class PlotGenerator:

    def __init__(self, rc1_data):

        self.data = rc1_data.copy()

    def conversion_plot(self):

        return px.line(
            self.data,
            x="Time(min)",
            y="Conversion",
            markers=True,
            title="Conversion vs Time"
        )

    def concentration_plot(self):

        return px.line(
            self.data,
            x="Time(min)",
            y=["CA (mol/L)", "CB (mol/L)"],
            markers=True,
            title="Concentration vs Time"
        )

    def rate_plot(self):

        return px.line(
            self.data,
            x="Time(min)",
            y="Rate (mol/L/min)",
            markers=True,
            title="Reaction Rate vs Time"
        )

    def predicted_rate_plot(self, fit_data):

        return px.scatter(
            fit_data,
            x="Rate (mol/L/min)",
            y="Predicted Rate",
            title="Experimental vs Predicted Rate"
        )

    def residual_plot(self, fit_data):

        return px.scatter(
            fit_data,
            x="Time(min)",
            y="Residual",
            title="Residual Plot"
        )