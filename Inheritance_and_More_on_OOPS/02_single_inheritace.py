class Base:
    name="Mr"
    _class="7th"
    def baseClass(self):
        print("base class")

class Drived(Base):
    name="Garg"
    def singleInheritance(self):
        print("drived class")

b=Base()
b.baseClass()
d=Drived()
d.singleInheritance()