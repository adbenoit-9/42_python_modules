from numpy import isin
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


class MyPlotLib:
    def __init__(self) -> None:
        pass

    def histogram(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        try:
            axis = plt.subplots(len(features))[1]
            for i, elem in enumerate(features):
                x = data[elem].tolist()
                axis[i].hist(x, 15, density=False, facecolor='b', alpha=0.75)
                plt.title(elem)
                axis[i].grid(True)
            plt.show()
        except Exception:
            print('Error: Failed to display historgram.')

    def density(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        try:
            axis = plt.subplots()[1]
            for elem in features:
                pd.DataFrame(data[elem]).plot(ax=axis, kind='density')
            plt.show()
        except Exception:
            print('Error: Failed to display density.')

    def pair_plot(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        try:
            sb.pairplot(data.filter(items=features))
            plt.show()
        except Exception:
            print('Error: Failed to display pairplot.')

    def box_plot(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        try:
            data.boxplot(column=features, grid=False)
            plt.show()
        except Exception:
            print('Error: Failed to display boxplot.')
