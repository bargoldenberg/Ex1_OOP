import json
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

    def FindFastestElevator(self):
        fastest=0
        fastestelev=0
        for elev in self._elevators:
            currspeed=elev.speed
            if currspeed>fastest:
                fastest=currspeed
                fastestelev=elev.id
        return fastestelev
""""
self,id: int=0,speed: float=0,minFloor: int =0,maxFloor: int =0,closeTime: float=0,openTime: float=0, startTime: float=0,stopTime: float=0
"""

b=Building()
b2=Building()
b2.load_json("B2.json")
b.load_json("B1.json")
b5=Building()
b5.load_json("B5.json")
print(b)
print(b2)
print(b5)
print(b2.FindFastestElevator())
print(b5.FindFastestElevator())



