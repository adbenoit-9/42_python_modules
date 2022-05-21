import sys

class CsvReader(object):
    def __init__(self, file_name=None, sep=',', header=False, skip_top=0, skip_bottom=0):
        try:
            self.file = open(file_name, 'r')
            self.data = []
            self.sep = sep
            self.header = header
            self.skip_top = skip_top
            self.skip_bottom = skip_bottom
        except:
            self.file = None

    def __enter__(self):
        if self.file is None:
            return None
        lines = self.file.read().splitlines()
        for i, line in enumerate(lines):
            self.data.append(line.split(self.sep))
            if i == 0:
                len_ref = len(self.data[i])
            if len(self.data[i]) != len_ref:
                return None
            for j, word in enumerate(self.data[i]):
                if len(word) == 0:
                    return None
                self.data[i][j] = word.strip(' ')
                self.data[i][j] = self.data[i][j].strip('"')
        return self

    def __exit__(self, type, value, traceback):
        if self.file is not None:
            self.file.close()

    def getdata(self):
        """ Retrieves the data/records from skip_top to skip bottom.
        Returns:
            nested list (list(list, list, ...)) representing the data.
        """
        start = self.skip_top + 1 if self.header else self.skip_top 
        end = len(self.data) - self.skip_bottom
        return self.data[start:end]

    def getheader(self):
        """ Retrieves the header from csv file.
        Returns:
            list: representing the data (when self.header is True).
        None: (when self.header is False).
        """
        if self.header is False:
            return None
        return self.data[0]
