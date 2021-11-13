import csv
from Call import *
from Building import *
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

def for_debug(calls):
    for i in calls:
        i.elevator = 9
    return 0

def correct_state(call, curr_dest, direction):
    return call.dest > curr_dest and direction == 1 or call.dest < curr_dest and direction == -1


def direction(call):
    if call.dest > call.src:
        return 1
    else:
        return -1


def max_trip(b) -> float:
    slowest_elev = b.FindSlowestElevator()
    slowest_speed = slowest_elev.speed
    floors = (abs(b._minFloor) + abs(b._maxFloor))
    total_open = slowest_elev.openTime * floors
    total_close = slowest_elev.closeTime * floors
    total_start = slowest_elev.startTime * floors
    total_stop = slowest_elev.stopTime * floors
    return float(floors / slowest_speed + total_open + total_stop + total_close + total_start)


def change_direction(b, calls, curr_elev, first_call, curr_dest):
    max_trip1 = max_trip(b)
    for call in calls:
        if float(call.time) > float(first_call) + max_trip1:
            break
        if correct_state(call, curr_dest, direction(call)):
            curr_dest = call.dest
            call.elevator = b.FindFastestElevator(curr_elev).id
            calls.remove(call)


def allocate_elevators(b, calls):
    call_list = []
    e = Elevator()
    max_trip1 = max_trip(b)
    curr_elev = b.FindFastestElevator(e)
    curr_dest = calls[0].src
    while not len(calls) == 0:
        first_call = calls[0].time
        for call in calls:
            if float(call.time) > float(first_call) + max_trip1:
                curr_dest = calls[0].src
                change_direction(b, calls, curr_elev, first_call, curr_dest)
                break
            if correct_state(call, curr_dest, direction(call)):
                curr_dest = call.dest
                call.elevator = b.FindFastestElevator(e).id
                calls.remove(call)


"""
this is a test for the csv read
"""
c = []
c = loadCalls("Calls_a.csv")
c[1].elevator=1
print(c)
c = loadCalls("Calls_a.csv")
c[1].elevator=1
print(c)
print("Check for exporting:")
for_debug(c)
print("Print new list:")
print(c)
exportCalls(c)
#for commit