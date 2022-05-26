import pandas as pd
from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt

class Komparator:
    def __init__(self, data) -> None:
        if isinstance(data, pd.DataFrame) is False:
            raise ValueError('Invald dataset')
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        try:
            self.data.boxplot(column=[numerical_var], by=categorical_var)
            plt.show()
        except Exception:
            print('Error: Failed to display compare boxplot.')


    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        age_list = [8, 10, 12, 14, 72, 74, 76, 78, 20, 25, 30, 35, 60, 85]
        df = pd.DataFrame({"gender": list("MMMMMMMMFFFFFF"), "age": age_list})
        ax = df.plot.hist(column=["age"], by="gender", figsize=(10, 8))
        # self.data.plot.hist(column=[numerical_var], by=categorical_var, figsize=(10, 8))
        # plt.show()
        # plt.grid(True)
        pass
