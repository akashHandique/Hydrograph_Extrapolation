"""User input files, folder paths, and required packages are imported
and specified here"""

# import necessary basic python libraries
try:
    import logging
    import os
    import math
except ModuleNotFoundError as basic:
    print(
        'ModuleNotFoundError: Missing basic libraries (required: logging, '
        'os, math)')
    print(basic)

# import global python libraries
try:
    import numpy as np
    import pandas as pd
    import matplotlib.pyplot as plt
    from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
    import tkinter as tk
    from tkinter import ttk  # for Combobox widget

    # to select files or folders
    from tkinter.filedialog import askopenfilename, askdirectory
    from tkinter.messagebox import askokcancel, showinfo  # infoboxes
    from tkinter.messagebox import showerror
except ModuleNotFoundError as additional:
    print(
        'ModuleNotFoundError: Missing global packages (required: numpy, '
        'pandas, maptlotlib, tkinter)')
    print(additional)


# User Input files Path for Data

# Discharge_data.csv file path
# Specify the path of the Discharge data in GUI

# gumbel_reduce_data.csv file path
gumbel_reduce_path = os.path.abspath('') + '/gumbel_reduced/gumbel.csv'

# Disable (False) or enable (True) plot
plot_gumbel = True

try:
    os.path.isfile(gumbel_reduce_path)
except FileNotFoundError:
    logging.error('ERROR: Gumbel Reduce file is missing')
