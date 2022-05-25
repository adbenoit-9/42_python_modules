from MyPlotLib import MyPlotLib
from FileLoader import FileLoader

if __name__ == "__main__":
    mpl = MyPlotLib()
    f = FileLoader()
    data = f.load('../data/athlete_events.csv')
    # mpl.histogram(data, ['Height', 'Weight'])
    # mpl.density(data, ['Height', 'Weight'])
    # mpl.pair_plot(data, ['Height', 'Weight'])
    mpl.box_plot(data, ['Height', 'Weight'])