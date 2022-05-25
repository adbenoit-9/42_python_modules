from FileLoader import FileLoader
from HowManyMedalsByCountry import howManyMedalsByCountry


if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../data/athlete_events.csv')
    print(howManyMedalsByCountry(data, "United States"))
