from config import *


class DischargeDataHandler:
    """
    Class author: Aswatha

    Class with Methods for handling and printing the Discharge Data.
    Extracting data from user inputted ".csv" file and sorting the data.
    Computing the Annual max and adding it to the DataFrame.

    Attributes:
        data_csv_file: STR of filename

    Methods:
        get_discharge_data(): Method creates a pandas DataFrame from
                            input Discharge Data after instantiation
        print_discharge_data(): Method prints the DataFrame
    """

    def __init__(self, data_csv_file):
        """
        Assign values to class attributes when an object is
        instantiated.
        :param data_csv_file: STR of the file name
        """
        self.sep = ';'
        self.data_csv_file = data_csv_file
        self.discharge_data = pd.DataFrame

    def get_discharge_data(self):
        """
        Method creates a pandas DataFrame from input Discharge Data
        after instantiation
        :return: annual_max: pd DataFrame with Discharge and Year cols
        """
        self.discharge_data = pd.read_csv(self.data_csv_file, header=10,
                                          names=['Date', 'Discharge [CMS]'],
                                          sep=self.sep,
                                          usecols=[0, 1], parse_dates=[0],
                                          index_col='Date')
        annual_max = self.discharge_data.resample(rule='A',
                                                  kind='period').max()
        annual_max["Year"] = annual_max.index.year
        annual_max.reset_index(inplace=True, drop=True)
        return annual_max

    def print_discharge_data(self):
        """
        Method prints the DataFrame
        :return: None
        """
        print(self.discharge_data)
