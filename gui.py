from main import *

import tkinter


class OurApp(tk.Frame):
    """
    Class authors: Aswatha and Akash

    Class with Methods for generating Graphical User Interface and
    displaying the results and plots. Allows the user to choose the
    discharge data and select the scatter size of the hydrograph plot.

    Attributes:
        master: parameter used to represent the parent window of the
            tkinter
        options: optional arguments

    Methods:
        call_estimator(): using user input to display a dialog with the
                        extrapolated discharge
        sel_discharge_data(): calls the method to get user selected
                            directory and showing the updated message
        select_file(): returns the directory of the user selected
                    discharge data
        estimate_u(): estimates the extrapolated discharge
        plot_hydrograph(): plots the hydrograph
        plot_extrapolation(): plots the extrapolated discharge values
    """

    def __init__(self, master=None, **options):
        """
        Assigning values to the class attributes and all the parameters
        and arguments of the methods.
        :param master: parameter used to represent the parent window
                    of the tkinter
        :param options: optional arguments
        """
        tk.Frame.__init__(self, master, **options)

        self.master.title("GUI for Extrapolation of Hydrograph")
        self.master.iconbitmap("images/icon.ico")

        ww = 648  # width
        wh = 382  # height
        # screen position
        wx = (self.master.winfo_screenwidth() - ww) / 2
        wy = (self.master.winfo_screenheight() - wh) / 2
        # assign geometry
        self.master.geometry("%dx%d+%d+%d" % (ww, wh, wx, wy))

        # assign space holders around widgets
        self.dx = 5
        self.dy = 5

        self.discharge_file = "SELECT"
        self.results = {}
        self.t_series = None
        self.q_series = None
        self.plotter = None
        self.df_data = None

        self.scatter_size = tk.DoubleVar(value=1.0)

        # select Discharge Data Button
        tkinter.Button(master, text='SELECT River Discharge Data',
                       command=lambda: self.sel_discharge_data()).grid(
            row=0, column=0, padx=self.dx, pady=self.dy,
            sticky=tk.W)

        # label for select Discharge Data Button
        self.discharge_label = tk.Label(master,
                                        text="River Discharge Data file "
                                             "(csv): " + self.discharge_file)
        self.discharge_label.grid(row=1, column=0, columnspan=3,
                                  padx=self.dx, pady=self.dy, sticky=tk.W)

        # for Scatter Size Input
        tk.Label(master, text='Specify the size of the scatter plot size: ') \
            .grid(column=0, columnspan=3, row=2, padx=self.dx, pady=self.dy,
                  sticky=tk.W)
        tk.Entry(master, bg="alice blue", width=20,
                 textvariable=self.scatter_size).grid(row=2, column=1,
                                                      padx=self.dx,
                                                      pady=self.dy,
                                                      sticky=tk.W)

        # Hydrograph Label and Button
        tk.Label(master, text="Click here to generate the Hydrograph:").grid(
            column=0, row=5, padx=self.dx, pady=self.dy, sticky=tk.W)
        tkinter.Button(master, text='Hydrograph', width=20,
                       command=lambda: self.plot_hydrograph()).grid(
            row=5, column=1, padx=self.dx, pady=self.dy,
            sticky=tk.W)

        # Extrapolate Label & Button
        tk.Label(master, text="Click here to plot the Extrapolated "
                              "Discharges:").grid(column=0, row=6,
                                                  padx=self.dx, pady=self.dy,
                                                  sticky=tk.W)
        tkinter.Button(master, text='Extrapolation Plot', width=20,
                       command=lambda: self.plot_extrapolation()).grid(
            row=6, column=1, padx=self.dx, pady=self.dy,
            sticky=tk.W)

        # Label for  Return Periods Combobox
        tk.Label(master, text="Select the return period for Estimation:").grid(
            column=0, row=7, padx=self.dx, pady=self.dy, sticky=tk.W)
        # Combobox
        self.cbx_r_period = ttk.Combobox(master, width=5)
        self.cbx_r_period.grid(column=1, row=7, padx=self.dx, pady=self.dy,
                               sticky=tk.W)
        self.cbx_r_period['state'] = 'disabled'
        self.cbx_r_period['values'] = [""]

        # Estimate Discharge Button
        self.eval_button = tk.Button(master, text="Estimate Discharge",
                                     bg="snow2", fg="dark violet",
                                     command=lambda: self.call_estimator())
        self.eval_button.grid(row=8, column=0, padx=self.dx, pady=self.dy,
                              sticky=tk.W)

        self.b_run = tk.Button(master, bg="white", text="Compute", width=30,
                               command=lambda: self.run_program())
        self.b_run.grid(sticky=tk.W, row=3, column=0, padx=self.dx,
                        pady=self.dy)
        self.run_label = tk.Label(master, fg="forest green", text="")
        self.run_label.grid(column=1, columnspan=3, row=3, padx=self.dx,
                            pady=self.dy, sticky=tk.W)

        # Quit Button
        self.close_button = tk.Button(text="Close window", fg='red',
                                      command=lambda: self.master.quit())
        self.close_button.place(anchor=tk.E, x=635, y=310, rely=0.1)

    def run_program(self):
        # ensure that user selected all necessary inputs
        if not self.valid_selections():
            return -1

        if askokcancel("Start calculation?",
                       "Click OK to start the calculation."):

            if self.discharge_file != "SELECT":
                self.results = main(self.discharge_file,
                                    float(self.scatter_size.get()))

            self.df_data = self.results['d_data']
            self.t_series = self.results['t_series']
            self.q_series = self.results['q_series']
            self.plotter = self.results['obj']

            # update run label
            self.b_run.config(fg="forest green")
            self.run_label.config(text="Successfully Executed!!!")
            self.eval_button.config(text=">> Estimate Discharge <<")

            # update and enable combobox
            self.cbx_r_period['state'] = 'readonly'
            self.cbx_r_period['values'] = time_list
            self.cbx_r_period.set('100')

    def call_estimator(self):
        """
        Estimates the discharge by putting the user inputed value to estimate_u() method
        :return: Result in a pop up dialog
        """
        try:
            year = float(self.cbx_r_period.get())
        except tk.TclError:
            return showerror("ERROR", "Non-numeric value entered.")
        self.eval_button.config(fg="green4", bg="DarkSeaGreen1")
        showinfo("Result",
                 "The estimated Discharge is: %0.2f m3/s" % (
                     self.estimate_u(year)))

    def sel_discharge_data(self):
        """
        Select the discharge data file by calling select_file().
        :return: None
        """
        self.discharge_file = self.select_file("Discharge Data file", "csv")
        # update discharge label
        self.discharge_label.config(
            text="River Discharge Data file (csv): " + self.discharge_file)

    def select_file(self, description, file_type):
        """
        open the discharge file that user selects
        :param description: STR of file name in GUI label
        :param file_type: STR of file type in HUI label
        :return: Opening user selected file
        """
        return askopenfilename(filetypes=[(description, file_type)],
                               initialdir=os.path.abspath(""),
                               title="Select a %s file" % file_type,
                               parent=self)

    def plot_hydrograph(self):
        """
        Plots the hydrograph
        :return: shows the plot
        """
        if plot_gumbel is True:
            try:
                self.plotter.plot_discharge(self.results['d_data']['Year'],
                                            self.results['d_data'][
                                                'Discharge ['
                                                'CMS]'],
                                            title='Hydrograph', color='grey')
            except TypeError:
                return np.nan
        else:
            showinfo("WARNING", "Plotting is disabled, enable it from "
                                "config.py")

    def plot_extrapolation(self):
        """
        plots the extrapolated discharge
        :return: shows the plot
        """
        if plot_gumbel is True:
            try:
                # plotting the extrapolated discharge
                self.plotter.gumbel_plotting(self.t_series, self.q_series,
                                             title='Gumbel Extrapolation',
                                             color='blue')
            except TypeError:
                return np.nan
        else:
            showinfo("WARNING", "Plotting is disabled, enable it from "
                                "config.py")

    def estimate_u(self, h):
        """
        estimating the extrapolated discharge
        :param h: user inputed return period
        :return: extrapolated discharge
        """
        try:
            return self.results['return_periods'][h]
        except ValueError:
            showerror("ERROR: Bad values defined.")
            return None
        except TypeError:
            showerror("ERROR: Bad data types defined.")
            return None

    def valid_selections(self):
        if "SELECT" in self.discharge_file:
            showinfo("ERROR", "Please, select the River Discharge Data file.")
            return False
        if self.scatter_size == 0.0:
            showinfo("ERROR", "Specify a size for the scatter points.")
            return False
        if self.scatter_size == 0.0:
            showinfo("ERROR", "Specify a size for the scatter points.")
        return True


if __name__ == '__main__':
    OurApp().mainloop()
