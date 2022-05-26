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
    try:
        filtered = df[(df['Year'] == year) & (df['Sex'] == gender)]
        total = len(filtered.drop_duplicates(subset=['ID']).index)
        filtered = filtered[filtered['Sport'] == sport]
        filtered = filtered.drop_duplicates(subset=['ID'])
        n = len(filtered.index)
        if n == 0:
            return 0.
        return n / total
    except Exception:
        return None
