from YoungestFellah import youngestfellah
from FileLoader import FileLoader

df = FileLoader().load('../data/athlete_events.csv')
print(youngestfellah(df, 1992))
print(youngestfellah(df, 2004))
print(youngestfellah(df, 2010))
print(youngestfellah(df, 2003))
