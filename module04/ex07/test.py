from Komparator import Komparator

if __name__ == '__main__':
    komp = Komparator()
    komp.compare_box_plots('Medal', 'Age')
    komp.compare_histograms('Medal', 'Height')
    komp.compare_histograms('Medal', 'Weight')
