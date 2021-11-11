import json
class Elevator:
    def __init__(self):
        self.id=0
        self.speed=0
        self.minFloor=0
        self.maxFloor=0
        self.closeTime=0
        self.openTime=0
        self.startTime=0
        self.stopTime=0

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




