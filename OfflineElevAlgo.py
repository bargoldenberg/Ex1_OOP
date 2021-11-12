import csv
import Call



def callRead( file_name):
    if __name__ == '__main__':
        rows = []
        calls = []
        with open(file_name) as e_calls:
            csvreader = csv.reader(e_calls)
            for row in csvreader:
                c = Call.Call(row[0], row[1], row[2], row[3], row[4],row[5])
                #c = Call(call = rows[0],time=rows[1] , src=rows[2], dest=rows[3] ,elevator=rows[4] ,F=rows[5])
                calls.append(c)
                rows.append(row)
    return calls

"""
this is a test for the csv read
"""
c = []
c = callRead("Calls_a.csv")
print(c.pop(0))
