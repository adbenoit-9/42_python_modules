import pandas as pd


class Komparator:
    def __init__(self, data) -> None:
        if isinstance(data, pd.DataFrame) is False:
            raise ValueError('Invald dataset')

    def compare_box_plots(self, categorical_var, numerical_var):
        pass

    def density(self, categorical_var, numerical_var):
        pass

    def compare_histograms(self, categorical_var, numerical_var):
        pass
