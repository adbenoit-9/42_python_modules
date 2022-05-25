from FileLoader import FileLoader
from SpatioTemporalData import SpatioTemporalData

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    sp = SpatioTemporalData(data)
    print(sp.where(1896))
    print(sp.where(2016))
    print(sp.when('Athina'))
    print(sp.when('Paris'))
    print(sp.where(2000))
    print(sp.where(1980))
    print(sp.when('London'))

    print(sp.where('1980'))
    print(sp.when('Unknown'))
    print(sp.when(1980))
    try:
        sp = SpatioTemporalData(1)
    except ValueError as err:
        print(err)
