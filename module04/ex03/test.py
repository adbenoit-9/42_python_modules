from FileLoader import FileLoader
from HowManyMedals import howManyMedals

if __name__ == "__main__":
    loader = FileLoader()
    data = loader.load('../ressources/athlete_events.csv')
    print(howManyMedals(data, 'Gary Abraham'))
    print(howManyMedals(data, 'Yekaterina Konstantinovna Abramova'))
    print(howManyMedals(data, 'Kristin Otto'))
