import csv

class Call:
    def __init__(self, call = "", time= 0.0 , src = 0, dest = 0, elevator = 0,F=-1 ):
        self.call =call
        self.time = time
        self.src = src
        self.dest = dest
        self.elevator = elevator
        self.F = F
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

