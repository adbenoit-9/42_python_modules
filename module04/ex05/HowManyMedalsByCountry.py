import pandas as pd


def howManyMedalsByCountry(df, name):
    if isinstance(df, pd.DataFrame) is False or \
            isinstance(name, str) is False:
        return None
    dct = {}
    team_sports = ['Basketball', 'Football',  'Tug-Of-War',
                   'Badminton', 'Sailing', 'Handball', 'Water Polo',
                   'Hockey', 'Rowing', 'Bobsleigh', 'Softball',
                   'Volleyball', 'Synchronized Swimming', 'Baseball',
                   'Rugby Sevens', 'Rugby', 'Lacrosse', 'Polo']
    data = df[df['Team'] == name]
    team_data = data[data.Sport.isin(team_sports)]
    team_data = team_data.drop_duplicates(['Year', 'Medal', 'Event'])
    others = data[~data.Sport.isin(team_sports)]
    data = pd.concat([team_data, others])
    years = data.drop_duplicates(subset=['Year']).sort_values('Year')
    for year in years.get('Year'):
        year_data = data[data['Year'] == year]
        dct[year] = {
            'G': len(year_data[year_data['Medal'] == 'Gold'].index),
            'S': len(year_data[year_data['Medal'] == 'Silver'].index),
            'B': len(year_data[year_data['Medal'] == 'Bronze'].index)
        }
    return dct
