import json

class Elevator:
    def __init__(self,_id: int=0,_speed: float=0,_minFloor: int =0,_maxFloor: int =0,_closeTime: float=0,_openTime: float=0, _startTime: float=0,_stopTime: float=0) -> None:
        self.id=_id
        self.speed=_speed
        self.minFloor=_minFloor
        self.maxFloor=_maxFloor
        self.closeTime=_closeTime
        self.openTime=_openTime
        self.startTime=_startTime
        self.stopTime=_stopTime
    def __repr__(self):
        return f"id:{self.id} ; speed:{self.speed} ; minFloor:{self.minFloor} ; maxFloor:{self.maxFloor} ; closeTime:{self.closeTime} ; openTime:{self.openTime} ; startTime:{self.startTime} ; stopTime:{self.stopTime} "
    def from_json(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self.id = di["_id"]
            self.speed = di["_speed"]
            self.minFloor = di["_minFloor"]
            self.maxFloor = di["_maxFloor"]
            self.closeTime = di["_closeTime"]
            self.openTime = di["_openTime"]
            self.startTime = di["_startTime"]
            self.stopTime = di["_stopTime"]




