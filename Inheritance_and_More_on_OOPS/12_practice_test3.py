''' create a class employee and add salary and increment properties to it.
    write a method salary after increment method with @propert decorator witha setter which changes the value 
    of increment based on salary  '''

class Employee:
    salary=90000
    increment=10000

    @property
    def salaryIncrement(self):
        return self.salary+self.increment

    @salaryIncrement.setter
    def salaryIncrement(self,total):
        self.increment=total-self.salary


e=Employee()
print(e.salaryIncrement)
print(e.increment)
e.salaryIncrement=150000
print(e.increment)

