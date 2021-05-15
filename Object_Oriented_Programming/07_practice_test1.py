# Create a class programmer for storing information of few programmers working in microsoft company.

class Programmer:
    company = "Microsoft"
    def __init__(self, name, batchno):
        self.name=name
        self.batchno=batchno
        print(self.company)

    def getInfo(self):
        print(self.name,self.batchno)

emp1=Programmer("Honey",12)
emp2=Programmer("Money",34)
emp1.getInfo()
emp2.getInfo()