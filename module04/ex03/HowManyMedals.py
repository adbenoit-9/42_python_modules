import pandas as pd


def howManyMedals(df, name):
    """
    Gives the number and type of medals for each year during
    which the participant won medals
    Args:
        df: a pandas.DataFrame which contains the dataset.
        name: participant name.
    Returns:
        dct: a dictionary of dictionaries.
    """
    if isinstance(df, pd.DataFrame) is False or \
            isinstance(name, str) is False:
        return None
    dct = {}
    data = df[df['Name'] == name]
    for year in data.drop_duplicates(subset=['Year']).get('Year'):
        year_data = data[data['Year'] == year]
        dct['{}'.format(year)] = {
            'G': len(year_data[year_data['Medal'] == 'Gold'].index),
            'S': len(year_data[year_data['Medal'] == 'Silver'].index),
            'B': len(year_data[year_data['Medal'] == 'Bronze'].index)
        }
    return dct
