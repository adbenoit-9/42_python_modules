class CsvReader(object):
    def __init__(self, file_name):
        self.file = open(file_name, 'r')
        self.data = []

    def __enter__(self):
        lines = self.file.readlines()
        for line in lines:
            self.data.append(line.split(','))
        return self

    def __exit__(self, type, value, traceback):
        self.file.close()

    def getdata(self):
        for line in self.data:
            print(line)
        return self.data

if __name__ == "__main__":
    with CsvReader('good.csv') as file:
        data = file.getdata()
        # header = file.getheader()