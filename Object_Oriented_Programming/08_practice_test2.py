# Write a class calculator capable of finding square,cube and squareroot of a number.

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the suare of {self.number} is {self.number**2}")

    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")

    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number**0.5}")

no = Calculator(45)
no.square()
no.cube()
no.squareroot()