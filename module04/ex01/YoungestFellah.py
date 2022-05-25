def youngfellah(df, year):
    """
    Get the name of the youngest woman and man for the given year.
    Args:
        df: pandas.DataFrame object containing the dataset.
        year: integer corresponding to a year.
    Returns:
        dct: dictionary with 2 keys for female and male athlete.
    """
    women = df[(df['Year'] == year) & (df['Sex'] == 'F')]
    men = df[(df['Year'] == year) & (df['Sex'] == 'M')]
    dct = {
        'f': 'nan' if len(women) == 0 else min(women['Age']),
        'm': 'nan' if len(men) == 0 else min(men['Age']),
    }
    return dct
