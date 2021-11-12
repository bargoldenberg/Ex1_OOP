import json

class Elevator:
    def __init__(self,id: int=0,speed: float=0,minFloor: int =0,maxFloor: int =0,closeTime: float=0,openTime: float=0, startTime: float=0,stopTime: float=0) -> None:
        self.id=id
        self.speed=speed
        self.minFloor=minFloor
        self.maxFloor=maxFloor
        self.closeTime=closeTime
        self.openTime=openTime
        self.startTime=startTime
        self.stopTime=stopTime

    def from_json(self, file_name):
        with open(file_name, "r") as fp:
            di = json.load(fp)
            self.id = di["id"]
            self.speed = di["speed"]
            self.minFloor = di["minFloor"]
            self.maxFloor = di["maxFloor"]
            self.closeTime = di["closeTime"]
            self.openTime = di["openTime"]
            self.startTime = di["startTime"]
            self.stopTime = di["stopTime"]




