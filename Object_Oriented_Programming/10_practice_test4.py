# add a static method in problem 2 to greet the user with hello

class Calculator:
    def __init__(self, num):
        self.number = num

    def square(self):
        print(f"the suare of {self.number} is {self.number**2}")

    def cube(self):
        print(f"the cube of {self.number} is {self.number**3}")

    def squareroot(self):
        print(f"the squareroot of {self.number} is {self.number**0.5}")

    @staticmethod
    def user():
        print("Hello")

no = Calculator(45)
no.user()
no.square()
no.cube()
no.squareroot()