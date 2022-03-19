from config import *


class PlotDischarge:
    """
    Class author: Akash

    Class for handling Discharge Data as numpy and Pandas DataFrame and
    plotting the Hydrograph along with Extrapolated Discharge.
    Flexibilize the plotting parameter (scatter size) using
    Magic Methods.

    Attributes:
        None

    Methods:
        __mul__(): Magic Method to multiply scatter plot size by
                a factor of 10
        __gt__(): Magic Method to warn the user whether the scatter
                plot size is too large
        __lt__(): Magic Method to warn the user whether the scatter
                plot size is too small
        plot_discharge(): Method to Plot the Hydrograph
        gumbel_plotting(): Method to Plot the Extrapolated Discharge
    """
    def __init__(self):
        """
        Assigning the input values to the class attributes and the
        scaling parameters.
        :param: None
        """
        self.t = pd.Series
        self.q = pd.Series
        self.T = np.array
        self.Q = np.array
        self.c = str
        self.s = 10

    def __mul__(self, multiplier):
        """
        Magic Method to multiply scatter plot size by a factor of 10
        :param multiplier: user inputted multiplying factor
        :return: self.s: size of the scatter plot
        """
        self.s *= multiplier
        return self.s

    def __gt__(self, value):
        """
        Magic Method to warn the user whether the scatter plot size
        is too large
        :param value: user inputted maximum threshold
        :return: Warning MSG if the scatter size is too large
        """
        if self.s > value:
            return logging.warning('WARNING: The Hydrograph scatter points '
                                   'are too large')

    def __lt__(self, value):
        """
        Magic Method to warn the user whether the scatter plot size
        is too small
        :param value: user inputted minimum threshold
        :return: Warning MSG if the scatter size is too small
        """
        if self.s < value:
            return logging.warning('WARNING: The Hydrograph scatter points '
                                   'are too small')

    def plot_discharge(self, time_series=pd.Series(), q_series=pd.Series(),
                       title="", color=""):
        """
        Method to Plot the Hydrograph
        :param time_series: pandas DataSeries for x-coordinates
        :param q_series: Pandas DataSeries for y-coordinates
        :param title: Plot Title as STR
        :param color: STR of Scatter plot color
        :return: None
        """
        self.t = time_series
        self.q = q_series
        self.c = color
        fig, axes = plt.subplots(figsize=(10, 6))
        axes.scatter(x=self.t, y=self.q, marker='o', s=self.s, color=self.c)
        axes.set(xlabel="Years", ylabel="Discharge [CMS]", title=title)
        plt.xlim(self.t.min(), self.t.max())
        plt.grid()
        plt.show()

    def gumbel_plotting(self, t_series, q_series, title='', color=''):
        """
        Method to Plot the Extrapolated Discharge
        :param t_series: numpy array for x-coordinates
        :param q_series: numpy array for y-coordinates
        :param title: Title of the Line Graph as STR
        :param color: STR of Line Graph color
        :return: None
        """
        self.T = t_series
        self.Q = q_series
        fig, axes = plt.subplots(figsize=(10, 6))
        axes.plot(self.T, self.Q, linestyle="-", label='Extrapolation',
                  marker="x", color=color)
        axes.legend()
        axes.set(xlabel="Flood return periods [years]", ylabel="Discharge [CMS]",
                 title=title)
        axes.set_xlim((0, 1000))
        axes.set_ylim((0, 400))
        axes.autoscale()
        plt.grid()
        plt.show()
