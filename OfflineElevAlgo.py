import csv
import Call



def callRead( file_name):
    if __name__ == '__main__':
        rows = []
        calls = []
        with open(file_name) as e_calls:
            cvsreader = csv.reader(e_calls)
            for rows in cvsreader:
                c = Call(call = rows[0],time=rows[1] , src=rows[2], dest=rows[3] ,elevator=rows[4] ,F=rows[5])
                calls.append(c)
                rows.append(rows)
    return calls

