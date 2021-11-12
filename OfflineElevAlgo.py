import csv
from Call import *

def loadCalls(file_name):
    if __name__ == '__main__':
        rows = []
        calls = []
        with open(file_name) as e_calls:
            csvreader = csv.reader(e_calls)
            for row in csvreader:
                c = Call(row[0], row[1], row[2], row[3], row[4],row[5])
                calls.append(c)
                rows.append(row)
    return calls

"""
this is a test for the csv read
"""
c = []
c = loadCalls("Calls_a.csv")
c[1].elevator=1
print(c)
