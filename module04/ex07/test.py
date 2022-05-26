from Komparator import Komparator
import pandas as pd

if __name__ == '__main__':
    data = pd.read_csv('../data/athlete_events.csv')
    komp = Komparator(data)
    komp.compare_box_plots('Medal', 'Age')
    komp.compare_histograms('Medal', 'Height')
    komp.density('Medal', 'Weight')
