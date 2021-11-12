import json
from Elevator import Elevator

class Building:
    def __init__(self):
        self._minFloor = 0
        self._maxFloor = 0
        self._elevators = [] # matching type as the Json


    def load_json(self,file_name):
        try:
            with open(file_name , "r+") as f:
                my_e=[]
                my_d = json.load(f)
                self._minFloor = my_d["_minFloor"]
                self._maxFloor = my_d["_maxFloor"]
                ele_l = my_d["_elevators"]
                #for elem in ele_l:
                for k,v in elem.items():
                    print(ele_l)
                    print(v["_id"])
                    #e=Elevator(id=v["_id"], speed=v["_speed"], minFloor=v["_minFloor"], maxFloor=v["_maxFloor"],
                    #           closeTime=v["_closeTime"], openTime=v["_openTime"], startTime=v["_startTime"], stopTime=v["_stopTime"])
                    #e = Elevator(**v)
                    #my_e[e.id]=e
               self._elevators = my_e
        except IOError as e:
            print(e)

""""
self,id: int=0,speed: float=0,minFloor: int =0,maxFloor: int =0,closeTime: float=0,openTime: float=0, startTime: float=0,stopTime: float=0
"""

b=Building()
b.load_json("B1.json")
print(b._minFloor)