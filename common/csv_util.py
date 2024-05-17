import csv


def readCsv(fpath):
    with open(fpath, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        data = [row for row in reader]
        print(data)
    return data