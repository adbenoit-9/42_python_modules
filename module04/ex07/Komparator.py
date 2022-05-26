from unicodedata import category
import pandas as pd
from MyPlotLib import MyPlotLib
import matplotlib.pyplot as plt
import numpy as np
import math


class Komparator:
    def __init__(self, data) -> None:
        if isinstance(data, pd.DataFrame) is False:
            raise ValueError('Invalid dataset')
        self.data = data

    def compare_box_plots(self, categorical_var, numerical_var):
        try:
            self.data.boxplot(column=[numerical_var], by=categorical_var,
                              figsize=(20, 10))
            plt.show()
        except Exception:
            print('Error: Failed to display compare boxplots.')

    def density(self, categorical_var, numerical_var):
        try:
            categories = self.data[categorical_var].unique()
            for i, x in enumerate(categories):
                if isinstance(x, float) and math.isnan(x):
                    categories = np.delete(categories, i)
                    break
            axis = plt.subplots(figsize=(20, 10))[1]
            for elem in categories:
                x = self.data[self.data[categorical_var] == elem]
                x = x[numerical_var].to_list()
                pd.DataFrame({elem: x}).plot(ax=axis, kind='density')
            plt.xlabel(numerical_var)
            plt.show()
        except Exception:
            print('Error: Failed to display density.')

    def compare_histograms(self, categorical_var, numerical_var):
        try:
            categories = self.data[categorical_var].unique()
            for i, x in enumerate(categories):
                if isinstance(x, float) and math.isnan(x):
                    categories = np.delete(categories, i)
                    break
            figure, axis = plt.subplots(1, len(categories), figsize=(20, 10))
            for i, elem in enumerate(categories):
                y = self.data[self.data[categorical_var] == elem]
                y = y[numerical_var].to_list()
                axis[i].hist(y, 15, density=False, facecolor='b', alpha=0.75)
                axis[i].set_xlabel(numerical_var)
                axis[i].set_title(elem)
                axis[i].grid(True)
            plt.show()
        except Exception:
            print('Error: Failed to display compare histograms.')
