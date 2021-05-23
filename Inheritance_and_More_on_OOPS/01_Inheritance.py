class Employee:
    name="Mr"
    _class="7th"
    def baseClass(self):
        print("call to baseclass")

class Trainee(Employee):
    name="Garg"# if I will not define this then p.name function will call the value of name from base class. 
    def derivedClass(self):
        print("call to derivedclass")

    def baseClass(self):
        print("fuction overwrite")

e=Employee()
e.baseClass() 
t=Trainee()
t.derivedClass()
t.baseClass()
print(t.name)
print(t._class)