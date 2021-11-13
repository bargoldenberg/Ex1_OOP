import csv

class Call:
    def __init__(self, call: str="", time:float=0 , src:int= 0, dest:int= 0, elevator:int= 0,F:int=-1 ) -> None:
        self.call =call
        self.time = time
        self.src = src
        self.dest = dest
        self.elevator = elevator
        self.F = F

    def __repr__(self):
        return f"{self.call} time ={self.time} src ={self.src} dest = {self.dest} elevator = {self.elevator}"




"""""""""
    def from_Csv(self, file_name):
        with open(file_name) as fp:
            di = csv.load(fp)
            self.call = di["_id"]
            self.time = di["_speed"]
            self.src = di["_minFloor"]
            self.dest = di["_maxFloor"]
            self.elevator = di["_closeTime"]
            self.F = di["_openTime"]
"""

