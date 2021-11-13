import json
import sys
from Elevator import Elevator

class Building:
    def __init__(self):
        self._minFloor = 0
        self._maxFloor = 0
        self._elevators = [] # matching type as the Json
    def __repr__(self):
        return f"minFloor:{self._minFloor}  ; maxFloor:{self._maxFloor} ; elevators: {self._elevators}"
    def load_json(self,file_name):
        try:
            with open(file_name , "r+") as f:
                my_e=[]
                my_d = json.load(f)
                self._minFloor = my_d["_minFloor"]
                self._maxFloor = my_d["_maxFloor"]
                ele_l = my_d["_elevators"]
                for v in ele_l:
                    e = Elevator(**v)
                    my_e.append(e)
            self._elevators = my_e
        except IOError as e:
            print(e)

    def FindFastestElevator(self,full_elev):
        e=Elevator
        fastest=0
        for elev in self._elevators:
            curr_speed=elev.speed
            if curr_speed>fastest and elev is not full_elev:
                fastest=curr_speed
                e=elev
        return e

    def FindSlowestElevator(self):
        e=Elevator()
        slowest = sys.maxsize

        for elev in self._elevators:
            curr_speed=elev.speed
            if curr_speed<slowest:
                slowest=curr_speed
                e=elev
        return e



""""
self,id: int=0,speed: float=0,minFloor: int =0,maxFloor: int =0,closeTime: float=0,openTime: float=0, startTime: float=0,stopTime: float=0
"""





