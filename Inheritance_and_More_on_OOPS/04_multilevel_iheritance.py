# race call car and car call machine
class machine:
    obj="car"

    def vehicle(self):
        print("it is a vehicle")

class car(machine):
    model="tata"

    def vehicle(self):
        print("move vehicle")

class race(car):
    button="pull"

    def move(self):
        print("you are in child 2")
    def jump(self):
        print("speed")

m=machine()
m.vehicle()
c=car()
c.vehicle()
r=race() 
r.vehicle()
print(r.obj)