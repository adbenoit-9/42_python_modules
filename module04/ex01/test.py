from YoungestFellah import youngfellah
from FileLoader import FileLoader

df = FileLoader().load('../data/athlete_events.csv')
print(youngfellah(df, 1988))
print(youngfellah(df, 2004))
print(youngfellah(df, 1991))
