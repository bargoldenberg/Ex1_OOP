import math

from Call import *
from Building import *
import sys

def load_calls(file_name):
    # if __name__ == '__main__':
        rows = []
        calls = []
        with open(file_name) as e_calls:
            csvreader = csv.reader(e_calls)
            for row in csvreader:
                c = Call(row[0], row[1], row[2], row[3], row[4],row[5])
                calls.append(c)
                rows.append(row)

        return calls


def export_calls(e_call_assigned, output):
    new_e_call = []
    for call in e_call_assigned:
        new_e_call.append(call.__dict__.values())
    fileName = output

    with open(fileName , 'w',newline="") as file:
        csvwriter = csv.writer(file)
        for element in new_e_call:
            csvwriter.writerow(element)
'''
This function checks if a call is on the way or not.
'''
def correct_state(call, curr_dest, direction, call_list, current_elevator):
    if len(call_list)==0:
        return call.src >= curr_dest and direction == 1 or call.src <= curr_dest and direction == -1
    else:
        condition1 = call.src >= call_list[len(call_list)-1].src and direction == 1 or call.src <= call_list[len(call_list)-1].src and direction == -1
        condition2 = calc_time(call,call_list,current_elevator)<=float(call.time)-float(call_list[len(call_list)-1].time)
        return condition2 and condition1

def calc_time(call,call_list,current_elevator):
    time = (abs(float((call_list[len(call_list)-1].src))+abs(float(call.src)))/float(current_elevator.speed))+current_elevator.startTime+current_elevator.stopTime+current_elevator.openTime+current_elevator.closeTime
    return time

def direction(call):
    if call.dest > call.src:
        return 1
    else:
        return -1

def max_trip(b,curr_elev) -> float:
    slowest_elev = b.FindSlowestElevator(curr_elev)
    slowest_speed = slowest_elev.speed
    floors = (abs(b._minFloor) + abs(b._maxFloor))
    total_open = slowest_elev.openTime
    total_close = slowest_elev.closeTime
    total_start = slowest_elev.startTime
    total_stop = slowest_elev.stopTime
    all_delays=total_open+total_stop+total_close+total_start
    return float(floors / slowest_speed)+all_delays

def change_direction(b, calls, curr_elev, first_call, curr_dest,call_list,max_trip1):
    for call in calls:
        if float(call.time) > float(first_call) + max_trip1:
            break
        if correct_state(call, curr_dest, direction(call), call_list, b.FindFastestElevator(curr_elev)):
            curr_dest = call.dest
            call.elevator = b.FindFastestElevator(curr_elev).id
            call_list.append(call)
            calls.remove(call)
    return call_list

def allocate_elevators(b, calls):
    all_calls = []
    call_list = []
    call_list1 = []
    max_trip1 = max_trip(b,[])
    curr_dest = '0'
    elevator_counter = 0
    curr_elev = []
    while not len(calls) == 0:
        first_call = calls[0].time
        if elevator_counter == len(b._elevators):
            curr_elev = []
            elevator_counter = 0
        for call in calls:
            condition: bool = float(call.time) > float(first_call) + max_trip1 or float(calls[len(calls)-1].time)<max_trip1+float(first_call) and not correct_state(call, curr_dest, direction(call),call_list1,b.FindFastestElevator(curr_elev))
            if condition:
                if len(call_list1) != 0:
                    all_calls.append(call_list1)
                    call_list1 = []
                while condition:
                    if len(curr_elev) == len(b._elevators):
                        break
                    if not len(calls) == 0:
                        curr_dest = calls[0].src
                    max_trip1 = max_trip(b,[])
                    call_list1 = change_direction(b, calls, curr_elev, first_call, curr_dest, call_list1, max_trip1)
                    if len(call_list1) != 0:
                        all_calls.append(call_list1)
                        call_list1=[]
                    used_elev = b.FindFastestElevator(curr_elev)
                    curr_elev.append(used_elev)
                    elevator_counter += 1
                tmp_list = allocate_to_bunch(b, all_calls, call_list1)
                all_calls = []
                for call in tmp_list:
                    call_list.append(call)
                call_list1 = []
                break
            if correct_state(call, curr_dest, direction(call),call_list1,b.FindFastestElevator([])):
                curr_dest = call.dest
                chosen_elevator = b.FindFastestElevator([])
                call.elevator = chosen_elevator
                if chosen_elevator not in curr_elev:
                    curr_elev.append(chosen_elevator)
                    elevator_counter += 1
                call_list1.append(call)
                calls.remove(call)
    call_list.sort(key=lambda x: float(x.time))
    return call_list

def allocate_to_bunch(b, all_calls, call_list2):
    curr_elev = []
    while len(all_calls) != 0:
        max_len = 0
        for bunch in all_calls:
            if len(bunch)>max_len:
                max_len=len(bunch)
                largest_bunch=bunch
        all_calls.remove(largest_bunch)
        for call in largest_bunch:
            if len(curr_elev) == len(b._elevators):
                curr_elev = []
            tmp_elev=b.FindFastestElevator(curr_elev).id
            call.elevator = tmp_elev
        curr_elev.append(tmp_elev)
        for call in largest_bunch:
            call_list2.append(call)
    return call_list2
"""
this is a test for the csv read

def run(list):
    building_json = list[1]
    #building_json='B5.json'
    calls_csv = list[2]
    #calls_csv='Calls_b.csv'
    output = list[3]
    #output='output.csv'
    c = load_calls(calls_csv)
    b2 = Building()
    b2.load_json(building_json)
    c = allocate_elevators(b2, c)
    export_calls(c, output)
if __name__ == '__main__':
    list = sys.argv
    run(list)
#for commit

b4 = Building()
b5 = Building()

b4.load_json("B4.json")
b5.load_json("B5.json")

call1 = load_calls("myCsvForTest.csv")


ans1 = allocate_elevators(b4,call1)
export_calls(ans1,"call_List_For_test.csv")

"""