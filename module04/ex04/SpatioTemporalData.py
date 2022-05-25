import pandas as pd


class SpatioTemporalData:
    def __init__(self, dataset):
        if isinstance(dataset, pd.DataFrame) is False:
            raise ValueError('Invalid dataset')
        self.data = dataset
        pass

    def when(self, location):
        """
        Returns:
            years: a list containing the years where games were
            held in the given location
        """
        filtered = self.data[self.data['City'] == location]
        years = filtered.drop_duplicates(subset=['Year'])['Year']
        return years.tolist()

    def where(self, date):
        """
        Returns:
            location: returns the location where the
            Olympics took place in the given year.
        """
        filtered = self.data[self.data['Year'] == date]
        location = filtered.drop_duplicates(subset=['City'])['City']
        return location.tolist()
