class bca:
    def __init__(self,name,rollno,subject): # method to call constructor manually
        self.name = name
        self.rollno = rollno
        self.subject = subject
        print("I am constructor")

    def getDetails(self):
        print(f"{self.name} your roll no is {self.rollno},I am you {self.subject} teacher")

std = bca("Ram",453,"mathematics")
std.getDetails()