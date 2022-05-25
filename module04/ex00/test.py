from FileLoader import FileLoader

if __name__ == "__main__":
    f = FileLoader()
    df = f.load('athlete_events.csv')
    f.display(df, 3)
    f.display(df, -3)
    f.display(df, 0)
    f.display(df, "lol")
