class machine:
    obj="car"

    def __init__(self):
        print("1st")

    def vehicle(self):
        print("it is a vehicle")

class car(machine):
    model="tata"

    def __init__(self):
        super().__init__()
        print("2nd")

    def vehicle(self):
        super().vehicle()
        print("move vehicle")

class race(car):
    button="pull"

    def __init__(self):
        super().__init__()
        print("3nd")

    def move(self):
        print("you are in child 2")
    def jump(self):
        super().vehicle()
        print("speed")

m=machine()
m.vehicle()
c=car()
c.vehicle()
r=race() 
r.jump()
print(r.obj)