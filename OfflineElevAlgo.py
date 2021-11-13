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

def exportCalls(e_call_assigned):
    new_e_call = []
    for call in e_call_assigned:
        new_e_call.append(call.__dict__.values())
    print(new_e_call) # ONLY FOR Debug.
    fileName = 'Assigned_calls.csv'

    with open(fileName , 'w',newline="") as file:
        csvwriter = csv.writer(file)
        for element in new_e_call:
            csvwriter.writerow(element)



'''
Function for debuging, Delete this after we Done.
(this function change all elevator's value to 1)
'''
def for_debug(calls):
    for i in calls:
        i.elevator = 9
    return 0






"""
this is a test for the csv read
"""


c = []
c = loadCalls("Calls_a.csv")
c[1].elevator=1
print(c)
print("Check for exporting:")
for_debug(c)
print("Print new list:")
print(c)
exportCalls(c)
