class bca:
    def students(self,rollno): # multiple parameters
        print(f"My name is {self.name} and roll no is {rollno}")

    @staticmethod  # to create static method and it is used when we need not to get the value of any variable.
    def teacher():
        print("I am your tutor") 

std=bca()
std.name="ram"
std.students(234)

std.teacher()

