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
        axis = plt.subplots(len(features))[1]
        for i, elem in enumerate(features):
            x = data[elem].tolist()
            axis[i].hist(x, 15, density=False, facecolor='b', alpha=0.75)
            plt.title(elem)
            axis[i].grid(True)
        plt.show()

    def density(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        axis = plt.subplots()[1]
        for elem in features:
            pd.DataFrame(data[elem]).plot(ax=axis, kind='density')
        plt.show()

    def pair_plot(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        sb.pairplot(data.filter(items=features))
        plt.show()
        

    def box_plot(self, data, features):
        if isinstance(data, pd.DataFrame) is False or \
                isinstance(features, list) is False:
            return None
        my_dict = {}
        for elem in features:
            my_dict[elem] = data[elem].tolist()
        try:
            data.boxplot(column=features, grid=False)
            plt.show()
        except Exception:
            print('Error: Failed to display boxplot.')
