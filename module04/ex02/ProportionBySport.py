import pandas as pd


def proportionBySport(df, year, sport, gender):
    """
    Compute the proportion (percentage) of participants
    who played the given sport among the participants
    of the given gender.
    Args:
        df: a pandas.DataFrame of the dataset.
        year: an olympic year (positive integer)
        sport: a sport (string)
        gender: a gender ('F' or 'M')
    Returns:
        prop: a float corresponding to the proportion.
    """
    if isinstance(df, pd.DataFrame) is False or \
            isinstance(year, int) is False or year < 0 or \
            isinstance(sport, str) is False or \
            isinstance(gender, str) is False or \
            (gender != 'F' and gender != 'M'):
        return None
    filtered = df[(df['Year'] == year) & (df['Sex'] == gender)]
    total = len(filtered.drop_duplicates(subset=['ID']).index)
    filtered = filtered[filtered['Sport'] == sport]
    filtered = filtered.drop_duplicates(subset=['ID'])
    n = len(filtered.index)
    return n / total
