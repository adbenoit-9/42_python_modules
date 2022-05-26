import pandas as pd


def youngestfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    if isinstance(df, pd.DataFrame) is False or \
            isinstance(year, int) is False or year < 0:
        return None
    women = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    men = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    dct = {
        'f': 'nan' if len(women) == 0 else min(women['Age']),
        'm': 'nan' if len(men) == 0 else min(men['Age']),
    }
    return dct
