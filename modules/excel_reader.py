import pandas as pd


class ExcelReader:

    """
    Reads the standard RC1e Excel workbook.

    Returns
    -------
    experiment : pandas.DataFrame
        Experiment information sheet

    rc1_data : pandas.DataFrame
        Time-dependent RC1e data
    """

    def __init__(self, file_path):

        self.file_path = file_path

        self.experiment = None
        self.rc1_data = None

    def read(self):

        try:

            self.experiment = pd.read_excel(
                self.file_path,
                sheet_name="Experiment_Info"
            )

            self.rc1_data = pd.read_excel(
                self.file_path,
                sheet_name="RC1e_Data"
            )

            return self.experiment, self.rc1_data

        except Exception as e:

            raise Exception(
                f"Error reading Excel file : {e}"
            )