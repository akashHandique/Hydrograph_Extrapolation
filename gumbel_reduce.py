from config import pd


def gumbel_reduce_data(csv_file=''):
    """
    Extracting the Gumbel Reduced data as a pandas DataFrame
    :param csv_file: STR of the Gumbel Reduce mean and std data file
                    ("gumbel.csv")
    :return: pandas DataFrame of the Gumbel Reduce Data
    """
    reduced_data = pd.read_csv(csv_file, header=0,
                               sep=',',
                               names=['Data Index', 'Reduced mean',
                                      'Reduced std'],
                               usecols=[0, 1, 2],
                               index_col='Data Index')
    return reduced_data
