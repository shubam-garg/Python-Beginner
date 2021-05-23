# multiple parent class and single child
class base_1:
    name="rani"
    born=1965

class base_2:
    name="raja"
    age=5
    def updateage(self):
       self.age=self.age+1

class child (base_1 , base_2):
    kid="baby"

c=child()
c.updateage()
print(c.name) # this function will give priority to first defied class in child for inheritance