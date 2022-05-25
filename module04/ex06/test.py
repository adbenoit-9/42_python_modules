from MyPlotLib import MyPlotLib
import pandas as pd

if __name__ == "__main__":
    mpl = MyPlotLib()
    data = pd.read_csv('../data/athlete_events.csv')
    mpl.histogram(data, ['Height', 'Weight'])
    mpl.density(data, ['Height', 'Weight'])
    mpl.pair_plot(data, ['Height', 'Weight'])
    mpl.box_plot(data, ['Height', 'Weight'])
