import csv

class Call:
    def __init__(self, call: str="", time:float=0 , src:int= 0, dest:int= 0, elevator:int= 0,F:int=-1 ) -> None:
        self.call =call
        self.time = time
        self.src = src
        self.dest = dest
        self.F = F
        self.elevator = elevator

    def __repr__(self):
        return f"{self.call} time ={self.time} src ={self.src} dest = {self.dest} elevator = {self.elevator}"


