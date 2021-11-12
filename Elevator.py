import json

class Elevator:
    def __init__(self,id: int=0,speed: float=0,minFloor: int =0,maxFloor: int =0,closeTime: float=0,openTime: float=0, startTime: float=0,stopTime: float=0) -> None:
        self._id=id
        self._speed=speed
        self._minFloor=minFloor
        self._maxFloor=maxFloor
        self._closeTime=closeTime
        self._openTime=openTime
        self._startTime=startTime
        self._stopTime=stopTime

    def from_json(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self._id = di["_id"]
            self._speed = di["_speed"]
            self._minFloor = di["_minFloor"]
            self._maxFloor = di["_maxFloor"]
            self._closeTime = di["_closeTime"]
            self._openTime = di["_openTime"]
            self._startTime = di["_startTime"]
            self._stopTime = di["_stopTime"]




