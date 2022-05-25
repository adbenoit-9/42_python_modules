import pandas as pd


class FileLoader:
    def __init__(self) -> None:
        pass

    def load(self, path):
        """
        Loads a dataset ans displays a message specifying the
        dimensions of the dataset.
        Argument:
            path: file path of the dataset to load.
        Returns:
            df: dataset loaded as a pandas.DataFrame.
        """
        try:
            df = pd.read_csv(path)
            print('[{} x {}]'.format(*df.shape))
            return df
        except Exception as err:
            print(err)
            return None

    def display(self, df, n):
        """
        Displays the first n rows of the dataset if n is positive,
        or the last n rows if n is negative.
        Args:
            df: pandas.DataFrame object containing the dataset.
            n: integer.
        Returns:
            None.
        """
        if isinstance(df, pd.DataFrame) is False or \
                isinstance(n, int) is False:
            print('Invalid argument')
            return None
        if n > 0:
            print(df[:n])
        else:
            start = df.shape[0] + n
            print(df[start:])
