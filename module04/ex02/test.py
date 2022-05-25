from FileLoader import FileLoader
from ProportionBySport import proportionBySport


if __name__ == '__main__':
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print("")
    print(proportionBySport(data, 2004, 'Tennis', 'F'))
    print(proportionBySport(data, 2008, 'Hockey', 'F'))
    print(proportionBySport(data, 1964, 'Biathlon', 'M'))
