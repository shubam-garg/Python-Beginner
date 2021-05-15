class Employee:
    wages = 10000
    def salary(self):
        print("Name of the company is", self.company)
        print("Employee salary is", self.wages)

ram = Employee()
ram.company = "zara"
# ram.salary()
# another way to delaire
Employee.salary(ram) 