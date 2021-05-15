class Employee:
    company = "amazon"  
    # this is attribute of class to change just attribute rather then making seprate class for next time  

ram = Employee()
sham = Employee()
print(ram.company)
print(sham.company)
Employee.company = "Nike"  # name of company is changed
print(ram.company)
print(sham.company)